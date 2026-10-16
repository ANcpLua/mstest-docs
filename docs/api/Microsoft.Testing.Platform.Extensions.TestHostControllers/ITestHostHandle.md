# ITestHostHandle interface

- Namespace: `Microsoft.Testing.Platform.Extensions.TestHostControllers`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents a launched test host that the platform monitors for completion.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public interface ITestHostHandle : IDisposable
```

## Remarks

The handle is intentionally agnostic of the underlying launch mechanism: it does not assume a local OS process. `ITestHostHandle.Identifier` is therefore an optional, free-form string used only for diagnostics; the platform tracks completion through `ITestHostHandle.WaitForExitAsync(CancellationToken)`, `ITestHostHandle.HasExited`, and `ITestHostHandle.ExitCode`. The platform owns the handle for the whole lifetime of the test host and disposes it (via `IDisposable`) once the host has exited, so implementations should release any OS resources they hold (process objects, sockets, container clients, …) in `IDisposable.Dispose`.

This API is experimental. It may change, break, or be removed at any time without notice.

## Properties

### ExitCode

```csharp
int ExitCode { get; }
```

Gets the exit code of the test host.

#### Remarks

Only valid once `ITestHostHandle.HasExited` is `true` (or after `ITestHostHandle.WaitForExitAsync(CancellationToken)` has completed). Reading it while the host is still running is undefined; implementations are not required to throw.

### HasExited

```csharp
bool HasExited { get; }
```

Gets a value indicating whether the test host has exited.

### Identifier

```csharp
string? Identifier { get; }
```

Gets an optional, free-form identifier for the launched test host, used only for diagnostics.

#### Remarks

The value can be anything meaningful for the launch mechanism — for example a process id, a container id, or a remote `host:pid`. Returns `null` when the launcher has nothing useful to surface. The platform never relies on this value for control flow.

## Methods

### Terminate

```csharp
void Terminate()
```

Terminates the test host. The platform calls this for best-effort teardown (for example when hang dump decides to abort the run).

### WaitForExitAsync

```csharp
Task WaitForExitAsync(CancellationToken cancellationToken)
```

Waits asynchronously for the test host to exit, or for `cancellationToken` to be canceled. The platform may await this more than once.

**Parameters:**

- `cancellationToken`: A token that cancels the wait.

**Returns:** A task that completes when the test host has exited.
