# ILogger interface

- Namespace: `Microsoft.Testing.Platform.Logging`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents a logger that can be used for logging messages.

```csharp
public interface ILogger
```

## Methods

### IsEnabled

```csharp
bool IsEnabled(LogLevel logLevel)
```

Checks if the logger is enabled for the specified log level.

**Parameters:**

- `logLevel`: The log level to check.

**Returns:** True if the logger is enabled for the specified log level, otherwise false.

### Log

```csharp
void Log<TState>(
    LogLevel logLevel,
    TState state,
    Exception? exception,
    Func<TState, Exception?, string> formatter)
```

Logs a message with the specified log level, state, exception, and formatter.

**Type parameters:**

- `TState`: The type of the state object.

**Parameters:**

- `logLevel`: The log level of the message.
- `state`: The state object.
- `exception`: The exception associated with the message.
- `formatter`: The formatter function to format the message.

### LogAsync

```csharp
Task LogAsync<TState>(
    LogLevel logLevel,
    TState? state,
    Exception? exception,
    Func<TState?, Exception?, string> formatter)
```

Asynchronously logs a message with the specified log level, state, exception, and formatter.

**Type parameters:**

- `TState`: The type of the state object.

**Parameters:**

- `logLevel`: The log level of the message.
- `state`: The state object.
- `exception`: The exception associated with the message.
- `formatter`: The formatter function to format the message.

**Returns:** A task representing the asynchronous operation.
