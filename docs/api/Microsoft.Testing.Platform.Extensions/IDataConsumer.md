# IDataConsumer interface

- Namespace: `Microsoft.Testing.Platform.Extensions`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents a data consumer that can consume data produced by a data producer.

```csharp
public interface IDataConsumer : IExtension
```

## Remarks

The message bus does not dispatch data to a consumer when the consumer and producer have the same `IExtension.Uid`. Producer and consumer registrations that communicate through the message bus must use different UIDs. An extension that processes its own data should invoke that processing directly.

## Properties

### DataTypesConsumed

```csharp
Type[] DataTypesConsumed { get; }
```

Gets the types of data consumed by the data consumer.

## Methods

### ConsumeAsync

```csharp
Task ConsumeAsync(
    IDataProducer dataProducer,
    IData value,
    CancellationToken cancellationToken)
```

Consumes the specified data produced by a data producer.

**Parameters:**

- `dataProducer`: The data producer.
- `value`: The data to be consumed.
- `cancellationToken`: The cancellation token.

**Returns:** A task representing the asynchronous operation.
