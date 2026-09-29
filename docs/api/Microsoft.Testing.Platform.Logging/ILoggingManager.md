# ILoggingManager interface

- Namespace: `Microsoft.Testing.Platform.Logging`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents a logging manager that can be used to add logger providers.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public interface ILoggingManager
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Methods

### AddProvider

```csharp
void AddProvider(Func<LogLevel, IServiceProvider, ILoggerProvider> loggerProviderFactory)
```

Adds a logger provider factory to the logging manager.

**Parameters:**

- `loggerProviderFactory`: A function taking a `LogLevel` and a `IServiceProvider` to build the `ILoggerProvider`.
