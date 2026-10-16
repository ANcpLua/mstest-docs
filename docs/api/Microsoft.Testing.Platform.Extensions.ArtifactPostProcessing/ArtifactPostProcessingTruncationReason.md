# ArtifactPostProcessingTruncationReason enum

- Namespace: `Microsoft.Testing.Platform.Extensions.ArtifactPostProcessing`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Specifies why a test run was truncated before every scheduled test module completed.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public enum ArtifactPostProcessingTruncationReason
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Fields

| Name | Value | Description |
| --- | --- | --- |
| `None` | `0` | The test run completed without policy-driven truncation. |
| `MaximumFailedTests` | `1` | The test run reached the configured maximum number of failed tests. |
| `Timeout` | `2` | The test run reached its configured timeout. |
