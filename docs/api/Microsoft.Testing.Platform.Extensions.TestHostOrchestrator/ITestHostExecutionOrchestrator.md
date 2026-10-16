# ITestHostExecutionOrchestrator interface

- Namespace: `Microsoft.Testing.Platform.Extensions.TestHostOrchestrator`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents an extension that orchestrates test host execution.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public interface ITestHostExecutionOrchestrator : ITestHostOrchestratorExtension, IExtension
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Methods

### OrchestrateTestHostExecutionAsync

```csharp
Task<int> OrchestrateTestHostExecutionAsync(CancellationToken cancellationToken)
```

Orchestrates test host execution.

**Parameters:**

- `cancellationToken`: The cancellation token.

**Returns:** A task representing the asynchronous operation that returns the test host exit code.
