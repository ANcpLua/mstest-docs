# ConfigurationExtensions class

- Namespace: `Microsoft.Testing.Platform.Configurations`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Provides extension methods for the IConfiguration interface.

```csharp
public static class ConfigurationExtensions
```

## Methods

### GetCurrentWorkingDirectory

```csharp
public static string GetCurrentWorkingDirectory(this IConfiguration configuration)
```

Gets the current working directory from the configuration.

**Parameters:**

- `configuration`: The configuration.

**Returns:** The current working directory.

### GetTestResultDirectory

```csharp
public static string GetTestResultDirectory(this IConfiguration configuration)
```

Gets the test result directory from the configuration.

**Parameters:**

- `configuration`: The configuration.

**Returns:** The test result directory.
