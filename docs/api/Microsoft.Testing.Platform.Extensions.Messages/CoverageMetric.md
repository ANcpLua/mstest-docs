# CoverageMetric enum

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Identifies a code-coverage metric. This is a closed but append-only set: consumers MUST treat unrecognized values non-exhaustively (always handle a default case). New well-known members may be added in future versions without being a breaking change.

```csharp
public enum CoverageMetric
```

## Fields

| Name | Value | Description |
| --- | --- | --- |
| `Line` | `0` | Line coverage. |
| `Statement` | `1` | Statement coverage. |
| `Branch` | `2` | Branch coverage. |
| `Method` | `3` | Method coverage. |
| `Function` | `4` | Function coverage. |
| `Block` | `5` | Block coverage (Microsoft.CodeCoverage / dotnet-coverage primary metric). |
| `Instruction` | `6` | Instruction coverage (JaCoCo). |
| `Region` | `7` | Region coverage (llvm-cov). |
| `Class` | `8` | Class coverage (JaCoCo / PHPUnit entity counter). |
| `Condition` | `9` | Condition coverage. |
| `Complexity` | `10` | Cyclomatic complexity (JaCoCo, count-based rather than a percentage). |
| `Custom` | `255` | A collector-specific metric not covered by the well-known members. When set, `TestCoverageMessage.CustomMetricName` carries the metric identifier. This is the single escape hatch for proprietary / safety-critical metrics (e.g. MC/DC). |
