# ExecuteRequestContext class

- Namespace: `Microsoft.Testing.Platform.Extensions.TestFramework`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

This class represents the context that is passed to a test framework adapter when the `ITestFramework.ExecuteRequestAsync(ExecuteRequestContext)` method is called.

```csharp
public sealed class ExecuteRequestContext
```

## Remarks

It contains information about the request, message bus, semaphore, and cancellation token.

## Constructors

### ExecuteRequestContext

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public ExecuteRequestContext(
    IRequest request,
    IMessageBus messageBus,
    IExecuteRequestCompletionNotifier executeRequestCompletionNotifier,
    CancellationToken cancellationToken)
```

Initializes a new instance of the `ExecuteRequestContext` class.

**Parameters:**

- `request`: The request.
- `messageBus`: The message bus.
- `executeRequestCompletionNotifier`: The request completion notifier.
- `cancellationToken`: The cancellation token.

#### Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Properties

### CancellationToken

```csharp
public CancellationToken CancellationToken { get; }
```

Gets the cancellation token that can be used to cancel the execution.

### MessageBus

```csharp
public IMessageBus MessageBus { get; }
```

Gets the message bus used for reporting test execution events.

### Request

```csharp
public IRequest Request { get; }
```

Gets the request associated with the execution.

## Methods

### Complete

```csharp
public void Complete()
```

Completes the execution request.

### StartTestExecutionAsync

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public Task<TestExecution> StartTestExecutionAsync(IDataProducer dataProducer, TestNodeUpdateMessage inProgressMessage)
```

Starts a canonical test execution and publishes its in-progress message.

**Parameters:**

- `dataProducer`: The data producer reporting the test execution.
- `inProgressMessage`: The in-progress test node update.

**Returns:** A task containing the started test execution.

#### Remarks

This API is experimental. It may change, break, or be removed at any time without notice.
