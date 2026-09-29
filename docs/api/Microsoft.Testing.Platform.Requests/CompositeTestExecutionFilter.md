# CompositeTestExecutionFilter class

- Namespace: `Microsoft.Testing.Platform.Requests`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents an explicit composition of test execution filters.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public sealed class CompositeTestExecutionFilter : ITestExecutionFilter
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Constructors

### CompositeTestExecutionFilter

```csharp
public CompositeTestExecutionFilter(TestExecutionFilterOperator operator, params ITestExecutionFilter[] filters)
```

Initializes a new instance of the `CompositeTestExecutionFilter` class.

**Parameters:**

- `operator`: The operator used to combine the child filters.
- `filters`: The child filters.

## Properties

### Filters

```csharp
public IReadOnlyList<ITestExecutionFilter> Filters { get; }
```

Gets the child filters.

### Operator

```csharp
public TestExecutionFilterOperator Operator { get; }
```

Gets the operator used to combine the child filters.
