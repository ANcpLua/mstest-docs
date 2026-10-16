# TestExecution class

- Namespace: `Microsoft.Testing.Platform.Extensions.TestFramework`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents one canonical test execution occurrence.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public sealed class TestExecution : IDisposable
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Methods

### CompleteAsync

```csharp
public Task CompleteAsync(IReadOnlyList<TestNodeUpdateMessage> resultMessages, DateTimeOffset executionEndTime)
```

Completes this test execution by publishing its ordered result messages.

**Parameters:**

- `resultMessages`: The result messages to publish in order. The last message is the final result. An empty collection publishes an execution-completed update without inventing an outcome.
- `executionEndTime`: The producer-observed time at which test execution ended.

**Returns:** A task representing the asynchronous operation.

### Dispose

```csharp
public void Dispose()
```

Abandons an uncompleted test execution without publishing or inventing a result.

### Run

```csharp
public T? Run<T>(Func<T?> callback)
```

Runs a callback in the canonical context of this test execution and returns its result.

**Type parameters:**

- `T`: The callback result type.

**Parameters:**

- `callback`: The callback to run.

**Returns:** The callback result.

```csharp
public void Run(Action callback)
```

Runs a callback in the canonical context of this test execution.

**Parameters:**

- `callback`: The callback to run.

### RunAsync

```csharp
public Task RunAsync(Func<Task> callback)
```

Runs an asynchronous callback in the canonical context of this test execution.

**Parameters:**

- `callback`: The callback to run.

**Returns:** A task representing the asynchronous operation.

```csharp
public Task<T?> RunAsync<T>(Func<Task<T?>> callback)
```

Runs an asynchronous callback in the canonical context of this test execution and returns its result.

**Type parameters:**

- `T`: The callback result type.

**Parameters:**

- `callback`: The callback to run.

**Returns:** A task containing the callback result.
