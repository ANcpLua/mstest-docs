# ArgumentArity struct

- Namespace: `Microsoft.Testing.Platform.Extensions.CommandLine`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents the arity (minimum and maximum number of arguments) for a command line argument.

```csharp
public readonly struct ArgumentArity : IEquatable<ArgumentArity>
```

## Remarks

This is taken from https://learn.microsoft.com/dotnet/standard/commandline/syntax#argument-arity.

## Constructors

### ArgumentArity

```csharp
public ArgumentArity(int min, int max)
```

Represents the arity (minimum and maximum number of arguments) for a command line argument.

#### Remarks

This is taken from https://learn.microsoft.com/dotnet/standard/commandline/syntax#argument-arity.

## Fields

### ExactlyOne

```csharp
public static readonly ArgumentArity ExactlyOne
```

Represents an argument arity of exactly one.

### OneOrMore

```csharp
public static readonly ArgumentArity OneOrMore
```

Represents an argument arity of one or more.

### Zero

```csharp
public static readonly ArgumentArity Zero
```

Represents an argument arity of zero.

### ZeroOrMore

```csharp
public static readonly ArgumentArity ZeroOrMore
```

Represents an argument arity of zero or more.

### ZeroOrOne

```csharp
public static readonly ArgumentArity ZeroOrOne
```

Represents an argument arity of zero or one.

## Properties

### Max

```csharp
public int Max { get; }
```

Gets the maximum number of arguments.

### Min

```csharp
public int Min { get; }
```

Gets the minimum number of arguments.

## Methods

### Equals

```csharp
public bool Equals(ArgumentArity other)
```

```csharp
public override bool Equals(object? obj)
```

### GetHashCode

```csharp
public override int GetHashCode()
```

## Operators

### Equality

```csharp
public static bool operator Equality(ArgumentArity left, ArgumentArity right)
```

Determines whether two instances of `ArgumentArity` are equal.

**Parameters:**

- `left`: The first `ArgumentArity` to compare.
- `right`: The second `ArgumentArity` to compare.

**Returns:** `true` if the instances are equal; otherwise, `false`.

### Inequality

```csharp
public static bool operator Inequality(ArgumentArity left, ArgumentArity right)
```

Determines whether two instances of `ArgumentArity` are not equal.

**Parameters:**

- `left`: The first `ArgumentArity` to compare.
- `right`: The second `ArgumentArity` to compare.

**Returns:** `true` if the instances are not equal; otherwise, `false`.
