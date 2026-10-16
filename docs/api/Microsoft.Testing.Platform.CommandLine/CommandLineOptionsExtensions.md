# CommandLineOptionsExtensions class

- Namespace: `Microsoft.Testing.Platform.CommandLine`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Provides extension methods for command-line options.

```csharp
public static class CommandLineOptionsExtensions
```

## Methods

### TryGetOptionArgumentListOrDefault

```csharp
public static bool TryGetOptionArgumentListOrDefault(
    this ICommandLineOptions commandLineOptions,
    string optionName,
    [NotNullWhen(true)] out string[]? arguments)
```

Tries to get the explicit argument list for an option, falling back to a passive default from `commandLineOptionDefaults` in `testconfig.json`.

**Parameters:**

- `commandLineOptions`: The command-line options.
- `optionName`: The name of the option.
- `arguments`: The explicit or default argument list, if found.

**Returns:** `true` if an explicit value or configured default was found; otherwise, `false`.

#### Remarks

A configured default does not make `ICommandLineOptions.IsOptionSet(String)` return `true`. Extensions should use this method only after determining that the feature which owns the option is enabled.
