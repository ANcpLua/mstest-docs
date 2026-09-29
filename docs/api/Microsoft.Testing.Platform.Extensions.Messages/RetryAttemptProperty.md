# RetryAttemptProperty class

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Property that identifies a test node update as one attempt of an in-process retry sequence, i.e. several executions of the same test that a test framework performed within a single test host run and reported under the same `TestNode.Uid`.

```csharp
public sealed class RetryAttemptProperty : IProperty, IEquatable<RetryAttemptProperty>
```

## Remarks

A test framework that retries a test in-process (for example MSTest's `[Retry]` attribute) publishes one `TestNodeUpdateMessage` per attempt, each carrying this property. Consumers that want a single row per test - TRX, JUnit, the process exit code - ignore updates whose `RetryAttemptProperty.IsSuperseded` is `true`. Consumers that want the whole history - CTRF's `retryAttempts[]` / `flaky`, the HTML report, the terminal's retried/flaky counters - keep them all.

This is independent from the out-of-process `--retry-failed-tests` orchestrator, which re-invokes the whole test host and attributes attempts per host instance instead. When both are in play the two notions compose: the host attempt is the major number and `RetryAttemptProperty.AttemptNumber` the minor one.

## Constructors

### RetryAttemptProperty

```csharp
public RetryAttemptProperty(int attemptNumber, bool isSuperseded)
```

Initializes a new instance of the `RetryAttemptProperty` class.

**Parameters:**

- `attemptNumber`: The 1-based attempt number within the current test host run.
- `isSuperseded`: `true` when a later attempt for the same test node follows this one, so this result is not the test's final outcome.

**Exceptions:**

- `ArgumentOutOfRangeException`: `attemptNumber` is less than 1.

## Properties

### AttemptNumber

```csharp
public int AttemptNumber { get; }
```

Gets the 1-based attempt number within the current test host run. The first (non-retry) execution is 1.

### IsSuperseded

```csharp
public bool IsSuperseded { get; }
```

Gets a value indicating whether a later attempt for the same test node follows this one.

## Methods

### Equals

```csharp
public bool Equals(RetryAttemptProperty? other)
```

```csharp
public override bool Equals(object? obj)
```

### GetHashCode

```csharp
public override int GetHashCode()
```

### ToString

```csharp
public override string ToString()
```
