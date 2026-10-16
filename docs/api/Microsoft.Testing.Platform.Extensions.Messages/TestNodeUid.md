# TestNodeUid class

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents a test node unique identifier.

```csharp
public sealed class TestNodeUid : IEquatable<TestNodeUid>
```

## Constructors

### TestNodeUid

```csharp
public TestNodeUid(string value)
```

Represents a test node unique identifier.

**Parameters:**

- `value`: The UID.

## Properties

### Value

```csharp
public string Value { get; init; }
```

Gets the UID.

## Methods

### Equals

```csharp
public bool Equals(TestNodeUid? other)
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

## Operators

### Equality

```csharp
public static bool operator Equality(TestNodeUid left, TestNodeUid right)
```

Checks whether two `TestNodeUid` instances are equal.

**Parameters:**

- `left`: The first `TestNodeUid`.
- `right`: The second `TestNodeUid`.

**Returns:** `true` if the two instances are equal; `false` otherwise.

### Implicit

```csharp
public static implicit operator TestNodeUid(string value)
```

Implicitly converts a string to a `TestNodeUid`.

**Parameters:**

- `value`: The `TestNodeUid` value as `String`.

```csharp
public static implicit operator string(TestNodeUid testNode)
```

Implicitly converts a `TestNodeUid` to a `String`.

**Parameters:**

- `testNode`: The `TestNodeUid` value to convert.

### Inequality

```csharp
public static bool operator Inequality(TestNodeUid left, TestNodeUid right)
```

Checks whether two `TestNodeUid` instances are not equal.

**Parameters:**

- `left`: The first `TestNodeUid`.
- `right`: The second `TestNodeUid`.

**Returns:** `true` if the two instances are not equal; `false` otherwise.
