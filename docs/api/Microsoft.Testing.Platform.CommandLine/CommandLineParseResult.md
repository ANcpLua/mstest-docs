# CommandLineParseResult class

- Namespace: `Microsoft.Testing.Platform.CommandLine`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents the result of parsing a command line.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public sealed class CommandLineParseResult : IEquatable<CommandLineParseResult>
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Constructors

### CommandLineParseResult

```csharp
public CommandLineParseResult(
    string? toolName,
    IReadOnlyList<CommandLineParseOption> options,
    IReadOnlyList<string> errors)
```

Initializes a new instance of the `CommandLineParseResult` class.

**Parameters:**

- `toolName`: The name of the tool.
- `options`: The collection of parsed options.
- `errors`: The collection of errors associated to the parsing.

## Fields

### OptionPrefix

```csharp
public const char OptionPrefix = '-'
```

The prefix for options.

## Properties

### Empty

```csharp
public static CommandLineParseResult Empty { get; }
```

Gets an empty `CommandLineParseResult`.

### Errors

```csharp
public IReadOnlyList<string> Errors { get; }
```

Gets the collection of errors associated to the parsing.

### HasError

```csharp
public bool HasError { get; }
```

Gets a value indicating whether the parsing has errors.

### HasTool

```csharp
public bool HasTool { get; }
```

Gets a value indicating whether the parsing has a tool.

### Options

```csharp
public IReadOnlyList<CommandLineParseOption> Options { get; }
```

Gets the collection of parsed options.

### ToolName

```csharp
public string? ToolName { get; }
```

Gets the name of the tool.

## Methods

### Equals

```csharp
public bool Equals(CommandLineParseResult? other)
```

```csharp
public override bool Equals(object? obj)
```

### GetHashCode

```csharp
public override int GetHashCode()
```

### IsOptionSet

```csharp
public bool IsOptionSet(string optionName)
```

Determines if the specified option is set.

**Parameters:**

- `optionName`: The name of the option.

**Returns:** Returns `true` if the option is set; `false` otherwise.

### ToString

```csharp
public override string ToString()
```

### TryGetOptionArgumentList

```csharp
public bool TryGetOptionArgumentList(string optionName, [NotNullWhen(true)] out string[]? arguments)
```

Gets the argument list for the specified option.

**Parameters:**

- `optionName`: The name of the option.
- `arguments`: The arguments associated with the option.

**Returns:** Returns `true` if there are some arguments; `false` otherwise.
