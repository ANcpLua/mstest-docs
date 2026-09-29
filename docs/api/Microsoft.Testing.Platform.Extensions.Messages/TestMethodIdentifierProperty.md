# TestMethodIdentifierProperty class

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Property that uniquely identifies a test method. Values are ECMA-335 compliant.

```csharp
public sealed class TestMethodIdentifierProperty : IProperty, IEquatable<TestMethodIdentifierProperty>
```

## Constructors

### TestMethodIdentifierProperty

```csharp
public TestMethodIdentifierProperty(
    string assemblyFullName,
    string namespace,
    string typeName,
    string methodName,
    int methodArity,
    string[] parameterTypeFullNames,
    string returnTypeFullName)
```

Initializes a new instance of the `TestMethodIdentifierProperty` class.

**Parameters:**

- `assemblyFullName`: Assembly full name.
- `namespace`: Namespace.
- `typeName`: Type name in metadata format, not including the namespace. Generics are represented by backtick followed by arity. Nested types are represented by `+`.
- `methodName`: Method name in metadata format. This is simply the method name, it doesn't include backtick followed by arity.
- `methodArity`: The number of generic parameters of the method.
- `parameterTypeFullNames`: Parameter type full names in metadata format.
- `returnTypeFullName`: Return type full name in metadata format.

## Properties

### AssemblyFullName

```csharp
public string AssemblyFullName { get; }
```

Gets the assembly full name.

### MethodArity

```csharp
public int MethodArity { get; }
```

Gets the number of generic parameters of the method.

### MethodName

```csharp
public string MethodName { get; }
```

Gets the method name in metadata format.

### Namespace

```csharp
public string Namespace { get; }
```

Gets the namespace.

### ParameterTypeFullNames

```csharp
public string[] ParameterTypeFullNames { get; }
```

Gets the parameter type full names in metadata format.

### ReturnTypeFullName

```csharp
public string ReturnTypeFullName { get; }
```

Gets the return type full name in metadata format.

### TypeName

```csharp
public string TypeName { get; }
```

Gets the type name in metadata format, not including the namespace.

## Methods

### Equals

```csharp
public bool Equals(TestMethodIdentifierProperty? other)
```

```csharp
public override bool Equals(object? obj)
```

### GetHashCode

```csharp
public override int GetHashCode()
```

### ToString

```csharp
public override string ToString()
```
