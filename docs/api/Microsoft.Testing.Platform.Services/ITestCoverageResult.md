# ITestCoverageResult interface

- Namespace: `Microsoft.Testing.Platform.Services`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

A correlated, session-scoped view of all coverage data for consumers. The platform correlates the raw coverage messages once and exposes this read model so consumers (the terminal, HTML/UI report generators, PR-comment bots, dashboards) never re-parse artifacts or re-implement aggregation.

```csharp
public interface ITestCoverageResult
```

## Properties

### HasThresholdFailure

```csharp
bool HasThresholdFailure { get; }
```

Gets a value indicating whether any threshold failed (drives the exit code).

### Reports

```csharp
IReadOnlyList<CoverageReportReference> Reports { get; }
```

Gets pointers to rich report artifacts for deep parsing.

### Scopes

```csharp
IReadOnlyList<CoverageScopeSummary> Scopes { get; }
```

Gets the per-scope summaries with all metrics correlated per scope.

### Thresholds

```csharp
IReadOnlyList<TestCoverageThresholdMessage> Thresholds { get; }
```

Gets all threshold evaluations (passed and failed).

## Methods

### GetOverall

```csharp
CoverageScopeSummary? GetOverall(SessionUid sessionUid)
```

Gets the overall (whole-run) summary for a session, if reported.

**Parameters:**

- `sessionUid`: The session whose overall summary should be returned.

**Returns:** The session's overall summary, or null if none was reported.
