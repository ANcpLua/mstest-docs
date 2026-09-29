# CoverageAggregation enum

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

How per-scope values are combined for a threshold evaluation. Append-only. The population being aggregated is identified separately by `TestCoverageThresholdMessage.AggregatedOver` — e.g. `CoverageAggregation.Minimum` over `CoverageScopeLevel.Module` vs. over `CoverageScopeLevel.File` are distinct evaluations.

```csharp
public enum CoverageAggregation
```

## Fields

| Name | Value | Description |
| --- | --- | --- |
| `None` | `0` | Not an aggregate — a single scope's own value (use with an exact scope). |
| `Total` | `1` | Aggregate covered / aggregate coverable across the population. |
| `Minimum` | `2` | Worst scope in the population. |
| `Average` | `3` | Mean of per-scope percentages in the population. |
| `Maximum` | `4` | Best scope in the population. |
