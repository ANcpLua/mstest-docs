# ErrorMessageOutputDeviceData class

- Namespace: `Microsoft.Testing.Platform.OutputDevice`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents an error message output data.

```csharp
public sealed class ErrorMessageOutputDeviceData : IOutputDeviceData
```

## Constructors

### ErrorMessageOutputDeviceData

```csharp
public ErrorMessageOutputDeviceData(string message)
```

Represents an error message output data.

**Parameters:**

- `message`: The error message.

## Properties

### Message

```csharp
public string Message { get; }
```

Gets the error message.
