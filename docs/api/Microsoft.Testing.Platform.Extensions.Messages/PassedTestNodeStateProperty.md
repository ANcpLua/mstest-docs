# PassedTestNodeStateProperty class

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Property that represents a test node that has been executed and passed.

```csharp
public sealed class PassedTestNodeStateProperty : TestNodeStateProperty, IEquatable<PassedTestNodeStateProperty>
```

## Constructors

### PassedTestNodeStateProperty

```csharp
public PassedTestNodeStateProperty(string? explanation = null)
```

Initializes a new instance of the `PassedTestNodeStateProperty` class.

**Parameters:**

- `explanation`: Textual explanation of the node.

## Properties

### CachedInstance

```csharp
public static PassedTestNodeStateProperty CachedInstance { get; }
```

Gets the cached instance of the `PassedTestNodeStateProperty` property.

## Methods

### Equals

```csharp
public bool Equals(PassedTestNodeStateProperty? other)
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
