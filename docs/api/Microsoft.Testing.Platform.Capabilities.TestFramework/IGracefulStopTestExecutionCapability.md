# IGracefulStopTestExecutionCapability interface

- Namespace: `Microsoft.Testing.Platform.Capabilities.TestFramework`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

A capability to support stopping test execution gracefully, without cancelling/aborting everything. This is used to support '--maximum-failed-tests'.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public interface IGracefulStopTestExecutionCapability : ITestFrameworkCapability, ICapability
```

## Remarks

Test frameworks can choose to run any needed cleanup when cancellation is requested.

This API is experimental. It may change, break, or be removed at any time without notice.

## Methods

### StopTestExecutionAsync

```csharp
Task StopTestExecutionAsync(CancellationToken cancellationToken)
```

Stops the test execution gracefully.

**Parameters:**

- `cancellationToken`: The cancellation token.

**Returns:** A task representing the asynchronous operation.
