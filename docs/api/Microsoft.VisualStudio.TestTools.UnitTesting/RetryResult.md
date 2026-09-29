# RetryResult class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

The result of a test retry.

```csharp
[Experimental("MSTESTEXP", UrlFormat = "https://aka.ms/mstest/diagnostics#{0}")]
public sealed class RetryResult
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Constructors

### RetryResult

```csharp
public RetryResult()
```

## Properties

### AllResults

```csharp
public IReadOnlyList<TestResult[]> AllResults { get; }
```

Gets the test results of all retry attempts, in the order they were added. Each element corresponds to a single attempt and holds the test results produced by that attempt.

#### Remarks

All attempts are reported to Microsoft.Testing.Platform: the last one as the test's outcome, the earlier ones tagged as superseded so tooling can surface the retry (see the platform's `RetryAttemptProperty`).

## Methods

### AddResult

```csharp
public void AddResult(TestResult[] testResults)
```

Adds a set of test results to the retry result.

**Parameters:**

- `testResults`: The test results for the current attempt.
