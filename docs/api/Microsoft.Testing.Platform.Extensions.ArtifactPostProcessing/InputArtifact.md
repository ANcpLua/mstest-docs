# InputArtifact class

- Namespace: `Microsoft.Testing.Platform.Extensions.ArtifactPostProcessing`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Describes an artifact supplied to an `IArtifactPostProcessor`.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public sealed class InputArtifact
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Constructors

### InputArtifact

```csharp
public InputArtifact(
    string path,
    string? kind,
    string? producingTestModule,
    string? targetFramework,
    string? architecture,
    string? executionId)
```

Initializes a new instance of the `InputArtifact` class.

## Properties

### Architecture

```csharp
public string? Architecture { get; }
```

Gets the process architecture of the producing test module.

### ExecutionId

```csharp
public string? ExecutionId { get; }
```

Gets the execution identifier associated with the artifact.

### Kind

```csharp
public string? Kind { get; }
```

Gets the producer-asserted artifact kind, or `null` when unavailable.

### Path

```csharp
public string Path { get; }
```

Gets the artifact path.

### ProducingTestModule

```csharp
public string? ProducingTestModule { get; }
```

Gets the path of the test module that produced the artifact.

### TargetFramework

```csharp
public string? TargetFramework { get; }
```

Gets the target framework of the producing test module.
