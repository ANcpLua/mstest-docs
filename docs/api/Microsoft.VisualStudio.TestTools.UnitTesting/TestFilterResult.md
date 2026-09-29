# TestFilterResult struct

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

The decision returned by an `ITestFilter` for a single test.

```csharp
[Experimental("MSTESTEXP", UrlFormat = "https://aka.ms/mstest/diagnostics#{0}")]
public readonly struct TestFilterResult : IEquatable<TestFilterResult>
```

## Remarks

Designed as a `readonly` `struct` so the filter hot path stays allocation-free. Use the static `TestFilterResult.Run` / `TestFilterResult.Drop` properties (one shared value each) or the parameterized `TestFilterResult.Skip(String)` factory to create explicit results. The default value also represents `TestFilterResult.Run`.

This API is experimental. It may change, break, or be removed at any time without notice.

## Properties

### Action

```csharp
public TestFilterAction Action { get; }
```

Gets the action MSTest should apply for the test that produced this result.

### Drop

```csharp
public static TestFilterResult Drop { get; }
```

Gets the result indicating that the test should be silently dropped. Matches the semantics of the command-line `--filter` option: no test result is emitted and the test is not counted.

### Run

```csharp
public static TestFilterResult Run { get; }
```

Gets the result indicating that the test should run normally.

#### Remarks

Equivalent to `default(TestFilterResult)`; `TestFilterAction.Run` is the default enum value so a filter that forgets to assign a result still defaults to running the test.

### SkipReason

```csharp
public string? SkipReason { get; }
```

Gets the reason supplied to `TestFilterResult.Skip(String)`. Non-`null` only when `TestFilterResult.Action` is `TestFilterAction.Skip`.

## Methods

### Equals

```csharp
public bool Equals(TestFilterResult other)
```

```csharp
public override bool Equals(object? obj)
```

### GetHashCode

```csharp
public override int GetHashCode()
```

### Skip

```csharp
public static TestFilterResult Skip(string reason)
```

Creates a result indicating that the test should be reported as Skipped with the given reason.

**Parameters:**

- `reason`: A non-empty human-readable explanation surfaced in TRX / console / IDE output.

**Returns:** A `TestFilterResult` with `TestFilterResult.Action` equal to `TestFilterAction.Skip`.

**Exceptions:**

- `ArgumentNullException`: Thrown when `reason` is `null`.
- `ArgumentException`: Thrown when `reason` is empty or whitespace only.

## Operators

### Equality

```csharp
public static bool operator Equality(TestFilterResult left, TestFilterResult right)
```

Equality operator.

### Inequality

```csharp
public static bool operator Inequality(TestFilterResult left, TestFilterResult right)
```

Inequality operator.
