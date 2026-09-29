# IGracefulStopTestExecutionResultCapability interface

- Namespace: `Microsoft.Testing.Platform.Capabilities.TestFramework`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

A graceful-stop capability that reports whether a stop request was accepted.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public interface IGracefulStopTestExecutionResultCapability : IGracefulStopTestExecutionCapability, ITestFrameworkCapability, ICapability
```

## Remarks

Test frameworks should implement this capability when a successful stop request can be a no-op because execution has already completed.

This API is experimental. It may change, break, or be removed at any time without notice.

## Methods

### TryStopTestExecutionAsync

```csharp
Task<bool> TryStopTestExecutionAsync(CancellationToken cancellationToken)
```

Attempts to stop the test execution gracefully.

**Parameters:**

- `cancellationToken`: The cancellation token.

**Returns:** A task whose result is `true` when a new stop request was accepted; otherwise, `false` when execution had already completed or a stop had already been requested.
