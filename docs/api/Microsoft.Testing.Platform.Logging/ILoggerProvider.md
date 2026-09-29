# ILoggerProvider interface

- Namespace: `Microsoft.Testing.Platform.Logging`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents a logger provider that can be used to create loggers.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public interface ILoggerProvider
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Methods

### CreateLogger

```csharp
ILogger CreateLogger(string categoryName)
```

Creates a logger with the specified category name.

**Parameters:**

- `categoryName`: The name of the category.

**Returns:** A logger.
