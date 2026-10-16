# CommandLineParseOption class

- Namespace: `Microsoft.Testing.Platform.CommandLine`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents a command line parsed option.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public sealed class CommandLineParseOption
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Constructors

### CommandLineParseOption

```csharp
public CommandLineParseOption(string name, string[] arguments)
```

Represents a command line parsed option.

**Parameters:**

- `name`: The name of the option.
- `arguments`: The arguments associated to this option.

#### Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Properties

### Arguments

```csharp
public string[] Arguments { get; }
```

Gets the arguments of the option.

### Name

```csharp
public string Name { get; }
```

Gets the name of the option.
