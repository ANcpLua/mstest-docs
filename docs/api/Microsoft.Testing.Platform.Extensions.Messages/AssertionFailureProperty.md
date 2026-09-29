# AssertionFailureProperty class

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Property that carries the structured `expected` and `actual` values of a failed assertion, so consumers can render an expected-vs-actual diff instead of only a flat failure message.

```csharp
public sealed class AssertionFailureProperty : IProperty, IEquatable<AssertionFailureProperty>
```

## Remarks

Historically this information could only travel on `Exception.Data` under the `assert.expected` / `assert.actual` keys. That channel requires the test framework to hand the platform the very exception instance the assertion library threw, which is not always possible: a framework may report a failure without any exception at all (see the `FailedTestNodeStateProperty.ctor(String)` overload), or it may only have the message and stack trace as strings once the failure has crossed a process or AppDomain boundary.

Consumers should prefer this property and fall back to the `Exception.Data` keys for producers that have not been updated yet.

## Constructors

### AssertionFailureProperty

```csharp
public AssertionFailureProperty(string? expected, string? actual)
```

Initializes a new instance of the `AssertionFailureProperty` class.

**Parameters:**

- `expected`: The pre-formatted text representation of the expected value, or `null` when the assertion has no natural expected value.
- `actual`: The pre-formatted text representation of the actual value, or `null` when the assertion has no natural actual value.

**Exceptions:**

- `ArgumentException`: Both `expected` and `actual` are `null`, which would make the property carry no information. Rejecting that state is what lets consumers treat the mere presence of this property as authoritative and stop consulting the legacy `Exception.Data` keys.

## Properties

### Actual

```csharp
public string? Actual { get; }
```

Gets the pre-formatted text representation of the actual value, or `null` when the assertion has no natural actual value.

### Expected

```csharp
public string? Expected { get; }
```

Gets the pre-formatted text representation of the expected value, or `null` when the assertion has no natural expected value.

## Methods

### Equals

```csharp
public bool Equals(AssertionFailureProperty? other)
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
