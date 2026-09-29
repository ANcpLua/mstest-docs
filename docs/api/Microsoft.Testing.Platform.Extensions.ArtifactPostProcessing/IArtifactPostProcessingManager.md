# IArtifactPostProcessingManager interface

- Namespace: `Microsoft.Testing.Platform.Extensions.ArtifactPostProcessing`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Registers artifact post-processors with a test application.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public interface IArtifactPostProcessingManager
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Methods

### AddArtifactPostProcessor

```csharp
void AddArtifactPostProcessor(Func<IServiceProvider, IArtifactPostProcessor> factory)
```

Adds an artifact post-processor factory.

**Parameters:**

- `factory`: The factory used to create the post-processor.
