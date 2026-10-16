# IArtifactPostProcessorRequiresPostProcessing interface

- Namespace: `Microsoft.Testing.Platform.Extensions.ArtifactPostProcessing`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Marks an artifact post-processor whose inputs are internal coordination artifacts that must always be post-processed, including when only one matching input exists.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public interface IArtifactPostProcessorRequiresPostProcessing : IArtifactPostProcessor, IExtension
```

## Remarks

Orchestrators that support this capability advertise that support in the handshake response before a test session starts. Producers must preserve their standalone behavior when the capability is unavailable.

This API is experimental. It may change, break, or be removed at any time without notice.
