# FailedTestNodeStateProperty class

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Property that represents a test node that has been failed.

```csharp
public sealed class FailedTestNodeStateProperty : TestNodeStateProperty, IEquatable<FailedTestNodeStateProperty>
```

## Constructors

### FailedTestNodeStateProperty

```csharp
public FailedTestNodeStateProperty()
```

Initializes a new instance of the `FailedTestNodeStateProperty` class.

```csharp
public FailedTestNodeStateProperty(string explanation)
```

Initializes a new instance of the `FailedTestNodeStateProperty` class.

**Parameters:**

- `explanation`: Failure explanation.

```csharp
public FailedTestNodeStateProperty(Exception exception, string? explanation = null)
```

Initializes a new instance of the `FailedTestNodeStateProperty` class.

**Parameters:**

- `exception`: Failure exception.
- `explanation`: Failure explanation.

## Properties

### Exception

```csharp
public Exception? Exception { get; }
```

Gets the failure exception.

## Methods

### Equals

```csharp
public bool Equals(FailedTestNodeStateProperty? other)
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
