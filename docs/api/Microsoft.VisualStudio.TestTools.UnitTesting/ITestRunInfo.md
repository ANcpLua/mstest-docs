# ITestRunInfo interface

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.Extensions.dll`
- Package: `MSTest.TestFramework` 4.4.1

Read-only ambient information about the current test run. Accessed via `TestRun.Current`.

```csharp
[Experimental("MSTESTEXP", UrlFormat = "https://aka.ms/mstest/diagnostics#{0}")]
public interface ITestRunInfo
```

## Remarks

Unlike `TestContext`, which describes the test currently executing, an `ITestRunInfo` describes the run as a whole and is queryable from any code reachable during a test run (for example helpers, fixtures, or `[AssemblyInitialize]` methods).

This API is experimental. It may change, break, or be removed at any time without notice.

## Properties

### PlannedTests

```csharp
IReadOnlyCollection<PlannedTest> PlannedTests { get; }
```

Gets the tests that have been discovered and have passed the active filter for the currently-executing assembly. The collection is empty until the platform begins executing tests for an assembly.

#### Remarks

Data-driven tests whose rows are unfolded only at execution time may appear here as a single entry rather than one entry per row.
