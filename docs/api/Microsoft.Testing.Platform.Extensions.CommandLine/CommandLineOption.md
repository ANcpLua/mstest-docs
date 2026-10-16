# CommandLineOption class

- Namespace: `Microsoft.Testing.Platform.Extensions.CommandLine`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents a command line option.

```csharp
public sealed class CommandLineOption : IEquatable<CommandLineOption>
```

## Constructors

### CommandLineOption

```csharp
public CommandLineOption(
    string name,
    string description,
    ArgumentArity arity,
    bool isHidden)
```

Initializes a new instance of the `CommandLineOption` class.

**Parameters:**

- `name`: The name of the command line option.
- `description`: The description of the command line option.
- `arity`: The arity of the command line option.
- `isHidden`: Indicates whether the command line option is hidden.

#### Remarks

This ctor is public and used by non built-in extension, we need to know if the extension is built-in or not to correctly handle the --internal- prefix.

## Properties

### Arity

```csharp
public ArgumentArity Arity { get; }
```

Gets the arity of the command line option.

### Description

```csharp
public string Description { get; }
```

Gets the description of the command line option.

### IsHidden

```csharp
public bool IsHidden { get; }
```

Gets a value indicating whether the command line option is hidden.

### Name

```csharp
public string Name { get; }
```

Gets the name of the command line option.

## Methods

### Equals

```csharp
public bool Equals(CommandLineOption? other)
```

```csharp
public override bool Equals(object? obj)
```

### GetHashCode

```csharp
public override int GetHashCode()
```
