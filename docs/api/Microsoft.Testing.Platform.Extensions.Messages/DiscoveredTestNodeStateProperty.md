# DiscoveredTestNodeStateProperty class

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Property that represents test node that has been discovered.

```csharp
public sealed class DiscoveredTestNodeStateProperty : TestNodeStateProperty, IEquatable<DiscoveredTestNodeStateProperty>
```

## Constructors

### DiscoveredTestNodeStateProperty

```csharp
public DiscoveredTestNodeStateProperty(string? explanation = null)
```

Initializes a new instance of the `DiscoveredTestNodeStateProperty` class.

**Parameters:**

- `explanation`: Textual explanation of the node.

## Properties

### CachedInstance

```csharp
public static DiscoveredTestNodeStateProperty CachedInstance { get; }
```

Gets cached instance of the `DiscoveredTestNodeStateProperty`.

## Methods

### Equals

```csharp
public bool Equals(DiscoveredTestNodeStateProperty? other)
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
