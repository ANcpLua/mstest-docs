# ProcessedArtifact class

- Namespace: `Microsoft.Testing.Platform.Extensions.ArtifactPostProcessing`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Describes an artifact produced by an `IArtifactPostProcessor`.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public sealed class ProcessedArtifact
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Constructors

### ProcessedArtifact

```csharp
public ProcessedArtifact(
    string path,
    string kind,
    string displayName,
    string? description)
```

Initializes a new instance of the `ProcessedArtifact` class.

## Properties

### Description

```csharp
public string? Description { get; }
```

Gets the artifact description.

### DisplayName

```csharp
public string DisplayName { get; }
```

Gets the artifact display name.

### Kind

```csharp
public string Kind { get; }
```

Gets the producer-asserted artifact kind.

### Path

```csharp
public string Path { get; }
```

Gets the processed artifact path.
