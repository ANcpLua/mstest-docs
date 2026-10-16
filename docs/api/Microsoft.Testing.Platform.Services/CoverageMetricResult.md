# CoverageMetricResult class

- Namespace: `Microsoft.Testing.Platform.Services`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

A single correlated coverage measurement (one metric for one scope) exposed through `ITestCoverageResult`. Carries counts; percentage is derived.

```csharp
public sealed class CoverageMetricResult
```

## Constructors

### CoverageMetricResult

```csharp
public CoverageMetricResult(
    CoverageMetric metric,
    long coveredCount,
    long coverableCount,
    string producerId,
    string? customMetricName = null)
```

Initializes a new instance of the `CoverageMetricResult` class.

**Parameters:**

- `metric`: The metric being measured.
- `coveredCount`: The number of covered units.
- `coverableCount`: The number of coverable units.
- `producerId`: The collector that produced this measurement; part of the correlation key.
- `customMetricName`: The custom metric name; set only when `metric` is `CoverageMetric.Custom`.

## Properties

### CoverableCount

```csharp
public long CoverableCount { get; }
```

Gets the number of coverable units.

### CoveredCount

```csharp
public long CoveredCount { get; }
```

Gets the number of covered units.

### CustomMetricName

```csharp
public string? CustomMetricName { get; }
```

Gets the custom metric name; set only when `CoverageMetricResult.Metric` is `CoverageMetric.Custom`.

### HasCoverableData

```csharp
public bool HasCoverableData { get; }
```

Gets a value indicating whether there is any coverable data.

### Metric

```csharp
public CoverageMetric Metric { get; }
```

Gets the metric being measured.

### Percentage

```csharp
public double Percentage { get; }
```

Gets the coverage as a percentage in the range 0–100; 0 when nothing is coverable.

### ProducerId

```csharp
public string ProducerId { get; }
```

Gets the collector that produced this measurement; part of the correlation key.
