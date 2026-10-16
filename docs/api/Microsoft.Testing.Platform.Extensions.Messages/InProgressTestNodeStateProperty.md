# InProgressTestNodeStateProperty class

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Property that represents a test node that is being executed.

```csharp
public sealed class InProgressTestNodeStateProperty : TestNodeStateProperty, IEquatable<InProgressTestNodeStateProperty>
```

## Constructors

### InProgressTestNodeStateProperty

```csharp
public InProgressTestNodeStateProperty(string? explanation = null)
```

Initializes a new instance of the `InProgressTestNodeStateProperty` class.

**Parameters:**

- `explanation`: Textual explanation of the node.

## Properties

### CachedInstance

```csharp
public static InProgressTestNodeStateProperty CachedInstance { get; }
```

Gets cached instance of the `InProgressTestNodeStateProperty`.

## Methods

### Equals

```csharp
public bool Equals(InProgressTestNodeStateProperty? other)
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
