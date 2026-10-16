# ITestHostOrchestratorApplicationLifetime interface

- Namespace: `Microsoft.Testing.Platform.Extensions.TestHostOrchestrator`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents the application lifetime for a test host orchestrator.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public interface ITestHostOrchestratorApplicationLifetime : ITestHostOrchestratorExtension, IExtension
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Methods

### AfterRunAsync

```csharp
Task AfterRunAsync(int exitCode, CancellationToken cancellationToken)
```

Executes after the orchestrator runs.

**Parameters:**

- `exitCode`: The exit code of the orchestrator.
- `cancellationToken`: The cancellation token.

**Returns:** A task representing the asynchronous operation.

#### Remarks

Also invoked when the orchestration was canceled or failed, so that whatever `ITestHostOrchestratorApplicationLifetime.BeforeRunAsync(CancellationToken)` acquired can still be released. Implementations must therefore tolerate being called when their `ITestHostOrchestratorApplicationLifetime.BeforeRunAsync(CancellationToken)` never ran or did not complete, must be safe to call once per run regardless of outcome, and should not assume `cancellationToken` is still usable — it may already be canceled. Implementations should not throw from this method. When the orchestration was canceled or failed, exceptions thrown from this method are logged and suppressed so they cannot mask the original outcome.

### BeforeRunAsync

```csharp
Task BeforeRunAsync(CancellationToken cancellationToken)
```

Executes before the orchestrator runs.

**Parameters:**

- `cancellationToken`: The cancellation token.

**Returns:** A task representing the asynchronous operation.
