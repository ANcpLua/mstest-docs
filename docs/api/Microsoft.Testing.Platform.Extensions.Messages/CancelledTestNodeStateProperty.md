# CancelledTestNodeStateProperty class

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Property that represents an eventual cancellation of a test node.

```csharp
[Obsolete("CancelledTestNodeStateProperty is obsolete. Test frameworks should throw OperationCanceledException using the cancellation token passed by Microsoft.Testing.Platform instead of using this state.", DiagnosticId = "MTP0001", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public sealed class CancelledTestNodeStateProperty : TestNodeStateProperty, IEquatable<CancelledTestNodeStateProperty>
```

## Constructors

### CancelledTestNodeStateProperty

```csharp
public CancelledTestNodeStateProperty()
```

Initializes a new instance of the `CancelledTestNodeStateProperty` class.

```csharp
public CancelledTestNodeStateProperty(string explanation)
```

Initializes a new instance of the `CancelledTestNodeStateProperty` class.

**Parameters:**

- `explanation`: Cancellation explanation.

```csharp
public CancelledTestNodeStateProperty(Exception exception, string? explanation = null)
```

Initializes a new instance of the `CancelledTestNodeStateProperty` class.

**Parameters:**

- `exception`: Cancellation exception.
- `explanation`: Cancellation explanation.

## Properties

### Exception

```csharp
public Exception? Exception { get; }
```

Gets the cancellation exception.

## Methods

### Equals

```csharp
public bool Equals(CancelledTestNodeStateProperty? other)
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
