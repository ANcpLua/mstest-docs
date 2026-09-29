# IOutputDevice interface

- Namespace: `Microsoft.Testing.Platform.OutputDevice`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents an output device.

```csharp
public interface IOutputDevice
```

## Methods

### DisplayAsync

```csharp
Task DisplayAsync(
    IOutputDeviceDataProducer producer,
    IOutputDeviceData data,
    CancellationToken cancellationToken)
```

Displays the output data asynchronously.

**Parameters:**

- `producer`: The data producer.
- `data`: The output data.
- `cancellationToken`: The cancellation token.

**Returns:** A task representing the asynchronous operation.
