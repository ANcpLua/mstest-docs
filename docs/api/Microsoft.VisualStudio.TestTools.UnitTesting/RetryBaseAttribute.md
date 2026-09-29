# RetryBaseAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

An abstract attribute that controls retrying a test method if it failed. It's up to the derived classes to define how the retry is done.

```csharp
[AttributeUsage(AttributeTargets.Class | AttributeTargets.Method, Inherited = false, AllowMultiple = false)]
public abstract class RetryBaseAttribute : Attribute
```

## Remarks

When applied to a test class, the attribute is used as a default for every test method declared on the class. A retry attribute placed directly on a test method takes precedence over a class-level one. The attribute is not inherited: applying it to a base test class does not apply it to derived test classes.

The runner only invokes `RetryBaseAttribute.ExecuteAsync(RetryContext)` after the initial (non-retry) run produced an unacceptable result, i.e. at least one of the produced `TestResult` entries had a `UnitTestOutcome.Failed` or `UnitTestOutcome.Timeout` outcome. It does not itself re-run the test on subsequent attempts: once `RetryBaseAttribute.ExecuteAsync(RetryContext)` is entered, the derived implementation owns the retry loop and decides when to stop. Derived types may use `IsAcceptableResultForRetry` (as `RetryAttribute` does) or implement any other policy.

## Constructors

### RetryBaseAttribute

```csharp
protected RetryBaseAttribute()
```

## Methods

### ExecuteAsync

```csharp
[Experimental("MSTESTEXP", UrlFormat = "https://aka.ms/mstest/diagnostics#{0}")]
protected internal abstract Task<RetryResult> ExecuteAsync(RetryContext retryContext)
```

Retries the test method. The details of how retry is done is left to the derived classes. Note that a first run of the method was already executed and failed before this method is called.

**Parameters:**

- `retryContext`: An object to encapsulate the state needed for retry execution.

**Returns:** Returns a `RetryResult` object that contains the results of all attempts. The last added element determines the test outcome; under Microsoft.Testing.Platform the earlier attempts are also reported, tagged as superseded, so tooling can surface the retry (attempt count, flaky detection, per-attempt error messages).

#### Remarks

This API is experimental. It may change, break, or be removed at any time without notice.
