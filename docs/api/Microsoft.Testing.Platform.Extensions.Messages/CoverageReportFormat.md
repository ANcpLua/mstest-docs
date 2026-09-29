# CoverageReportFormat enum

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

The on-disk format of a coverage report artifact. Append-only.

```csharp
public enum CoverageReportFormat
```

## Fields

| Name | Value | Description |
| --- | --- | --- |
| `Unknown` | `0` | An unknown / unspecified format. |
| `Cobertura` | `1` | Cobertura XML. |
| `OpenCover` | `2` | OpenCover XML. |
| `Lcov` | `3` | lcov text. |
| `CoverageXml` | `4` | Microsoft.CodeCoverage XML. |
| `Custom` | `255` | A collector-specific format identified by `TestCoverageReportMessage.CustomFormatName`. |
