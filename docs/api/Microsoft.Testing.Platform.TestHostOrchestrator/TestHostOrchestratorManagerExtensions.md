# TestHostOrchestratorManagerExtensions class

- Namespace: `Microsoft.Testing.Platform.TestHostOrchestrator`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Extension methods for `ITestHostOrchestratorManager`.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public static class TestHostOrchestratorManagerExtensions
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Methods

### AddTestHostExecutionOrchestratorMiddleware

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public static void AddTestHostExecutionOrchestratorMiddleware(
    this ITestHostOrchestratorManager manager,
    Func<IServiceProvider, ITestHostExecutionOrchestratorMiddleware> factory)
```

Adds a test host execution orchestrator middleware to `manager`, when `manager` supports it.

**Parameters:**

- `manager`: The test host orchestrator manager.
- `factory`: The factory method for creating the middleware.

**Exceptions:**

- `ArgumentNullException`: `manager` or `factory` is `null`.
- `NotSupportedException`: `manager` does not implement `ITestHostExecutionOrchestratorMiddlewareManager`.

#### Remarks

This method exists so middleware can be registered through the existing `ITestHostOrchestratorManager` surface without adding a required member to that interface, which would break existing implementations. It casts `manager` to the optional `ITestHostExecutionOrchestratorMiddlewareManager` capability and throws a clear, actionable exception when the concrete manager does not support middleware.

This API is experimental. It may change, break, or be removed at any time without notice.
