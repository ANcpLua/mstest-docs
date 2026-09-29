#:package System.Reflection.MetadataLoadContext@10.0.0
#:property PublishAot=false
// Writes one Markdown page per public type of the given assemblies, from metadata plus the XML doc file next to each assembly.
// Usage: dotnet run scripts/api_reference.cs -- <outDir> <package> <version> <assembly.dll> [<assembly.dll> ...]
using System.Reflection;
using System.Runtime.InteropServices;
using System.Text;
using System.Text.RegularExpressions;
using System.Xml.Linq;

if (args.Length < 4)
{
    Console.Error.WriteLine("usage: api_reference.cs <outDir> <package> <version> <assembly.dll>...");
    return 1;
}

var outDir = args[0];
var package = args[1];
var version = args[2];
var assemblies = args[3..].Select(Path.GetFullPath).ToArray();

var probe = Directory.GetFiles(RuntimeEnvironment.GetRuntimeDirectory(), "*.dll")
    .Concat(assemblies.SelectMany(a => Directory.GetFiles(Path.GetDirectoryName(a)!, "*.dll")))
    .GroupBy(Path.GetFileName)
    .Select(g => g.First());
using var context = new MetadataLoadContext(new PathAssemblyResolver(probe));

var docs = assemblies.Select(a => Path.ChangeExtension(a, ".xml")).Where(File.Exists)
    .SelectMany(xml => XDocument.Load(xml, LoadOptions.PreserveWhitespace).Descendants("member"))
    .Where(m => m.Attribute("name") is not null)
    .GroupBy(m => m.Attribute("name")!.Value)
    .ToDictionary(g => g.Key, g => g.First());

var pages = 0;
foreach (var path in assemblies)
{
    var assembly = context.LoadFromAssemblyPath(path);
    foreach (var type in assembly.GetTypes().Where(Api.IsVisible).OrderBy(t => t.FullName, StringComparer.Ordinal))
    {
        var file = Path.Combine(outDir, type.Namespace ?? "global", Api.FileName(type) + ".md");
        Directory.CreateDirectory(Path.GetDirectoryName(file)!);
        File.WriteAllText(file, new Page(type, docs, package, version, Path.GetFileName(path)).Render());
        pages++;
    }
}

Console.WriteLine($"{package} {version}: {pages} API pages");
return 0;

static class Api
{
    const BindingFlags Declared = BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance | BindingFlags.Static | BindingFlags.DeclaredOnly;

    static readonly Dictionary<string, string> Keywords = new()
    {
        ["System.Void"] = "void", ["System.Object"] = "object", ["System.String"] = "string", ["System.Boolean"] = "bool",
        ["System.Byte"] = "byte", ["System.SByte"] = "sbyte", ["System.Int16"] = "short", ["System.UInt16"] = "ushort",
        ["System.Int32"] = "int", ["System.UInt32"] = "uint", ["System.Int64"] = "long", ["System.UInt64"] = "ulong",
        ["System.Single"] = "float", ["System.Double"] = "double", ["System.Decimal"] = "decimal", ["System.Char"] = "char",
        ["System.IntPtr"] = "nint", ["System.UIntPtr"] = "nuint",
    };

    static readonly HashSet<string> ShownAttributes =
    [
        "AttributeUsageAttribute", "ObsoleteAttribute", "ExperimentalAttribute", "FlagsAttribute", "DoesNotReturnAttribute",
        "CallerArgumentExpressionAttribute", "CallerMemberNameAttribute", "CallerFilePathAttribute", "CallerLineNumberAttribute",
        "NotNullAttribute", "NotNullWhenAttribute", "MaybeNullWhenAttribute", "DoesNotReturnIfAttribute", "StringSyntaxAttribute",
    ];

    public static bool IsVisible(Type type)
    {
        for (var t = type; t is not null; t = t.DeclaringType)
        {
            var visible = t.IsNested ? t.IsNestedPublic || t.IsNestedFamily || t.IsNestedFamORAssem : t.IsPublic;
            if (!visible || IsHidden(t.GetCustomAttributesData()) || t.Name.Contains('<'))
            {
                return false;
            }
        }

        return true;
    }

    public static bool IsVisible(MethodBase? method) => method is not null && (method.IsPublic || method.IsFamily || method.IsFamilyOrAssembly);

    public static bool IsHidden(IEnumerable<CustomAttributeData> attributes) => attributes.Any(a =>
        a.AttributeType.Name == "CompilerGeneratedAttribute"
        || (a.AttributeType.Name == "EditorBrowsableAttribute" && a.ConstructorArguments.Count == 1 && Convert.ToInt32(a.ConstructorArguments[0].Value) == 1));

    public static IEnumerable<T> Members<T>(Type type) where T : MemberInfo =>
        type.GetMembers(Declared).OfType<T>().Where(m => !IsHidden(m.GetCustomAttributesData()) && !m.Name.Contains('<'));

    public static string FileName(Type type) => (type.IsNested ? FileName(type.DeclaringType!) + "." : "") + type.Name.Replace('`', '-');

    public static string Kind(Type type) =>
        type.IsEnum ? "enum"
        : type.IsInterface ? "interface"
        : IsDelegate(type) ? "delegate"
        : type.IsValueType ? "struct"
        : "class";

    public static bool IsDelegate(Type type) => type.BaseType?.FullName == "System.MulticastDelegate";

    public static string StripArity(string name) => name.Contains('`') ? name[..name.IndexOf('`')] : name;

    /// <summary>Type name as C# writes it; <paramref name="qualified"/> keeps the declaring types of a nested type.</summary>
    public static string Name(Type type, NullabilityInfo? nullability = null, bool qualified = true)
    {
        if (type.IsByRef)
        {
            return Name(type.GetElementType()!, nullability, qualified);
        }

        var suffix = nullability?.ReadState == NullabilityState.Nullable && !type.IsValueType ? "?" : "";
        if (type.IsArray)
        {
            var commas = new string(',', type.GetArrayRank() - 1);
            return $"{Name(type.GetElementType()!, nullability?.ElementType, qualified)}[{commas}]{suffix}";
        }

        if (type.IsPointer)
        {
            return Name(type.GetElementType()!, null, qualified) + "*";
        }

        if (type.IsGenericParameter)
        {
            return type.Name + suffix;
        }

        if (type.IsGenericType && !type.IsGenericTypeDefinition && type.GetGenericTypeDefinition().FullName == "System.Nullable`1")
        {
            return Name(type.GetGenericArguments()[0], nullability?.GenericTypeArguments.FirstOrDefault(), qualified) + "?";
        }

        if (type.FullName is { } fullName && Keywords.TryGetValue(fullName, out var keyword))
        {
            return keyword + suffix;
        }

        var arguments = type.GetGenericArguments();
        var chain = new List<Type>();
        for (var t = type; t is not null; t = qualified ? t.DeclaringType : null)
        {
            chain.Insert(0, t);
        }

        var used = 0;
        var parts = new List<string>();
        foreach (var t in chain)
        {
            var arity = t.GetGenericArguments().Length - used;
            var part = StripArity(t.Name);
            if (arity > 0)
            {
                var names = Enumerable.Range(used, arity).Select(i =>
                    Name(arguments[i], nullability is not null && i < nullability.GenericTypeArguments.Length ? nullability.GenericTypeArguments[i] : null));
                part += $"<{string.Join(", ", names)}>";
                used += arity;
            }

            parts.Add(part);
        }

        return string.Join(".", parts) + suffix;
    }

    public static string Access(MethodBase method) =>
        method.IsPublic ? "public" : method.IsFamily ? "protected" : method.IsFamilyOrAssembly ? "protected internal" : "internal";

    public static string Modifiers(MethodBase method)
    {
        if (method.DeclaringType!.IsInterface)
        {
            return method.IsStatic ? "static " + (method.IsAbstract ? "abstract " : "") : "";
        }

        var text = Access(method) + " ";
        if (method.IsStatic)
        {
            return text + "static ";
        }

        var isOverride = method.IsVirtual && (method.Attributes & MethodAttributes.NewSlot) == 0;
        if (method.IsAbstract)
        {
            return text + "abstract " + (isOverride ? "override " : "");
        }

        if (isOverride)
        {
            return text + (method.IsFinal ? "sealed " : "") + "override ";
        }

        return text + (method.IsVirtual && !method.IsFinal ? "virtual " : "");
    }

    public static string Literal(object? value, Type type)
    {
        var target = type.IsByRef ? type.GetElementType()! : type;
        if (target.IsGenericType && !target.IsGenericTypeDefinition && target.GetGenericTypeDefinition().FullName == "System.Nullable`1")
        {
            target = target.GetGenericArguments()[0];
        }

        if (value is null)
        {
            return target.IsValueType || target.IsGenericParameter ? "default" : "null";
        }

        if (target.IsEnum)
        {
            return EnumLiteral(target, value);
        }

        return value switch
        {
            string s => "\"" + s.Replace("\\", "\\\\").Replace("\"", "\\\"").Replace("\n", "\\n").Replace("\r", "\\r").Replace("\t", "\\t") + "\"",
            char c => $"'{c}'",
            bool b => b ? "true" : "false",
            float f => f.ToString("R", System.Globalization.CultureInfo.InvariantCulture) + "f",
            IFormattable f => f.ToString(null, System.Globalization.CultureInfo.InvariantCulture),
            _ => value.ToString() ?? "default",
        };
    }

    public static string EnumLiteral(Type type, object value)
    {
        var number = Convert.ToInt64(value, System.Globalization.CultureInfo.InvariantCulture);
        var fields = type.GetFields(BindingFlags.Public | BindingFlags.Static)
            .Select(f => (f.Name, Value: Convert.ToInt64(f.GetRawConstantValue(), System.Globalization.CultureInfo.InvariantCulture)))
            .ToList();
        var exact = fields.FirstOrDefault(f => f.Value == number);
        if (exact.Name is not null)
        {
            return $"{type.Name}.{exact.Name}";
        }

        var flags = fields.Where(f => f.Value != 0 && (number & f.Value) == f.Value).ToList();
        return flags.Count > 0 && flags.Aggregate(0L, (sum, f) => sum | f.Value) == number
            ? string.Join(" | ", flags.Select(f => $"{type.Name}.{f.Name}"))
            : $"({type.Name}){number}";
    }

    public static string Attributes(IEnumerable<CustomAttributeData> attributes, string separator)
    {
        var text = new StringBuilder();
        foreach (var attribute in attributes.Where(a => ShownAttributes.Contains(a.AttributeType.Name)))
        {
            var arguments = attribute.ConstructorArguments.Select(Argument)
                .Concat(attribute.NamedArguments.Select(n => $"{n.MemberName} = {Argument(n.TypedValue)}"))
                .ToList();
            var name = attribute.AttributeType.Name[..^"Attribute".Length];
            text.Append('[').Append(name).Append(arguments.Count > 0 ? $"({string.Join(", ", arguments)})" : "").Append(']').Append(separator);
        }

        return text.ToString();
    }

    static string Argument(CustomAttributeTypedArgument argument) => argument.Value switch
    {
        IEnumerable<CustomAttributeTypedArgument> items => $"[{string.Join(", ", items.Select(Argument))}]",
        Type type => $"typeof({Name(type)})",
        var value => Literal(value, argument.ArgumentType),
    };

    /// <summary>Documentation comment ID, the key of a member in the XML doc file.</summary>
    public static string DocId(MemberInfo member) => member switch
    {
        Type type => "T:" + DocName(type),
        MethodBase method => "M:" + DocName(method.DeclaringType!) + "." + method.Name.Replace('.', '#')
            + (method.IsGenericMethod ? "``" + method.GetGenericArguments().Length : "")
            + DocParameters(method.GetParameters())
            + (method.Name is "op_Implicit" or "op_Explicit" ? "~" + DocParameter(((MethodInfo)method).ReturnType) : ""),
        PropertyInfo property => "P:" + DocName(property.DeclaringType!) + "." + property.Name.Replace('.', '#') + DocParameters(property.GetIndexParameters()),
        FieldInfo field => "F:" + DocName(field.DeclaringType!) + "." + field.Name,
        EventInfo @event => "E:" + DocName(@event.DeclaringType!) + "." + @event.Name.Replace('.', '#'),
        _ => "",
    };

    public static string DocName(Type type) => (type.IsNested ? DocName(type.DeclaringType!) : type.Namespace) is { Length: > 0 } prefix
        ? prefix + "." + type.Name
        : type.Name;

    static string DocParameters(ParameterInfo[] parameters) =>
        parameters.Length == 0 ? "" : $"({string.Join(",", parameters.Select(p => DocParameter(p.ParameterType)))})";

    static string DocParameter(Type type)
    {
        if (type.IsByRef)
        {
            return DocParameter(type.GetElementType()!) + "@";
        }

        if (type.IsArray)
        {
            var rank = type.GetArrayRank();
            return DocParameter(type.GetElementType()!) + (rank == 1 ? "[]" : $"[{string.Join(",", Enumerable.Repeat("0:", rank))}]");
        }

        if (type.IsPointer)
        {
            return DocParameter(type.GetElementType()!) + "*";
        }

        if (type.IsGenericParameter)
        {
            return (type.DeclaringMethod is not null ? "``" : "`") + type.GenericParameterPosition;
        }

        if (!type.IsGenericType)
        {
            return DocName(type);
        }

        var arguments = type.GetGenericArguments();
        var chain = new List<Type>();
        for (var t = type; t is not null; t = t.DeclaringType)
        {
            chain.Insert(0, t);
        }

        var used = 0;
        var parts = new List<string>();
        foreach (var t in chain)
        {
            var arity = t.GetGenericArguments().Length - used;
            parts.Add(StripArity(t.Name) + (arity > 0 ? $"{{{string.Join(",", arguments.Skip(used).Take(arity).Select(DocParameter))}}}" : ""));
            used += arity;
        }

        return (type.Namespace is { Length: > 0 } ns ? ns + "." : "") + string.Join(".", parts);
    }
}

sealed class Page(Type type, Dictionary<string, XElement> docs, string package, string version, string assembly)
{
    readonly NullabilityInfoContext _nullability = new();
    readonly StringBuilder _text = new();

    public string Render()
    {
        var doc = Doc(type);
        _text.AppendLine($"# {Api.Name(type)} {Api.Kind(type)}").AppendLine();
        _text.AppendLine($"- Namespace: `{type.Namespace}`");
        _text.AppendLine($"- Assembly: `{assembly}`");
        _text.AppendLine($"- Package: `{package}` {version}").AppendLine();
        Paragraph(doc?.Element("summary"));
        Code(TypeDeclaration());
        TypeParameters(doc);
        if (Api.IsDelegate(type))
        {
            Parameters(doc);
            Labelled("Returns", doc?.Element("returns"));
        }

        Section("Remarks", doc?.Element("remarks"), "##");
        Examples(doc, "##");

        if (type.IsEnum)
        {
            Fields("Fields", type.GetFields(BindingFlags.Public | BindingFlags.Static));
        }
        else if (!Api.IsDelegate(type))
        {
            Group("Constructors", Api.Members<ConstructorInfo>(type).Where(c => Api.IsVisible(c) && !c.IsStatic), _ => Api.StripArity(type.Name), Constructor);
            Fields("Fields", Api.Members<FieldInfo>(type).Where(f => f.IsPublic || f.IsFamily || f.IsFamilyOrAssembly));
            Group("Properties", Api.Members<PropertyInfo>(type).Where(p => Api.IsVisible(p.GetMethod) || Api.IsVisible(p.SetMethod)), p => p.Name, Property);
            Group("Methods", Api.Members<MethodInfo>(type).Where(m => Api.IsVisible(m) && !m.IsSpecialName), m => m.Name, Method);
            Group("Operators", Api.Members<MethodInfo>(type).Where(m => Api.IsVisible(m) && m.IsSpecialName && m.Name.StartsWith("op_", StringComparison.Ordinal)), m => m.Name[3..], Method);
            Group("Events", Api.Members<EventInfo>(type).Where(e => Api.IsVisible(e.AddMethod)), e => e.Name, Event);
        }

        return Regex.Replace(_text.ToString(), @"\n{3,}", "\n\n").TrimEnd() + "\n";
    }

    string TypeDeclaration()
    {
        var attributes = Api.Attributes(type.GetCustomAttributesData(), "\n");
        var access = type.IsNested ? (type.IsNestedPublic ? "public" : "protected") : "public";
        if (Api.IsDelegate(type))
        {
            var invoke = type.GetMethod("Invoke")!;
            return $"{attributes}{access} delegate {Return(invoke)} {Api.Name(type, qualified: false)}({ParameterList(invoke.GetParameters())});";
        }

        if (type.IsEnum)
        {
            var underlying = type.GetEnumUnderlyingType();
            return $"{attributes}{access} enum {type.Name}" + (underlying.FullName == "System.Int32" ? "" : $" : {Api.Name(underlying)}");
        }

        var modifiers = type.IsInterface ? ""
            : type.IsValueType ? (HasAttribute(type, "IsReadOnlyAttribute") ? "readonly " : "") + (HasAttribute(type, "IsByRefLikeAttribute") ? "ref " : "")
            : type.IsAbstract && type.IsSealed ? "static "
            : type.IsAbstract ? "abstract "
            : type.IsSealed ? "sealed "
            : "";
        var bases = new List<string>();
        if (type is { IsClass: true, BaseType: { FullName: not "System.Object" } baseType })
        {
            bases.Add(Api.Name(baseType));
        }

        var inherited = type.BaseType?.GetInterfaces() ?? [];
        bases.AddRange(type.GetInterfaces().Where(i => Api.IsVisible(i) || i.Namespace!.StartsWith("System", StringComparison.Ordinal))
            .Where(i => !inherited.Contains(i))
            .Select(i => Api.Name(i)));
        return $"{attributes}{access} {modifiers}{Api.Kind(type)} {Api.Name(type, qualified: false)}" + (bases.Count > 0 ? $" : {string.Join(", ", bases)}" : "");
    }

    static bool HasAttribute(Type type, string name) => type.GetCustomAttributesData().Any(a => a.AttributeType.Name == name);

    void Group<T>(string title, IEnumerable<T> members, Func<T, string> name, Func<T, string> signature) where T : MemberInfo
    {
        var groups = members.GroupBy(name).OrderBy(g => g.Key, StringComparer.Ordinal).ToList();
        if (groups.Count == 0)
        {
            return;
        }

        _text.AppendLine($"## {title}").AppendLine();
        foreach (var group in groups)
        {
            _text.AppendLine($"### {group.Key}").AppendLine();
            foreach (var member in group.OrderBy(m => (m as MethodBase)?.GetParameters().Length ?? 0).ThenBy(signature, StringComparer.Ordinal))
            {
                var doc = Doc(member);
                Code(signature(member));
                Paragraph(doc?.Element("summary"));
                TypeParameters(doc);
                Parameters(doc);
                Labelled(member is PropertyInfo ? "Value" : "Returns", doc?.Element(member is PropertyInfo ? "value" : "returns"));
                Exceptions(doc);
                Section("Remarks", doc?.Element("remarks"), "####");
                Examples(doc, "####");
            }
        }
    }

    void Fields(string title, IEnumerable<FieldInfo> fields)
    {
        var rows = fields.Where(f => !f.IsSpecialName && !Api.IsHidden(f.GetCustomAttributesData())).ToList();
        if (rows.Count == 0)
        {
            return;
        }

        _text.AppendLine($"## {title}").AppendLine();
        if (type.IsEnum)
        {
            _text.AppendLine("| Name | Value | Description |").AppendLine("| --- | --- | --- |");
            foreach (var field in rows)
            {
                _text.AppendLine($"| `{field.Name}` | `{Api.Literal(field.GetRawConstantValue(), type.GetEnumUnderlyingType())}` | {Inline(Doc(field)?.Element("summary"))} |");
            }

            _text.AppendLine();
            return;
        }

        foreach (var field in rows.OrderBy(f => f.Name, StringComparer.Ordinal))
        {
            var modifiers = (field.IsPublic ? "public " : "protected ") + (field.IsLiteral ? "const " : (field.IsStatic ? "static " : "") + (field.IsInitOnly ? "readonly " : ""));
            var value = field.IsLiteral ? " = " + Api.Literal(field.GetRawConstantValue(), field.FieldType) : "";
            _text.AppendLine($"### {field.Name}").AppendLine();
            Code($"{modifiers}{Api.Name(field.FieldType, Nullability(() => _nullability.Create(field)))} {field.Name}{value}");
            Paragraph(Doc(field)?.Element("summary"));
        }
    }

    string Constructor(ConstructorInfo constructor) =>
        $"{Api.Attributes(constructor.GetCustomAttributesData(), "\n")}{Api.Modifiers(constructor)}{Api.StripArity(type.Name)}({ParameterList(constructor.GetParameters())})";

    string Method(MethodInfo method)
    {
        var attributes = Api.Attributes(method.GetCustomAttributesData(), "\n");
        var parameters = ParameterList(method.GetParameters(), method.IsDefined("System.Runtime.CompilerServices.ExtensionAttribute"));
        if (method.Name is "op_Implicit" or "op_Explicit")
        {
            return $"{attributes}public static {method.Name[3..].ToLowerInvariant()} operator {Return(method)}({parameters})";
        }

        var generic = method.IsGenericMethod ? $"<{string.Join(", ", method.GetGenericArguments().Select(a => a.Name))}>" : "";
        var name = method.IsSpecialName && method.Name.StartsWith("op_", StringComparison.Ordinal) ? "operator " + method.Name[3..] : method.Name;
        return $"{attributes}{Api.Modifiers(method)}{Return(method)} {name}{generic}({parameters})";
    }

    string Property(PropertyInfo property)
    {
        var lead = new[] { property.GetMethod, property.SetMethod }.Where(Api.IsVisible).OrderBy(a => a!.IsPublic ? 0 : 1).First()!;
        var accessors = new List<string>();
        if (Api.IsVisible(property.GetMethod))
        {
            accessors.Add(Accessor(property.GetMethod!, lead, "get"));
        }

        if (Api.IsVisible(property.SetMethod))
        {
            var init = property.SetMethod!.ReturnParameter.GetRequiredCustomModifiers().Any(m => m.Name == "IsExternalInit");
            accessors.Add(Accessor(property.SetMethod!, lead, init ? "init" : "set"));
        }

        var index = property.GetIndexParameters();
        var name = index.Length > 0 ? $"this[{ParameterList(index)}]" : property.Name;
        var propertyType = Api.Name(property.PropertyType, Nullability(() => _nullability.Create(property)));
        return $"{Api.Attributes(property.GetCustomAttributesData(), "\n")}{Api.Modifiers(lead)}{propertyType} {name} {{ {string.Join(" ", accessors)} }}";
    }

    static string Accessor(MethodBase accessor, MethodBase lead, string keyword) =>
        (Api.Access(accessor) == Api.Access(lead) || accessor.DeclaringType!.IsInterface ? "" : Api.Access(accessor) + " ") + keyword + ";";

    string Event(EventInfo @event) =>
        $"{Api.Modifiers(@event.AddMethod!)}event {Api.Name(@event.EventHandlerType!, Nullability(() => _nullability.Create(@event)))} {@event.Name}";

    string Return(MethodInfo method) => Api.Name(method.ReturnType, Nullability(() => _nullability.Create(method.ReturnParameter)));

    string ParameterList(ParameterInfo[] parameters, bool extension = false)
    {
        var items = parameters.Select((p, i) =>
        {
            var modifier = p.ParameterType.IsByRef ? (p.IsOut ? "out " : p.IsIn ? "in " : "ref ") : "";
            var prefix = (extension && i == 0 ? "this " : "") + (p.IsDefined("System.ParamArrayAttribute") || p.IsDefined("System.Runtime.CompilerServices.ParamCollectionAttribute") ? "params " : "");
            var value = p.HasDefaultValue ? " = " + Api.Literal(p.RawDefaultValue, p.ParameterType) : "";
            return $"{Api.Attributes(p.GetCustomAttributesData(), " ")}{prefix}{modifier}{Api.Name(p.ParameterType, Nullability(() => _nullability.Create(p)))} {p.Name}{value}";
        }).ToList();
        return items.Count > 2 || items.Sum(i => i.Length) > 100
            ? "\n    " + string.Join(",\n    ", items)
            : string.Join(", ", items);
    }

    static NullabilityInfo? Nullability(Func<NullabilityInfo> read)
    {
        try
        {
            return read();
        }
        catch (Exception)
        {
            return null;
        }
    }

    XElement? Doc(MemberInfo member)
    {
        var id = Api.DocId(member);
        if (!docs.TryGetValue(id, out var doc))
        {
            return null;
        }

        if (doc.Element("inheritdoc") is not { } inherit)
        {
            return doc;
        }

        if (inherit.Attribute("cref")?.Value is { } cref)
        {
            return docs.GetValueOrDefault(cref, doc);
        }

        // <inheritdoc/> without a target: the same member on a base type or an implemented interface.
        var owner = member as Type ?? member.DeclaringType!;
        var rest = id[(2 + Api.DocName(owner).Length)..];
        var ancestors = new List<Type>();
        for (var t = owner.BaseType; t is not null; t = t.BaseType)
        {
            ancestors.Add(t);
        }

        return ancestors.Concat(owner.GetInterfaces())
            .Select(t => docs.GetValueOrDefault(id[..2] + Api.DocName(t.IsGenericType ? t.GetGenericTypeDefinition() : t) + rest))
            .FirstOrDefault(d => d is not null && d.Element("inheritdoc") is null) ?? doc;
    }

    void Code(string code) => _text.AppendLine("```csharp").AppendLine(code).AppendLine("```").AppendLine();

    void Paragraph(XElement? element)
    {
        var text = Block(element);
        if (text.Length > 0)
        {
            _text.AppendLine(text).AppendLine();
        }
    }

    void Section(string title, XElement? element, string level)
    {
        var text = Block(element);
        if (text.Length > 0)
        {
            _text.AppendLine($"{level} {title}").AppendLine().AppendLine(text).AppendLine();
        }
    }

    void Examples(XElement? doc, string level)
    {
        foreach (var example in doc?.Elements("example") ?? [])
        {
            Section("Example", example, level);
        }
    }

    void Labelled(string label, XElement? element)
    {
        var text = Inline(element);
        if (text.Length > 0)
        {
            _text.AppendLine($"**{label}:** {text}").AppendLine();
        }
    }

    void TypeParameters(XElement? doc) => Named("Type parameters", doc?.Elements("typeparam"), "name");

    void Parameters(XElement? doc) => Named("Parameters", doc?.Elements("param"), "name");

    void Exceptions(XElement? doc) => Named("Exceptions", doc?.Elements("exception"), "cref");

    void Named(string label, IEnumerable<XElement>? elements, string attribute)
    {
        var rows = (elements ?? []).Select(e => (Name: Reference(e.Attribute(attribute)?.Value ?? ""), Text: Inline(e))).Where(r => r.Name.Length > 0).ToList();
        if (rows.Count == 0)
        {
            return;
        }

        _text.AppendLine($"**{label}:**").AppendLine();
        foreach (var (name, text) in rows)
        {
            _text.AppendLine($"- `{name}`" + (text.Length > 0 ? $": {text}" : ""));
        }

        _text.AppendLine();
    }

    static string Inline(XElement? element) => Regex.Replace(Block(element), @"\s*\n\s*", " ").Replace("|", "\\|");

    static string Block(XElement? element)
    {
        if (element is null)
        {
            return "";
        }

        var text = new StringBuilder();
        foreach (var node in element.Nodes())
        {
            text.Append(node switch
            {
                XText t => Regex.Replace(t.Value, @"\s+", " "),
                XElement e => Element(e),
                _ => "",
            });
        }

        var lines = text.ToString().Split('\n').Select(l => l.StartsWith("    ", StringComparison.Ordinal) || l.StartsWith("```", StringComparison.Ordinal) ? l : l.Trim());
        return Regex.Replace(string.Join("\n", lines), @"\n{3,}", "\n\n").Trim();
    }

    static string Element(XElement element) => element.Name.LocalName switch
    {
        "see" or "seealso" => See(element),
        "paramref" or "typeparamref" => $"`{element.Attribute("name")?.Value}`",
        "c" => $"`{element.Value}`",
        "code" => $"\n\n```csharp\n{Dedent(element.Value)}\n```\n\n",
        "para" or "p" => $"\n\n{Block(element)}\n\n",
        "br" => "\n\n",
        "list" => "\n\n" + string.Join("\n", element.Elements().Where(i => i.Name.LocalName is "item" or "listheader").Select(Item)) + "\n\n",
        "b" or "strong" => $"**{Block(element)}**",
        "i" or "em" => $"*{Block(element)}*",
        "a" => $"[{Block(element)}]({element.Attribute("href")?.Value})",
        _ => Block(element),
    };

    static string Item(XElement item)
    {
        var term = Inline(item.Element("term"));
        var description = Inline(item.Element("description"));
        var text = term.Length > 0 && description.Length > 0 ? $"**{term}**: {description}"
            : term.Length > 0 ? term
            : description.Length > 0 ? description
            : Inline(item);
        return "- " + text;
    }

    static string See(XElement element)
    {
        if (element.Attribute("langword")?.Value is { } keyword)
        {
            return $"`{keyword}`";
        }

        if (element.Attribute("href")?.Value is { } href)
        {
            return $"[{(element.Value.Length > 0 ? element.Value : href)}]({href})";
        }

        return element.Value.Length > 0 ? element.Value : $"`{Reference(element.Attribute("cref")?.Value ?? "")}`";
    }

    /// <summary>Short readable form of a documentation comment ID: <c>M:Ns.Type.Method(System.String)</c> becomes <c>Type.Method(string)</c>.</summary>
    static string Reference(string id)
    {
        if (id.Length < 2 || id[1] != ':')
        {
            return id;
        }

        var kind = id[0];
        var body = id[2..];
        var open = body.IndexOf('(');
        var arguments = open >= 0 ? body[open..] : "";
        var path = Regex.Replace(open >= 0 ? body[..open] : body, @"`+\d+", "").Replace("#ctor", "ctor").Split('.');
        var name = string.Join(".", kind is 'T' or '!' ? path[^1..] : path[Math.Max(0, path.Length - 2)..]);
        if (arguments.Length == 0)
        {
            return name;
        }

        var types = Regex.Replace(arguments, @"[A-Za-z_][\w.]*\.", "");
        types = Regex.Replace(types, @"``?(\d+)", "T$1").Replace('{', '<').Replace('}', '>').Replace("@", "");
        return name + types;
    }

    static string Dedent(string code)
    {
        var lines = code.Replace("\r", "").Split('\n').ToList();
        while (lines.Count > 0 && lines[0].Trim().Length == 0)
        {
            lines.RemoveAt(0);
        }

        while (lines.Count > 0 && lines[^1].Trim().Length == 0)
        {
            lines.RemoveAt(lines.Count - 1);
        }

        var indent = lines.Where(l => l.Trim().Length > 0).Select(l => l.Length - l.TrimStart().Length).DefaultIfEmpty(0).Min();
        return string.Join("\n", lines.Select(l => l.Length >= indent ? l[indent..] : l));
    }
}

static class ReflectionExtensions
{
    public static bool IsDefined(this MethodBase method, string attribute) => method.GetCustomAttributesData().Any(a => a.AttributeType.FullName == attribute);

    public static bool IsDefined(this ParameterInfo parameter, string attribute) => parameter.GetCustomAttributesData().Any(a => a.AttributeType.FullName == attribute);
}
