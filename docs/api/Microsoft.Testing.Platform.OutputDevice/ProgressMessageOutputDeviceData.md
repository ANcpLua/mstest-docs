# ProgressMessageOutputDeviceData class

- Namespace: `Microsoft.Testing.Platform.OutputDevice`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents a transient message displayed in the terminal progress area.

```csharp
public sealed class ProgressMessageOutputDeviceData : IOutputDeviceData
```

## Remarks

Messages are scoped to their `IOutputDeviceDataProducer` and identified by `ProgressMessageOutputDeviceData.Key`. Sending another message with the same key replaces the previous text. A `null` `ProgressMessageOutputDeviceData.Message` removes the message from an interactive progress area. When interactive progress is unavailable or disabled, each changed value is written as a durable line instead; those lines remain in terminal scrollback and cannot be removed by a later update. Progress messages are currently not forwarded through the `dotnet test` pipe protocol, where the SDK owns terminal rendering. Keyed protocol forwarding is required before this payload can be represented there.

## Constructors

### ProgressMessageOutputDeviceData

```csharp
public ProgressMessageOutputDeviceData(string key, string? message)
```

Initializes a new instance of the `ProgressMessageOutputDeviceData` class.

**Parameters:**

- `key`: The producer-local key used to replace or remove the message.
- `message`: The message to display, or `null` to remove it from an interactive progress area.

## Properties

### Key

```csharp
public string Key { get; }
```

Gets the producer-local key used to replace or remove the message.

### Message

```csharp
public string? Message { get; }
```

Gets the message to display, or `null` when the message should be removed.
