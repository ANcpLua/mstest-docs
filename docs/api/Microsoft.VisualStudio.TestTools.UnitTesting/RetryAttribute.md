# RetryAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

This attribute is used to set a retry count on a test method in case of failure.

```csharp
[AttributeUsage(AttributeTargets.Class | AttributeTargets.Method, Inherited = false, AllowMultiple = false)]
public sealed class RetryAttribute : RetryBaseAttribute
```

## Remarks

When applied to a test class, the attribute is used as a default for every test method declared on the class. A `RetryAttribute` placed directly on a test method takes precedence over a class-level one (the method-level value fully replaces the class-level value, regardless of whether it is larger or smaller). The attribute is not inherited: applying it to a base test class does not apply it to derived test classes.

A retry is performed while at least one `TestResult` of the attempt has a `UnitTestOutcome.Failed` or `UnitTestOutcome.Timeout` outcome. Retrying stops as soon as an attempt produces no failed and no timed-out result. For a data-driven test (multiple results per attempt) this is an aggregate rule: an `UnitTestOutcome.Inconclusive` result (for example when the test calls `Assert.Inconclusive()`) only ends retrying when none of its sibling results in the same attempt failed or timed out; otherwise the attempt is still retried. The last attempt's results become the final outcome of the test.

This attribute retries within a single test-host run. It is independent from the `Microsoft.Testing.Extensions.Retry` `--retry-failed-tests` orchestrator, which re-invokes the whole test host. When both are enabled at the same time the attempt counts multiply (a test can run up to `(MaxRetryAttempts + 1) x (--retry-failed-tests + 1)` times), so avoid combining them unless that is intended.

## Constructors

### RetryAttribute

```csharp
public RetryAttribute(int maxRetryAttempts)
```

Initializes a new instance of the `RetryAttribute` class with the given number of max retries.

**Parameters:**

- `maxRetryAttempts`: The maximum number of retry attempts. This must be greater than or equal to 1.

## Properties

### BackoffType

```csharp
public DelayBackoffType BackoffType { get; set; }
```

Gets or sets the delay backoff type.

### MaxRetryAttempts

```csharp
public int MaxRetryAttempts { get; }
```

Gets the number of retries that the test should make in case of failures. Note that before RetryAttribute is considered, the test was already executed once. This property determines the max number of retries after the first normal run.

### MillisecondsDelayBetweenRetries

```csharp
public int MillisecondsDelayBetweenRetries { get; set; }
```

Gets or sets the delay, in milliseconds, between retries. This delay is also applied after the first run and before the first retry attempt.

## Methods

### ExecuteAsync

```csharp
protected internal override Task<RetryResult> ExecuteAsync(RetryContext retryContext)
```

Retries the test method `RetryAttribute.MaxRetryAttempts` times in case of failure. Note that a first run of the method was already executed and failed before this method is called.

**Parameters:**

- `retryContext`: An object to encapsulate the state needed for retry execution.

**Returns:** Returns a `RetryResult` object that contains the results of all attempts. The last added element determines the test outcome; under Microsoft.Testing.Platform the earlier attempts are also reported, tagged as superseded, so tooling can surface the retry.
