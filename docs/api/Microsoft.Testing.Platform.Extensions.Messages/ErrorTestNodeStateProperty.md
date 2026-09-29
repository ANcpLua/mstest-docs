# ErrorTestNodeStateProperty class

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Property that represents an eventual error in the test node.

```csharp
public sealed class ErrorTestNodeStateProperty : TestNodeStateProperty, IEquatable<ErrorTestNodeStateProperty>
```

## Constructors

### ErrorTestNodeStateProperty

```csharp
public ErrorTestNodeStateProperty()
```

Initializes a new instance of the `ErrorTestNodeStateProperty` class.

```csharp
public ErrorTestNodeStateProperty(string explanation)
```

Initializes a new instance of the `ErrorTestNodeStateProperty` class.

**Parameters:**

- `explanation`: Error explanation.

```csharp
public ErrorTestNodeStateProperty(Exception exception, string? explanation = null)
```

Initializes a new instance of the `ErrorTestNodeStateProperty` class.

**Parameters:**

- `exception`: Error exception.
- `explanation`: Error explanation.

## Properties

### Exception

```csharp
public Exception? Exception { get; }
```

Gets the error exception.

## Methods

### Equals

```csharp
public bool Equals(ErrorTestNodeStateProperty? other)
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
