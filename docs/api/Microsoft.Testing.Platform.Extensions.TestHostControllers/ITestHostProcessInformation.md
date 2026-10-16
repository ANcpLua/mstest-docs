# ITestHostProcessInformation interface

- Namespace: `Microsoft.Testing.Platform.Extensions.TestHostControllers`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents information about a test host process.

```csharp
public interface ITestHostProcessInformation
```

## Properties

### ExitCode

```csharp
int ExitCode { get; }
```

Gets the exit code of the test host process.

### HasExitedGracefully

```csharp
bool HasExitedGracefully { get; }
```

Gets a value indicating whether the test host app has exited gracefully.

#### Remarks

This flag is based on a message that the TestApplication sends at its end. The test host process might still crash or be killed after sending this message, in which case this flag will be true but the process hasn't truly exited gracefully.

### PID

```csharp
int PID { get; }
```

Gets the process ID of the test host.
