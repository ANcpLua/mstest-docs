# FileLocationProperty class

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Base property that represents a file location.

```csharp
public abstract class FileLocationProperty : IProperty, IEquatable<FileLocationProperty>
```

## Constructors

### FileLocationProperty

```csharp
protected FileLocationProperty(string filePath, LinePositionSpan lineSpan)
```

Initializes a new instance of the `FileLocationProperty` class.

**Parameters:**

- `filePath`: File path.
- `lineSpan`: Line position.

## Properties

### FilePath

```csharp
public string FilePath { get; }
```

Gets the file path.

### LineSpan

```csharp
public LinePositionSpan LineSpan { get; }
```

Gets the line position span.

## Methods

### Equals

```csharp
public bool Equals(FileLocationProperty? other)
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
