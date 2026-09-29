# TimeoutTestNodeStateProperty class

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Property that represents an eventual timeout in the test node.

```csharp
public sealed class TimeoutTestNodeStateProperty : TestNodeStateProperty, IEquatable<TimeoutTestNodeStateProperty>
```

## Constructors

### TimeoutTestNodeStateProperty

```csharp
public TimeoutTestNodeStateProperty()
```

Initializes a new instance of the `TimeoutTestNodeStateProperty` class.

```csharp
public TimeoutTestNodeStateProperty(string explanation)
```

Initializes a new instance of the `TimeoutTestNodeStateProperty` class.

**Parameters:**

- `explanation`: Timeout explanation.

```csharp
public TimeoutTestNodeStateProperty(Exception exception, string? explanation = null)
```

Initializes a new instance of the `TimeoutTestNodeStateProperty` class.

**Parameters:**

- `exception`: Timeout exception.
- `explanation`: Timeout explanation.

## Properties

### Exception

```csharp
public Exception? Exception { get; }
```

Gets the timeout exception.

### Timeout

```csharp
public TimeSpan? Timeout { get; init; }
```

Gets the timeout TimeSpan.

## Methods

### Equals

```csharp
public bool Equals(TimeoutTestNodeStateProperty? other)
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
