# LinePositionSpan struct

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Line position span in a file.

```csharp
public readonly struct LinePositionSpan : IEquatable<LinePositionSpan>
```

## Constructors

### LinePositionSpan

```csharp
public LinePositionSpan(LinePosition start, LinePosition end)
```

Initializes a new instance of the `LinePositionSpan` struct.

**Parameters:**

- `start`: Start line position.
- `end`: End line position.

## Properties

### End

```csharp
public LinePosition End { get; }
```

Gets the end line position.

### Start

```csharp
public LinePosition Start { get; }
```

Gets the start line position.

## Methods

### Equals

```csharp
public bool Equals(LinePositionSpan other)
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
public static bool operator Equality(LinePositionSpan left, LinePositionSpan right)
```

Implementation of the equality operator.

### Inequality

```csharp
public static bool operator Inequality(LinePositionSpan left, LinePositionSpan right)
```

Implementation of the non-equality operator.
