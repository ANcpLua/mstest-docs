# FileArtifactProperty class

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Property that represents multiple artifacts/attachments to associate with a test node.

```csharp
public sealed class FileArtifactProperty : IProperty, IEquatable<FileArtifactProperty>
```

## Constructors

### FileArtifactProperty

```csharp
public FileArtifactProperty(
    FileInfo fileInfo,
    string displayName,
    string? description = null)
```

Initializes a new instance of the `FileArtifactProperty` class.

**Parameters:**

- `fileInfo`: The file information.
- `displayName`: The display name.
- `description`: The description.

## Properties

### Description

```csharp
public string? Description { get; }
```

Gets the description.

### DisplayName

```csharp
public string DisplayName { get; }
```

Gets the display name.

### FileInfo

```csharp
public FileInfo FileInfo { get; }
```

Gets the file information.

## Methods

### Equals

```csharp
public bool Equals(FileArtifactProperty? other)
```

```csharp
public override bool Equals(object? obj)
```

### GetHashCode

```csharp
public override int GetHashCode()
```

### ToString

```csharp
public override string ToString()
```
