# ICommandLineOptions interface

- Namespace: `Microsoft.Testing.Platform.CommandLine`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents the interface for command line options.

```csharp
public interface ICommandLineOptions
```

## Methods

### IsOptionSet

```csharp
bool IsOptionSet(string optionName)
```

Checks if the specified option is set.

**Parameters:**

- `optionName`: The name of the option.

**Returns:** True if the option is set; otherwise, false.

### TryGetOptionArgumentList

```csharp
bool TryGetOptionArgumentList(string optionName, [NotNullWhen(true)] out string[]? arguments)
```

Tries to get the argument list for the specified option.

**Parameters:**

- `optionName`: The name of the option.
- `arguments`: The argument list for the option, if found.

**Returns:** True if the argument list is found; otherwise, false.
