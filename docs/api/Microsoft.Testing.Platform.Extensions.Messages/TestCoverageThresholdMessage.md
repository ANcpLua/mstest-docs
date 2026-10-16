# TestCoverageThresholdMessage class

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Reports the result of a coverage threshold evaluation.

```csharp
public sealed class TestCoverageThresholdMessage : DataWithSessionUid
```

## Constructors

### TestCoverageThresholdMessage

```csharp
public TestCoverageThresholdMessage(
    SessionUid sessionUid,
    CoverageScope scope,
    CoverageMetric metric,
    CoverageAggregation aggregation,
    double actualPercentage,
    double requiredPercentage,
    bool hasCoverableData,
    string producerId,
    CoverageScopeLevel? aggregatedOver = default,
    bool treatNoDataAsFailure = true,
    string? customMetricName = null)
```

Initializes a new instance of the `TestCoverageThresholdMessage` class.

**Parameters:**

- `sessionUid`: The session this evaluation belongs to.
- `scope`: The scope the threshold applies to.
- `metric`: The metric being evaluated.
- `aggregation`: How per-scope values were combined.
- `actualPercentage`: The actual coverage, 0–100 (normalized to 0 when there is no coverable data).
- `requiredPercentage`: The required coverage threshold, 0–100.
- `hasCoverableData`: Whether the evaluated scope had any coverable data.
- `producerId`: A stable, non-empty id of the collector that produced the evaluation.
- `aggregatedOver`: The child scope level the aggregation was computed over; non-null iff `aggregation` is not `CoverageAggregation.None`.
- `treatNoDataAsFailure`: The no-data policy: whether an evaluation with no coverable data counts as failed.
- `customMetricName`: The custom metric name; required when `metric` is `CoverageMetric.Custom` and forbidden otherwise.

## Properties

### ActualPercentage

```csharp
public double ActualPercentage { get; }
```

Gets the actual coverage, 0–100; normalized to 0 when `TestCoverageThresholdMessage.HasCoverableData` is false.

### AggregatedOver

```csharp
public CoverageScopeLevel? AggregatedOver { get; }
```

Gets the child scope level that `TestCoverageThresholdMessage.Aggregation` was computed over (e.g. the minimum across `CoverageScopeLevel.Module` vs. across `CoverageScopeLevel.File`). Non-null iff `TestCoverageThresholdMessage.Aggregation` is not `CoverageAggregation.None`, so a (scope, metric, aggregation) triple is unambiguous.

### Aggregation

```csharp
public CoverageAggregation Aggregation { get; }
```

Gets how per-scope values were combined.

### CustomMetricName

```csharp
public string? CustomMetricName { get; }
```

Gets the custom metric name; set only when `TestCoverageThresholdMessage.Metric` is `CoverageMetric.Custom`.

### HasCoverableData

```csharp
public bool HasCoverableData { get; }
```

Gets a value indicating whether the evaluated scope had any coverable data. `false` when the scope had nothing coverable (an empty module, generated-only code, …). This is kept distinct from a genuine 0% so a no-data policy can be applied explicitly rather than being conflated with real 0% coverage.

### Metric

```csharp
public CoverageMetric Metric { get; }
```

Gets the metric being evaluated.

### Passed

```csharp
public bool Passed { get; }
```

Gets a value indicating whether the threshold is satisfied. With no coverable data the outcome follows `TestCoverageThresholdMessage.TreatNoDataAsFailure`; otherwise it is a plain numeric comparison.

### ProducerId

```csharp
public string ProducerId { get; }
```

Gets the id of the collector that produced this evaluation (required, correlation key).

### RequiredPercentage

```csharp
public double RequiredPercentage { get; }
```

Gets the required coverage threshold, 0–100.

### Scope

```csharp
public CoverageScope Scope { get; }
```

Gets the scope the threshold applies to (enables per-scope thresholds).

### TreatNoDataAsFailure

```csharp
public bool TreatNoDataAsFailure { get; }
```

Gets a value indicating whether an evaluation with no coverable data counts as failed (the no-data policy).
