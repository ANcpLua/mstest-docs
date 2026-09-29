# ExceptionOutputDeviceData class

- Namespace: `Microsoft.Testing.Platform.OutputDevice`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents an exception output data.

```csharp
public sealed class ExceptionOutputDeviceData : IOutputDeviceData
```

## Constructors

### ExceptionOutputDeviceData

```csharp
public ExceptionOutputDeviceData(Exception exception)
```

Represents an exception output data.

**Parameters:**

- `exception`: The exception.

## Properties

### Exception

```csharp
public Exception Exception { get; }
```

Gets the exception.
