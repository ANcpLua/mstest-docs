# StandardErrorProperty class

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Property that represents standard error to associate with a test node.

```csharp
public sealed class StandardErrorProperty : IProperty, IEquatable<StandardErrorProperty>
```

## Constructors

### StandardErrorProperty

```csharp
public StandardErrorProperty(string standardError)
```

Initializes a new instance of the `StandardErrorProperty` class.

**Parameters:**

- `standardError`: The standard error.

## Properties

### StandardError

```csharp
public string StandardError { get; }
```

Gets the standard error.

## Methods

### Equals

```csharp
public bool Equals(StandardErrorProperty? other)
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
