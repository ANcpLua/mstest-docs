# IDataProducer interface

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents a data producer extension.

```csharp
public interface IDataProducer : IExtension
```

## Properties

### DataTypesProduced

```csharp
Type[] DataTypesProduced { get; }
```

Gets the types of data produced by the data producer.
