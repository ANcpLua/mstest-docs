# ILoggerFactory interface

- Namespace: `Microsoft.Testing.Platform.Logging`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents a factory for creating loggers.

```csharp
public interface ILoggerFactory
```

## Methods

### CreateLogger

```csharp
ILogger CreateLogger(string categoryName)
```

Creates a logger with the specified category name.

**Parameters:**

- `categoryName`: The name of the category for the logger.

**Returns:** A new instance of the logger.
