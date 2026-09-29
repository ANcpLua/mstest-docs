# ArtifactPostProcessingMode enum

- Namespace: `Microsoft.Testing.Platform.Extensions.ArtifactPostProcessing`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Specifies how the supplied artifacts relate to one another.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public enum ArtifactPostProcessingMode
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Fields

| Name | Value | Description |
| --- | --- | --- |
| `TestModules` | `0` | Artifacts were produced by distinct test modules in one test run. |
| `RetryAttempts` | `1` | Artifacts were produced by successive attempts of the same logical tests. Inputs are ordered from the initial execution to the final attempt. |
