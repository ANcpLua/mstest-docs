# ILocalTestHostHandle interface

- Namespace: `Microsoft.Testing.Platform.Extensions.TestHostControllers`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents a test host handle backed by a local operating-system process.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public interface ILocalTestHostHandle : ITestHostHandle, IDisposable
```

## Remarks

The platform uses `ILocalTestHostHandle.ProcessId` to verify that the process connecting to the controller is the process created by the launcher before privileged lifetime extensions inspect or terminate it.

This API is experimental. It may change, break, or be removed at any time without notice.

## Properties

### ProcessId

```csharp
int ProcessId { get; }
```

Gets the operating-system process identifier of the launched test host.
