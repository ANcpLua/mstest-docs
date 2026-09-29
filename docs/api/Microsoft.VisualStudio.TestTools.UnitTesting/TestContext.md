# TestContext class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.Extensions.dll`
- Package: `MSTest.TestFramework` 4.4.1

Used to store information that is provided to unit tests.

```csharp
public abstract class TestContext
```

## Constructors

### TestContext

```csharp
protected TestContext()
```

## Properties

### CancellationToken

```csharp
public CancellationToken CancellationToken { get; }
```

Gets the cancellation token. This token is canceled when test times out. Also when explicitly canceled the test will be aborted.

### Current

```csharp
[Experimental("MSTESTEXP", UrlFormat = "https://aka.ms/mstest/diagnostics#{0}")]
public static TestContext? Current { get; }
```

Gets the current `TestContext` instance.

#### Remarks

This property returns the context for the currently executing test. When accessed outside of a test execution, it returns `null`.

This API is experimental. It may change, break, or be removed at any time without notice.

### CurrentTestOutcome

```csharp
public virtual UnitTestOutcome CurrentTestOutcome { get; }
```

Gets the current test outcome.

### DeploymentDirectory

```csharp
public virtual string? DeploymentDirectory { get; }
```

Gets the directory for files deployed for the test run (the "Out" directory). This is typically the `Out` subdirectory of `TestContext.TestRunDirectory`.

#### Remarks

When app domains are disabled, this can instead point at the test assembly directory.

### FullyQualifiedTestClassName

```csharp
public virtual string FullyQualifiedTestClassName { get; }
```

Gets the Fully-qualified name of the class containing the test method currently being executed.

### Properties

```csharp
public abstract IDictionary<string, object?> Properties { get; }
```

Gets test properties for a test.

### ResultsDirectory

```csharp
public virtual string? ResultsDirectory { get; }
```

Gets the base directory for results from the test run (the "In" directory). This is typically the `In` subdirectory of `TestContext.TestRunDirectory`.

#### Remarks

In the current implementation this returns the same path as `TestContext.TestResultsDirectory` (the `In` directory). When run directory information is unavailable, the platform services layer can fall back to the application base directory.

### TestData

```csharp
public object?[]? TestData { get; protected set; }
```

Gets or sets the test data for the test method being executed.

### TestDisplayName

```csharp
public string? TestDisplayName { get; protected set; }
```

Gets or sets the test display name for the test method being executed.

### TestException

```csharp
public Exception? TestException { get; protected set; }
```

Gets or sets the exception that occurred in the TestInitialize or TestMethod steps.

#### Remarks

The property is always `null` when accessed during the TestInitialize or TestMethod steps.

### TestName

```csharp
public virtual string TestName { get; }
```

Gets the name of the test method currently being executed.

### TestResultsDirectory

```csharp
public virtual string? TestResultsDirectory { get; }
```

Gets the directory for test result files (the "In" directory). This is the same path as `TestContext.ResultsDirectory` and is typically the parent of `TestContext.TestRunResultsDirectory`. When run directory information is unavailable, the platform services layer can return the same path for both properties.

### TestRunCount

```csharp
public int TestRunCount { get; }
```

Gets the current attempt of the test run. This property is relevant when using `RetryAttribute` (or any implementation of `RetryBaseAttribute`). On the first run, this property is set to 1. On subsequent retries, the value is incremented.

### TestRunDirectory

```csharp
public virtual string? TestRunDirectory { get; }
```

Gets the top-level directory for the test run, under which deployed files and result files are stored.

#### Remarks

This is the root of the layout used by the other deployment directory properties. A typical run produces:

```csharp
<solution>\TestResults\<run-guid>        // TestRunDirectory
    \In                                  // ResultsDirectory and TestResultsDirectory
        \<MachineName>                    // TestRunResultsDirectory
    \Out                                 // DeploymentDirectory
```

### TestRunResultsDirectory

```csharp
public virtual string? TestRunResultsDirectory { get; }
```

Gets the per-machine directory for test run result files. This is the `<MachineName>` subdirectory of `TestContext.ResultsDirectory` (i.e. `In\<MachineName>`).

#### Remarks

Despite the similar names, this directory is typically a **child** of `TestContext.TestResultsDirectory`, not the other way around. For example, with `TestContext.ResultsDirectory` set to `...\In` on a machine named `BUILD01`:

```csharp
TestResultsDirectory    => ...\In
TestRunResultsDirectory => ...\In\BUILD01
```

When run directory information is unavailable, the platform services layer can return the same path for both properties.

### TestTempDirectory

```csharp
public virtual string? TestTempDirectory { get; }
```

Gets a temporary directory unique to the currently executing test.

#### Remarks

The directory is created on first access (lazily) and is unique to the currently executing test, including each data-driven case of a `[DataRow]`/`[DynamicData]` method. Because every test (and every data case) gets its own directory, tests can write to it concurrently without any coordination — even when the assembly runs in parallel.

This is a *per-test* directory, so it returns `null` when accessed outside of a test — for example from `[AssemblyInitialize]`, `[ClassInitialize]`, `[ClassCleanup]`, or `[AssemblyCleanup]` — where there is no single owning test.

The directory is deleted automatically when the test passes and retained when the test fails, so a failed test's artifacts remain available for inspection. Retention of all directories (including passing tests) can be forced for debugging via the `MSTEST_TEST_TEMP_DIRECTORY_RETAIN` environment variable. A passing test's directory is also retained when the test registers a file inside it as a result attachment via `TestContext.AddResultFile(String)`, since the host collects that attachment after the test completes.

Unlike `TestContext.TestRunDirectory`, `TestContext.DeploymentDirectory`, `TestContext.ResultsDirectory`, `TestContext.TestRunResultsDirectory`, and `TestContext.TestResultsDirectory` — which are shared across tests for the whole run — this directory is private scratch space owned by a single test. Use it for files a test needs to write during execution; use the result directories for files that should be collected as run artifacts.

On Windows the returned path is kept short enough to reserve roughly 80 characters of headroom under the classic `MAX_PATH` (260) limit for the files the test itself writes, so ordinary relative paths created inside it will not overflow `MAX_PATH`. The feature targets the 260-character limit and does not rely on long-path opt-in (`LongPathsEnabled` / the `\\?\` prefix), which is not guaranteed to be enabled and is often not honored by external tools. If the run's results directory is too deep to preserve that headroom, or cannot be written to (for example a read-only output directory), the directory is created under the system temporary directory instead.

## Methods

### AddResultFile

```csharp
public abstract void AddResultFile(string fileName)
```

Adds a file name to the list in TestResult.ResultFileNames.

**Parameters:**

- `fileName`: The file Name.

### DisplayMessage

```csharp
public abstract void DisplayMessage(MessageLevel messageLevel, string message)
```

Used to write trace messages while the test is running.

**Parameters:**

- `messageLevel`: The message level.
- `message`: The message.

### Write

```csharp
public abstract void Write(string? message)
```

Used to write trace messages while the test is running.

**Parameters:**

- `message`: formatted message string.

```csharp
public abstract void Write(string format, params object?[] args)
```

Used to write trace messages while the test is running.

**Parameters:**

- `format`: format string.
- `args`: the arguments.

### WriteLine

```csharp
public abstract void WriteLine(string? message)
```

Used to write trace messages while the test is running.

**Parameters:**

- `message`: formatted message string.

```csharp
public abstract void WriteLine(string format, params object?[] args)
```

Used to write trace messages while the test is running.

**Parameters:**

- `format`: format string.
- `args`: the arguments.
