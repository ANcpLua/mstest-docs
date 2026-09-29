# SessionUid struct

- Namespace: `Microsoft.Testing.Platform.TestHost`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents a unique identifier for a session.

```csharp
public readonly struct SessionUid
```

## Constructors

### SessionUid

```csharp
public SessionUid(string value)
```

Represents a unique identifier for a session.

## Properties

### Value

```csharp
public string Value { get; }
```

Gets the value of the session identifier.

## Methods

### ToString

```csharp
public override string ToString()
```

Returns a string representation of the SessionUid.

**Returns:** A string representation of the SessionUid.
