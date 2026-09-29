# TestCoverageReportMessage class

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

References a coverage report artifact so deep consumers (HTML/UI generators) can parse full-fidelity per-line data that the summary intentionally does not carry.

```csharp
public sealed class TestCoverageReportMessage : DataWithSessionUid
```

## Constructors

### TestCoverageReportMessage

```csharp
public TestCoverageReportMessage(
    SessionUid sessionUid,
    string reportPath,
    CoverageReportFormat format,
    string producerId,
    string? customFormatName = null)
```

Initializes a new instance of the `TestCoverageReportMessage` class.

**Parameters:**

- `sessionUid`: The session this report belongs to.
- `reportPath`: The path to the report artifact.
- `format`: The on-disk format of the report.
- `producerId`: A stable, non-empty id of the collector that produced the report.
- `customFormatName`: The custom format name; required when `format` is `CoverageReportFormat.Custom` and forbidden otherwise.

## Properties

### CustomFormatName

```csharp
public string? CustomFormatName { get; }
```

Gets the custom format name; set if and only if `TestCoverageReportMessage.Format` is `CoverageReportFormat.Custom`.

### Format

```csharp
public CoverageReportFormat Format { get; }
```

Gets the on-disk format of the report.

### ProducerId

```csharp
public string ProducerId { get; }
```

Gets the id of the collector that produced the report (required, correlation key).

### ReportPath

```csharp
public string ReportPath { get; }
```

Gets the path to the report artifact.
