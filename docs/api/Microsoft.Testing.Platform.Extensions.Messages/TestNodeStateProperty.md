# TestNodeStateProperty class

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Base class for test node state properties.

```csharp
public abstract class TestNodeStateProperty : IProperty, IEquatable<TestNodeStateProperty>
```

## Constructors

### TestNodeStateProperty

```csharp
protected TestNodeStateProperty(string? explanation)
```

Initializes a new instance of the `TestNodeStateProperty` class.

**Parameters:**

- `explanation`: Textual explanation of the node state.

## Properties

### Explanation

```csharp
public string? Explanation { get; }
```

Gets the textual explanation of the node state.

## Methods

### Equals

```csharp
public bool Equals(TestNodeStateProperty? other)
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
