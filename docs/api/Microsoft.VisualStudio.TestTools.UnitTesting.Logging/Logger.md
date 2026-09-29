# Logger class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting.Logging`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

Enables users to log/write traces from unit tests for diagnostics.

```csharp
public class Logger
```

## Constructors

### Logger

```csharp
public Logger()
```

## Methods

### LogMessage

```csharp
public static void LogMessage(string format, params object?[] args)
```

API for test writer to call to Log messages.

**Parameters:**

- `format`: String format with placeholders.
- `args`: Parameters for placeholders.

## Events

### OnLogMessage

```csharp
public static event Logger.LogMessageHandler? OnLogMessage
```

Event to listen. Raised when unit test writer writes some message. Mainly to consume by adapter.
