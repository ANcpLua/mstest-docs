# IMessageBus interface

- Namespace: `Microsoft.Testing.Platform.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents a message bus for publishing data.

```csharp
public interface IMessageBus
```

## Methods

### PublishAsync

```csharp
Task PublishAsync(IDataProducer dataProducer, IData data)
```

Publishes the specified data using the provided data producer.

**Parameters:**

- `dataProducer`: The data producer.
- `data`: The data to be published.

**Returns:** A task representing the asynchronous operation.

#### Remarks

The data is not dispatched to consumers whose `IExtension.Uid` matches the `dataProducer`'s UID.
