# TestFileLocationProperty class

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Property that represents a file location for a test node.

```csharp
public sealed class TestFileLocationProperty : FileLocationProperty, IEquatable<TestFileLocationProperty>
```

## Constructors

### TestFileLocationProperty

```csharp
public TestFileLocationProperty(string filePath, LinePositionSpan lineSpan)
```

Initializes a new instance of the `TestFileLocationProperty` class.

**Parameters:**

- `filePath`: File path.
- `lineSpan`: Line position.

## Methods

### Equals

```csharp
public bool Equals(TestFileLocationProperty? other)
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
