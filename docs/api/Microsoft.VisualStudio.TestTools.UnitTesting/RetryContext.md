# RetryContext struct

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

Represents the context for a test retry.

```csharp
[Experimental("MSTESTEXP", UrlFormat = "https://aka.ms/mstest/diagnostics#{0}")]
public readonly struct RetryContext
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Properties

### ExecuteTaskGetter

```csharp
public Func<Task<TestResult[]>> ExecuteTaskGetter { get; }
```

Gets the function that will execute the test asynchronously.

### FirstRunResults

```csharp
public TestResult[] FirstRunResults { get; }
```

Gets the test results of the initial run that failed.
