# CoverageReportReference class

- Namespace: `Microsoft.Testing.Platform.Services`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

A pointer to a rich coverage report artifact, correlated through `ITestCoverageResult`. Deep consumers (HTML/UI generators) parse the referenced artifact for the per-line data the summary intentionally does not carry.

```csharp
public sealed class CoverageReportReference
```

## Constructors

### CoverageReportReference

```csharp
public CoverageReportReference(
    SessionUid sessionUid,
    string path,
    CoverageReportFormat format,
    string producerId,
    string? customFormatName = null)
```

Initializes a new instance of the `CoverageReportReference` class.

**Parameters:**

- `sessionUid`: The session this report belongs to.
- `path`: The path to the report artifact.
- `format`: The on-disk format of the report.
- `producerId`: The collector that produced the report; part of the correlation key.
- `customFormatName`: The custom format name; set only when `format` is `CoverageReportFormat.Custom`.

## Properties

### CustomFormatName

```csharp
public string? CustomFormatName { get; }
```

Gets the custom format name; set only when `CoverageReportReference.Format` is `CoverageReportFormat.Custom`.

### Format

```csharp
public CoverageReportFormat Format { get; }
```

Gets the on-disk format of the report.

### Path

```csharp
public string Path { get; }
```

Gets the path to the report artifact.

### ProducerId

```csharp
public string ProducerId { get; }
```

Gets the collector that produced the report; part of the correlation key.

### SessionUid

```csharp
public SessionUid SessionUid { get; }
```

Gets the session this report belongs to.
