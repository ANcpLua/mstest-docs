# LoggingExtensions class

- Namespace: `Microsoft.Testing.Platform.Logging`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

A set of extension methods for `ILogger`.

```csharp
public static class LoggingExtensions
```

## Methods

### LogCritical

```csharp
public static void LogCritical(this ILogger logger, string message)
```

Logs a message with the critical log level.

**Parameters:**

- `logger`: The logger.
- `message`: The message to log.

### LogCriticalAsync

```csharp
public static Task LogCriticalAsync(this ILogger logger, string message)
```

Logs a message with the critical log level.

**Parameters:**

- `logger`: The logger.
- `message`: The message to log.

### LogDebug

```csharp
public static void LogDebug(this ILogger logger, string message)
```

Logs a message with the debug log level.

**Parameters:**

- `logger`: The logger.
- `message`: The message to log.

### LogDebugAsync

```csharp
public static Task LogDebugAsync(this ILogger logger, string message)
```

Logs a message with the debug log level.

**Parameters:**

- `logger`: The logger.
- `message`: The message.

### LogError

```csharp
public static void LogError(this ILogger logger, Exception ex)
```

Logs a message with the error log level.

**Parameters:**

- `logger`: The logger.
- `ex`: The exception.

```csharp
public static void LogError(this ILogger logger, string message)
```

Logs a message with the error log level.

**Parameters:**

- `logger`: The logger.
- `message`: The message to log.

```csharp
public static void LogError(
    this ILogger logger,
    string message,
    Exception ex)
```

Logs a message with the error log level.

**Parameters:**

- `logger`: The logger.
- `message`: The message to log.
- `ex`: The exception.

### LogErrorAsync

```csharp
public static Task LogErrorAsync(this ILogger logger, Exception ex)
```

Logs a message with the error log level.

**Parameters:**

- `logger`: The logger.
- `ex`: The exception.

```csharp
public static Task LogErrorAsync(this ILogger logger, string message)
```

Logs a message with the error log level.

**Parameters:**

- `logger`: The logger.
- `message`: The message.

```csharp
public static Task LogErrorAsync(
    this ILogger logger,
    string message,
    Exception ex)
```

Logs a message with the error log level.

**Parameters:**

- `logger`: The logger.
- `message`: The message.
- `ex`: The exception.

### LogInformation

```csharp
public static void LogInformation(this ILogger logger, string message)
```

Logs a message with the info log level.

**Parameters:**

- `logger`: The logger.
- `message`: The message to log.

### LogInformationAsync

```csharp
public static Task LogInformationAsync(this ILogger logger, string message)
```

Logs a message with the info log level.

**Parameters:**

- `logger`: The logger.
- `message`: The message.

### LogTrace

```csharp
public static void LogTrace(this ILogger logger, string message)
```

Logs a message with the trace log level.

**Parameters:**

- `logger`: The logger.
- `message`: The message to log.

### LogTraceAsync

```csharp
public static Task LogTraceAsync(this ILogger logger, string message)
```

Logs a message with the trace log level.

**Parameters:**

- `logger`: The logger.
- `message`: The message.

### LogWarning

```csharp
public static void LogWarning(this ILogger logger, string message)
```

Logs a message with the warning log level.

**Parameters:**

- `logger`: The logger.
- `message`: The message to log.

### LogWarningAsync

```csharp
public static Task LogWarningAsync(this ILogger logger, string message)
```

Logs a message with the warning log level.

**Parameters:**

- `logger`: The logger.
- `message`: The message.
