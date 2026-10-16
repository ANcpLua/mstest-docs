# TestExecutionFilterContext class

- Namespace: `Microsoft.Testing.Platform.Requests`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Describes the request for which a test execution filter provider is being evaluated.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public sealed class TestExecutionFilterContext
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Constructors

### TestExecutionFilterContext

```csharp
public TestExecutionFilterContext(TestExecutionRequestKind requestKind, TestExecutionRequestOrigin origin)
```

Initializes a new instance of the `TestExecutionFilterContext` class.

**Parameters:**

- `requestKind`: The request kind.
- `origin`: The request origin.

## Properties

### Origin

```csharp
public TestExecutionRequestOrigin Origin { get; }
```

Gets the request origin.

### RequestKind

```csharp
public TestExecutionRequestKind RequestKind { get; }
```

Gets the request kind.
