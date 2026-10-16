# LinePosition struct

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Line position in a file.

```csharp
public readonly struct LinePosition : IEquatable<LinePosition>
```

## Constructors

### LinePosition

```csharp
public LinePosition(int line, int column)
```

Initializes a new instance of the `LinePosition` struct.

**Parameters:**

- `line`: Line number.
- `column`: Column number.

## Properties

### Column

```csharp
public int Column { get; }
```

Gets the column number.

### Line

```csharp
public int Line { get; }
```

Gets the line number.

## Methods

### Equals

```csharp
public bool Equals(LinePosition other)
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
public static bool operator Equality(LinePosition left, LinePosition right)
```

Implementation of the equality operator.

### Inequality

```csharp
public static bool operator Inequality(LinePosition left, LinePosition right)
```

Implementation of the non-equality operator.
