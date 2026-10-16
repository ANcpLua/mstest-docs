# TestFilterContext class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

Snapshot of the metadata MSTest exposes to an `ITestFilter` for a single test under consideration.

```csharp
[Experimental("MSTESTEXP", UrlFormat = "https://aka.ms/mstest/diagnostics#{0}")]
public sealed class TestFilterContext
```

## Remarks

Only metadata that is available without loading the test type is exposed; `ITestFilter` must be able to decide using strings, categories, traits, and priority alone. This is what allows the filter to drop tests *before* their declaring type is loaded and before `[AssemblyInitialize]` / `[ClassInitialize]` run.

Properties are mutable (settable) so the platform can populate them via an object initializer and so the type can grow new metadata fields over time without breaking existing `ITestFilter` implementations or their unit tests. MSTest itself does not mutate a `TestFilterContext` after it is handed to an `ITestFilter`; filters should likewise treat the instance they receive as effectively read-only for the duration of the call.

Each property describes a separate facet of the test. The flat string properties (`TestFilterContext.FullyQualifiedName`, `TestFilterContext.DisplayName`) are convenience views and are always populated. The structured properties (`TestFilterContext.Namespace`, `TestFilterContext.ClassName`, `TestFilterContext.ManagedTypeName`, `TestFilterContext.ManagedMethodName`, `TestFilterContext.MethodArity`, `TestFilterContext.ParameterTypeFullNames`) may be `null` when the metadata is not available — typically for tests discovered through code paths that don't surface ECMA-335 managed names.

The type is designed to be extended over time: new properties can be added without breaking existing `ITestFilter` implementations or their unit tests. Consumers construct instances using an object initializer (e.g. `new TestFilterContext { FullyQualifiedName = "…" }`); no positional constructor needs to be updated when new properties land.

This API is experimental. It may change, break, or be removed at any time without notice.

## Constructors

### TestFilterContext

```csharp
public TestFilterContext()
```

## Properties

### Categories

```csharp
public IReadOnlyList<string> Categories { get; set; }
```

Gets or sets the test categories declared via `TestCategoryAttribute` on the method or its declaring class. Defaults to an empty list.

### ClassName

```csharp
public string? ClassName { get; set; }
```

Gets or sets the simple class name (without namespace), or `null` when no managed metadata is available. Nested types are surfaced using their managed metadata form (e.g. `Outer+Inner`); see `TestFilterContext.ManagedTypeName` for the fully escaped ECMA-335 representation.

### DisplayName

```csharp
public string DisplayName { get; set; }
```

Gets or sets the display name of the test, as reported to the runner / IDE.

#### Remarks

Often equal to `TestFilterContext.MethodName`; differs for data-driven tests, tests with a custom `TestMethodAttribute` display name, or attributes that override it.

### FullyQualifiedName

```csharp
public string FullyQualifiedName { get; set; }
```

Gets or sets the fully qualified test name in `Namespace.Class.Method` form.

### ManagedMethodName

```csharp
public string? ManagedMethodName { get; set; }
```

Gets or sets the method name in ECMA-335 metadata form, or `null` when no managed metadata is available.

#### Remarks

Includes the method name, generic arity suffix, and parameter type list (e.g. `MyMethod`1(System.Int32)`). Matches the format defined by the  Managed TestCase Properties RFC.

### ManagedTypeName

```csharp
public string? ManagedTypeName { get; set; }
```

Gets or sets the declaring type name in ECMA-335 metadata form, or `null` when no managed metadata is available.

#### Remarks

Includes the namespace, uses `+` for nested types, and uses backtick + arity for generics (e.g. `Acme.MyOuter+MyInner`1`). Matches the format defined by the  Managed TestCase Properties RFC.

### MethodArity

```csharp
public int? MethodArity { get; set; }
```

Gets or sets the number of generic type parameters declared on the test method, or `null` when no managed metadata is available. Zero indicates a non-generic method.

### MethodName

```csharp
public string MethodName { get; set; }
```

Gets or sets the unqualified test method name (i.e. without class or namespace).

### Namespace

```csharp
public string? Namespace { get; set; }
```

Gets or sets the namespace of the declaring test class, or `null` when no managed metadata is available or the class is in the global namespace.

### ParameterTypeFullNames

```csharp
public IReadOnlyList<string>? ParameterTypeFullNames { get; set; }
```

Gets or sets the ECMA-335-style fully qualified parameter type names of the test method, or `null` when no managed metadata is available. An empty list indicates a parameterless method.

### Priority

```csharp
public int? Priority { get; set; }
```

Gets or sets the `PriorityAttribute` value declared on the test, or `null` when no priority was declared.

### Source

```csharp
public string Source { get; set; }
```

Gets or sets the path to the test assembly file containing this test.

#### Remarks

This is *not* a simple assembly name; see `TestFilterContext.ManagedTypeName` if you need an ECMA-335-style identifier.

### Traits

```csharp
public IReadOnlyList<KeyValuePair<string, string>> Traits { get; set; }
```

Gets or sets the traits attached to this test. Multiple traits can share the same key; consumers must therefore not assume the collection behaves like a dictionary. Defaults to an empty list.
