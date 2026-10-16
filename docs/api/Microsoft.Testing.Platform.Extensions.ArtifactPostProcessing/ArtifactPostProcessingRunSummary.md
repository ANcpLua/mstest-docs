# ArtifactPostProcessingRunSummary class

- Namespace: `Microsoft.Testing.Platform.Extensions.ArtifactPostProcessing`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Describes authoritative run-level values supplied by the outer test orchestrator.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public sealed class ArtifactPostProcessingRunSummary
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Constructors

### ArtifactPostProcessingRunSummary

```csharp
public ArtifactPostProcessingRunSummary(
    long totalTests,
    long passedTests,
    long failedTests,
    long skippedTests,
    TimeSpan duration,
    int exitCode,
    int testModuleCount)
```

Initializes a new instance of the `ArtifactPostProcessingRunSummary` class.

## Properties

### Duration

```csharp
public TimeSpan Duration { get; }
```

Gets the outer orchestrator wall-clock duration.

### ExitCode

```csharp
public int ExitCode { get; }
```

Gets the outer orchestrator exit code.

### FailedTests

```csharp
public long FailedTests { get; }
```

Gets the number of failed tests reported by the orchestrator.

### PassedTests

```csharp
public long PassedTests { get; }
```

Gets the number of passed tests reported by the orchestrator.

### SkippedTests

```csharp
public long SkippedTests { get; }
```

Gets the number of skipped tests reported by the orchestrator.

### TestModuleCount

```csharp
public int TestModuleCount { get; }
```

Gets the number of test modules included in the orchestrator summary.

### TotalTests

```csharp
public long TotalTests { get; }
```

Gets the total number of tests reported by the orchestrator.
