# ITestHostHandleExitCodePolicy interface

- Namespace: `Microsoft.Testing.Platform.Extensions.TestHostControllers`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Describes whether the operating-system exit code exposed by an `ITestHostHandle` is authoritative for the test run.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public interface ITestHostHandleExitCodePolicy
```

## Remarks

Some activation mechanisms report a process exit code that represents the application lifecycle rather than the MTP run result. Such launchers can return `false` so the controller reconciles the run from the test-host completion protocol instead.

This API is experimental. It may change, break, or be removed at any time without notice.

## Properties

### IsExitCodeAuthoritative

```csharp
bool IsExitCodeAuthoritative { get; }
```

Gets a value indicating whether `ITestHostHandle.ExitCode` is authoritative.
