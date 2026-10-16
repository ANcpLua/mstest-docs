# ITestHostLauncher interface

- Namespace: `Microsoft.Testing.Platform.Extensions.TestHostControllers`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Allows an extension to control how the out-of-process test host is launched, replacing the platform's default `Process.Start` behavior.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public interface ITestHostLauncher : ITestHostControllersExtension, IExtension
```

## Remarks

The platform keeps owning argument and environment preparation, connection handshakes, lifecycle callbacks, and exit-code reconciliation, and delegates only the single "create and start the test host" step. A controller launch carries the controller IPC/PID handshake; an orchestrator launch can instead carry extension-specific connection metadata such as Retry. Launchers must forward the supplied context opaquely rather than require one specific handshake. The launcher does not have to start a local OS process as long as it returns an `ITestHostHandle` the platform can monitor.

This API is experimental. It may change, break, or be removed at any time without notice.

## Methods

### LaunchTestHostAsync

```csharp
Task<ITestHostHandle> LaunchTestHostAsync(TestHostLaunchContext context, CancellationToken cancellationToken)
```

Creates and starts the test host. The platform has already prepared the file name, arguments, and environment variables carried by `context` for the active controller or orchestrator mode. The implementation must return a handle the platform can monitor for completion.

**Parameters:**

- `context`: The fully prepared launch information.
- `cancellationToken`: The cancellation token.

**Returns:** A handle the platform monitors for the lifetime of the test host.
