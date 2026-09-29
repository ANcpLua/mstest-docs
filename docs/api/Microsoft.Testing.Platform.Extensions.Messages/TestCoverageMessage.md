# TestCoverageMessage class

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Reports a single code-coverage measurement (one metric for one scope) as counts. The percentage is derived, never stored.

```csharp
public sealed class TestCoverageMessage : DataWithSessionUid
```

## Constructors

### TestCoverageMessage

```csharp
public TestCoverageMessage(
    SessionUid sessionUid,
    CoverageScope scope,
    CoverageMetric metric,
    long coveredCount,
    long coverableCount,
    string producerId,
    string? customMetricName = null)
```

Initializes a new instance of the `TestCoverageMessage` class.

**Parameters:**

- `sessionUid`: The session this measurement belongs to.
- `scope`: The scope the measurement describes.
- `metric`: The metric being measured.
- `coveredCount`: The number of covered units.
- `coverableCount`: The number of coverable units.
- `producerId`: A stable, non-empty id of the collector that produced the measurement.
- `customMetricName`: The custom metric name; required when `metric` is `CoverageMetric.Custom` and forbidden otherwise.

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

Gets the custom metric name; set only when `TestCoverageMessage.Metric` is `CoverageMetric.Custom`.

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

Gets the id of the collector that produced this measurement (e.g. "microsoft-code-coverage"). **Required and non-empty**: it is part of the correlation key, so results from multiple collectors are never silently merged, and it ties a measurement back to its `TestCoverageReportMessage`. A collector that does not care about multi-collector scenarios should still pass a stable constant (e.g. its extension Uid).

### Scope

```csharp
public CoverageScope Scope { get; }
```

Gets the scope the measurement describes.
