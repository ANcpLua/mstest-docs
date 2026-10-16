# IBlockingDataConsumer interface

- Namespace: `Microsoft.Testing.Platform.Extensions`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Marker interface for a `IDataConsumer` that must consume the data inline, before the call to publish the data returns to the producer.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public interface IBlockingDataConsumer : IDataConsumer, IExtension
```

## Remarks

A regular `IDataConsumer` consumes data asynchronously: the data is queued and processed on a background loop, so there is no guarantee about when `IDataConsumer.ConsumeAsync(IDataProducer,IData,CancellationToken)` runs relative to the producer continuing its work. A consumer that additionally implements `IBlockingDataConsumer` is instead invoked inline by the message bus, so the producer's call to publish does not return until `IDataConsumer.ConsumeAsync(IDataProducer,IData,CancellationToken)` has completed. This is useful for extensions that need to guarantee a piece of work happens before the producer proceeds (for example, before a test starts running).

Because consumption happens inline, any exception thrown by `IDataConsumer.ConsumeAsync(IDataProducer,IData,CancellationToken)` propagates back to the producer that published the data, rather than being observed later during drain. Implementations should therefore avoid throwing for non-fatal conditions.

Inline consumption is serialized: only one `IDataConsumer.ConsumeAsync(IDataProducer,IData,CancellationToken)` call runs at a time per consumer. As a consequence, a blocking consumer must not, from within its `IDataConsumer.ConsumeAsync(IDataProducer,IData,CancellationToken)`, publish data that is routed back to itself, as that would deadlock. Note that publishing data where the producer is the consumer itself (same UID) is safe, because the message bus skips delivering a producer's data back to that same producer; the deadlock risk is specifically re-entrant publishing that routes back to this consumer under a *different* producer UID.

This API is experimental. It may change, break, or be removed at any time without notice.
