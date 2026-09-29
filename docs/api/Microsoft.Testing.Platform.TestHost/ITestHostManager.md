# ITestHostManager interface

- Namespace: `Microsoft.Testing.Platform.TestHost`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents the interface for managing the test host.

```csharp
public interface ITestHostManager
```

## Methods

### AddDataConsumer

```csharp
void AddDataConsumer(Func<IServiceProvider, IDataConsumer> dataConsumerFactory)
```

Adds a data consumer.

**Parameters:**

- `dataConsumerFactory`: The factory method for creating the data consumer.

```csharp
void AddDataConsumer<T>(CompositeExtensionFactory<T> compositeServiceFactory)
```

Adds a data consumer of type T.

**Type parameters:**

- `T`: The type of the data consumer.

**Parameters:**

- `compositeServiceFactory`: The composite extension factory for creating the data consumer.

### AddTestHostApplicationLifetime

```csharp
void AddTestHostApplicationLifetime(Func<IServiceProvider, ITestHostApplicationLifetime> testHostApplicationLifetimeFactory)
```

Adds a test application lifecycle callbacks.

**Parameters:**

- `testHostApplicationLifetimeFactory`: The factory method for creating the test host application lifetime callbacks.

### AddTestSessionLifetimeHandler

```csharp
void AddTestSessionLifetimeHandler(Func<IServiceProvider, ITestSessionLifetimeHandler> testSessionLifetimeHandleFactory)
```

Adds a test session lifetime handle.

**Parameters:**

- `testSessionLifetimeHandleFactory`: The factory method for creating the test session lifetime handle.

```csharp
void AddTestSessionLifetimeHandler<T>(CompositeExtensionFactory<T> compositeServiceFactory)
```

Adds a test session lifetime handle of type T.

**Type parameters:**

- `T`: The type of the test session lifetime handle.

**Parameters:**

- `compositeServiceFactory`: The composite extension factory for creating the test session lifetime handle.
