# IArtifactPostProcessingApplicationBuilder interface

- Namespace: `Microsoft.Testing.Platform.Builder`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents a test application builder that supports registering artifact post-processors and tools.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public interface IArtifactPostProcessingApplicationBuilder : ITestApplicationBuilder
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Properties

### ArtifactPostProcessing

```csharp
IArtifactPostProcessingManager ArtifactPostProcessing { get; }
```

Gets the artifact post-processing manager.

### Tools

```csharp
IToolsManager Tools { get; }
```

Gets the tools manager.
