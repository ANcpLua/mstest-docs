# ITestHostExecutionOrchestratorMiddlewareManager interface

- Namespace: `Microsoft.Testing.Platform.TestHostOrchestrator`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Optional capability of an `ITestHostOrchestratorManager` that also supports registering single-invocation `ITestHostExecutionOrchestratorMiddleware` instances.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public interface ITestHostExecutionOrchestratorMiddlewareManager
```

## Remarks

This is a separate, optional interface rather than a new required member on `ITestHostOrchestratorManager`, so existing implementations of `ITestHostOrchestratorManager` keep compiling and running unchanged. Prefer `TestHostOrchestratorManagerExtensions.AddTestHostExecutionOrchestratorMiddleware(ITestHostOrchestratorManager,Func<IServiceProvider,ITestHostExecutionOrchestratorMiddleware>)` to add middleware through an `ITestHostOrchestratorManager` reference without depending on this interface directly.

This API is experimental. It may change, break, or be removed at any time without notice.

## Methods

### AddTestHostExecutionOrchestratorMiddleware

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
void AddTestHostExecutionOrchestratorMiddleware(Func<IServiceProvider, ITestHostExecutionOrchestratorMiddleware> factory)
```

Adds a test host execution orchestrator middleware.

**Parameters:**

- `factory`: The factory method for creating the middleware.

#### Remarks

Middleware is composed outermost-first in registration order: the first middleware registered is the outermost layer and is the last to observe the pipeline's overall result (after every inner layer, including the wrapped orchestrator, has run); the last middleware registered is the innermost layer, closest to the wrapped orchestrator. This ordering is explicit and positional — there is no numeric ordering key, and middleware must not assume its effect on the pipeline is commutative with other middleware.

This API is experimental. It may change, break, or be removed at any time without notice.
