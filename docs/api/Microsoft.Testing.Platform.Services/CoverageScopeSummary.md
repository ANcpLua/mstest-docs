# CoverageScopeSummary class

- Namespace: `Microsoft.Testing.Platform.Services`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

All coverage metrics correlated for a single scope. This is the primary summary-layer surface for report generators: one entry per scope, with every metric that scope reported.

```csharp
public sealed class CoverageScopeSummary
```

## Constructors

### CoverageScopeSummary

```csharp
public CoverageScopeSummary(
    SessionUid sessionUid,
    CoverageScope scope,
    IReadOnlyList<CoverageMetricResult> metrics)
```

Initializes a new instance of the `CoverageScopeSummary` class.

**Parameters:**

- `sessionUid`: The session this summary belongs to.
- `scope`: The scope this summary describes.
- `metrics`: The metrics reported for the scope.

## Properties

### Item

```csharp
public CoverageMetricResult? this[CoverageMetric metric] { get; }
```

Gets a convenience lookup for a well-known metric, e.g. `summary[CoverageMetric.Line]`; null if absent. Throws for `CoverageMetric.Custom`, because every custom metric shares that enum value and is distinguished only by its name — use `CoverageScopeSummary.GetCustom(String)` instead. If a scope carries the same metric from multiple producers, this returns the first; use `CoverageScopeSummary.Metrics` to disambiguate by `CoverageMetricResult.ProducerId`.

**Parameters:**

- `metric`: The well-known metric to look up.

### Metrics

```csharp
public IReadOnlyList<CoverageMetricResult> Metrics { get; }
```

Gets the metrics reported for the scope.

### Scope

```csharp
public CoverageScope Scope { get; }
```

Gets the scope this summary describes.

### SessionUid

```csharp
public SessionUid SessionUid { get; }
```

Gets the session this summary belongs to.

## Methods

### GetCustom

```csharp
public CoverageMetricResult? GetCustom(string customMetricName)
```

Looks up a custom (proprietary) metric by its name; null if absent. If multiple producers report the same custom metric name, this returns the first in stable first-seen order; use `CoverageScopeSummary.Metrics` to disambiguate by `CoverageMetricResult.ProducerId`.

**Parameters:**

- `customMetricName`: The custom metric name.

**Returns:** The matching metric result, or null if absent.
