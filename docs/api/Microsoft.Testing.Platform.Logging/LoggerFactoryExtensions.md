# LoggerFactoryExtensions class

- Namespace: `Microsoft.Testing.Platform.Logging`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Provides extension methods for the `ILoggerFactory` interface.

```csharp
public static class LoggerFactoryExtensions
```

## Methods

### CreateLogger

```csharp
public static ILogger<TCategoryName?> CreateLogger<TCategoryName>(this ILoggerFactory factory)
```

Creates a logger instance for the specified category name.

**Type parameters:**

- `TCategoryName`: The type of the category name.

**Parameters:**

- `factory`: The logger factory.

**Returns:** A logger instance.
