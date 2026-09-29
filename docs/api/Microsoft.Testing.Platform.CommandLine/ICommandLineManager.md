# ICommandLineManager interface

- Namespace: `Microsoft.Testing.Platform.CommandLine`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents a command line manager.

```csharp
public interface ICommandLineManager
```

## Methods

### AddProvider

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
void AddProvider(Func<IServiceProvider, ICommandLineOptionsProvider> commandLineProviderFactory)
```

Adds a command line options provider.

**Parameters:**

- `commandLineProviderFactory`: The factory method for creating the command line options provider, given a service provider.

#### Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

```csharp
void AddProvider(Func<ICommandLineOptionsProvider> commandLineProviderFactory)
```

Adds a command line options provider.

**Parameters:**

- `commandLineProviderFactory`: The factory method for creating the command line options provider.
