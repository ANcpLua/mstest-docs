# IArtifactPostProcessor interface

- Namespace: `Microsoft.Testing.Platform.Extensions.ArtifactPostProcessing`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Processes artifacts of one or more well-known kinds after test execution completes.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public interface IArtifactPostProcessor : IExtension
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Properties

### SupportedFileExtensionsFallback

```csharp
IReadOnlyList<string> SupportedFileExtensionsFallback { get; }
```

Gets the lowercase file extensions, including the leading dot, used to match artifacts produced by older hosts that do not provide a kind.

### SupportedKinds

```csharp
IReadOnlyList<string> SupportedKinds { get; }
```

Gets the producer-asserted artifact kinds supported by this processor.

### SupportedModes

```csharp
IReadOnlyList<ArtifactPostProcessingMode> SupportedModes { get; }
```

Gets the post-processing modes supported by this processor.

### SupportsTruncatedRuns

```csharp
bool SupportsTruncatedRuns { get; }
```

Gets a value indicating whether this processor can process artifacts observed before a run was truncated.

#### Remarks

This capability only indicates support for an incomplete set of complete artifacts. It does not indicate that the processor can consume malformed or partially written files.

## Methods

### ProcessAsync

```csharp
Task<ProcessedArtifact?> ProcessAsync(
    IReadOnlyList<InputArtifact> inputs,
    string outputDirectory,
    ArtifactPostProcessingContext context,
    CancellationToken cancellationToken)
```

Processes matching artifacts and writes at most one result under `outputDirectory`.

**Parameters:**

- `inputs`: The input artifacts. Implementations must treat them as read-only.
- `outputDirectory`: The directory under which the processed artifact must be written.
- `context`: The context describing the test run that produced the artifacts.
- `cancellationToken`: The cancellation token.

**Returns:** The processed artifact representing all `inputs`, or `null` when no processing is needed.

#### Remarks

Implementations must be deterministic and idempotent because orchestrators may retry transient failures. A non-`null` result must represent every supplied input. Implementations that cannot produce one artifact representing the complete input set must return `null` or throw. When a processor declares both kinds and legacy file extensions, `inputs` can contain the union of producer-kind matches and untagged extension-fallback matches.
