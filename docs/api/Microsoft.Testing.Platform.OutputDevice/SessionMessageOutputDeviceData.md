# SessionMessageOutputDeviceData class

- Namespace: `Microsoft.Testing.Platform.OutputDevice`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents a durable session message that remains visible in the terminal output.

```csharp
public sealed class SessionMessageOutputDeviceData : IOutputDeviceData
```

## Remarks

Under the `dotnet test` pipe protocol, delivery requires an active connection that negotiates protocol version 1.3.0 or later. The host drops the message when no connection is available or an older protocol is negotiated because those SDK versions cannot deserialize informational display messages.

## Constructors

### SessionMessageOutputDeviceData

```csharp
public SessionMessageOutputDeviceData(string message)
```

Initializes a new instance of the `SessionMessageOutputDeviceData` class.

**Parameters:**

- `message`: The message to display.

## Properties

### Message

```csharp
public string Message { get; }
```

Gets the message to display.
