# SkippedTestNodeStateProperty class

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Property that represents a test node that has been skipped.

```csharp
public sealed class SkippedTestNodeStateProperty : TestNodeStateProperty, IEquatable<SkippedTestNodeStateProperty>
```

## Constructors

### SkippedTestNodeStateProperty

```csharp
public SkippedTestNodeStateProperty(string? explanation = null)
```

Initializes a new instance of the `SkippedTestNodeStateProperty` class.

**Parameters:**

- `explanation`: Textual explanation of the node.

## Properties

### CachedInstance

```csharp
public static SkippedTestNodeStateProperty CachedInstance { get; }
```

Gets the cached instance of the `SkippedTestNodeStateProperty` property.

## Methods

### Equals

```csharp
public bool Equals(SkippedTestNodeStateProperty? other)
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
