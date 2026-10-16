# ICommandLineOptionsProvider interface

- Namespace: `Microsoft.Testing.Platform.Extensions.CommandLine`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents an interface for providing command line options.

```csharp
public interface ICommandLineOptionsProvider : IExtension
```

## Methods

### GetCommandLineOptions

```csharp
IReadOnlyCollection<CommandLineOption> GetCommandLineOptions()
```

Gets the command line options provided by this extension.

**Returns:** The collection of command line options.

### ValidateCommandLineOptionsAsync

```csharp
Task<ValidationResult> ValidateCommandLineOptionsAsync(ICommandLineOptions commandLineOptions)
```

Validate that the command line options are valid in the context of each other.

**Parameters:**

- `commandLineOptions`: All command line options (including the ones provided by other extensions) are provided.

**Returns:** The result of the validation.

### ValidateOptionArgumentsAsync

```csharp
Task<ValidationResult> ValidateOptionArgumentsAsync(CommandLineOption commandOption, string[] arguments)
```

Validate the arguments for the given command option.

**Parameters:**

- `commandOption`: The command option.
- `arguments`: The arguments provided for the command option.

**Returns:** The result of the validation.
