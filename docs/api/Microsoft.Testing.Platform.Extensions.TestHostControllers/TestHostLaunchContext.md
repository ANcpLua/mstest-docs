# TestHostLaunchContext class

- Namespace: `Microsoft.Testing.Platform.Extensions.TestHostControllers`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Carries the fully prepared information the platform would have used to start the test host, passed to an `ITestHostLauncher`.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public sealed class TestHostLaunchContext
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Constructors

### TestHostLaunchContext

```csharp
public TestHostLaunchContext(
    string fileName,
    IReadOnlyList<string> arguments,
    IReadOnlyDictionary<string, string?> environmentVariables,
    string? workingDirectory)
```

Initializes a new instance of the `TestHostLaunchContext` class.

**Parameters:**

- `fileName`: The test host executable path the platform would have started.
- `arguments`: The fully prepared arguments for the active launch mode.
- `environmentVariables`: The final environment for the test host, including any controller or orchestrator connection metadata the host must consume.
- `workingDirectory`: The working directory, or `null` to inherit the current one.

## Properties

### Arguments

```csharp
public IReadOnlyList<string> Arguments { get; }
```

Gets the fully prepared arguments for the active launch mode.

### EnvironmentVariables

```csharp
public IReadOnlyDictionary<string, string?> EnvironmentVariables { get; }
```

Gets the final environment for the test host, including any controller or orchestrator connection metadata required by the active launch mode.

### FileName

```csharp
public string FileName { get; }
```

Gets the test host executable path the platform would have started.

### WorkingDirectory

```csharp
public string? WorkingDirectory { get; }
```

Gets the working directory, or `null` to inherit the current one.
