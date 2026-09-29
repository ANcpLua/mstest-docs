# StandardOutputProperty class

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Property that represents standard output to associate with a test node.

```csharp
public sealed class StandardOutputProperty : IProperty, IEquatable<StandardOutputProperty>
```

## Constructors

### StandardOutputProperty

```csharp
public StandardOutputProperty(string standardOutput)
```

Initializes a new instance of the `StandardOutputProperty` class.

**Parameters:**

- `standardOutput`: The standard output.

## Properties

### StandardOutput

```csharp
public string StandardOutput { get; }
```

Gets the standard output.

## Methods

### Equals

```csharp
public bool Equals(StandardOutputProperty? other)
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
