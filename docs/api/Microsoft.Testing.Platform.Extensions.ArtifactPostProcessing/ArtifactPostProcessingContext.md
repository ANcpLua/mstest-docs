# ArtifactPostProcessingContext class

- Namespace: `Microsoft.Testing.Platform.Extensions.ArtifactPostProcessing`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Describes the test run that produced artifacts supplied to an `IArtifactPostProcessor`.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public sealed class ArtifactPostProcessingContext
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Constructors

### ArtifactPostProcessingContext

```csharp
public ArtifactPostProcessingContext(ArtifactPostProcessingTruncationReason truncationReason)
```

Initializes a new instance of the `ArtifactPostProcessingContext` class.

**Parameters:**

- `truncationReason`: The reason the run was truncated, or `ArtifactPostProcessingTruncationReason.None` for a complete run.

```csharp
public ArtifactPostProcessingContext(ArtifactPostProcessingTruncationReason truncationReason, ArtifactPostProcessingMode mode)
```

Initializes a new instance of the `ArtifactPostProcessingContext` class.

**Parameters:**

- `truncationReason`: The reason the run was truncated, or `ArtifactPostProcessingTruncationReason.None` for a complete run.
- `mode`: The operation that supplied the artifacts.

```csharp
public ArtifactPostProcessingContext(ArtifactPostProcessingTruncationReason truncationReason, ArtifactPostProcessingRunSummary? runSummary)
```

Initializes a new instance of the `ArtifactPostProcessingContext` class.

**Parameters:**

- `truncationReason`: The reason the run was truncated, or `ArtifactPostProcessingTruncationReason.None` for a complete run.
- `runSummary`: The authoritative orchestrator summary, or `null` when unavailable.

```csharp
public ArtifactPostProcessingContext(
    ArtifactPostProcessingTruncationReason truncationReason,
    ArtifactPostProcessingMode mode,
    ArtifactPostProcessingRunSummary? runSummary)
```

Initializes a new instance of the `ArtifactPostProcessingContext` class.

**Parameters:**

- `truncationReason`: The reason the run was truncated, or `ArtifactPostProcessingTruncationReason.None` for a complete run.
- `mode`: The operation that supplied the artifacts.
- `runSummary`: The authoritative orchestrator summary, or `null` when unavailable.

## Properties

### IsTruncated

```csharp
public bool IsTruncated { get; }
```

Gets a value indicating whether the test run was truncated.

### Mode

```csharp
public ArtifactPostProcessingMode Mode { get; }
```

Gets the operation that supplied the artifacts.

### RunSummary

```csharp
public ArtifactPostProcessingRunSummary? RunSummary { get; }
```

Gets the authoritative orchestrator summary, or `null` when the invoking orchestrator does not provide run-level totals, duration, and exit verdict.

### TruncationReason

```csharp
public ArtifactPostProcessingTruncationReason TruncationReason { get; }
```

Gets the reason the test run was truncated.
