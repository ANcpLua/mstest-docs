# FileArtifact class

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents a file artifact.

```csharp
public class FileArtifact : PropertyBagData
```

## Constructors

### FileArtifact

```csharp
public FileArtifact(
    FileInfo fileInfo,
    string displayName,
    string? description = null)
```

Initializes a new instance of the `FileArtifact` class.

**Parameters:**

- `fileInfo`: The file information.
- `displayName`: The display name.
- `description`: The description.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public FileArtifact(
    FileInfo fileInfo,
    string displayName,
    string? description,
    string? kind)
```

Initializes a new instance of the `FileArtifact` class with a producer-asserted artifact kind.

**Parameters:**

- `fileInfo`: The file information.
- `displayName`: The display name.
- `description`: The description.
- `kind`: An optional producer-asserted, reverse-DNS identifier of the artifact format (e.g. `microsoft.testing.trx`). Used by post-processing to group artifacts of the same kind for consolidation. `null` when the producer does not declare a kind.

#### Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Properties

### FileInfo

```csharp
public FileInfo FileInfo { get; }
```

Gets the file information.

### Kind

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public string? Kind { get; }
```

Gets the producer-asserted, reverse-DNS identifier of the artifact format (e.g. `microsoft.testing.trx`), or `null` when the producer did not declare one.

#### Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Methods

### ToString

```csharp
public override string ToString()
```
