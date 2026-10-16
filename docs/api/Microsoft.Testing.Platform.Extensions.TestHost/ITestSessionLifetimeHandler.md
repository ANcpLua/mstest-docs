# ITestSessionLifetimeHandler interface

- Namespace: `Microsoft.Testing.Platform.Extensions.TestHost`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents an interface for handling the lifetime of a test session.

```csharp
public interface ITestSessionLifetimeHandler : ITestHostExtension, IExtension
```

## Methods

### OnTestSessionFinishingAsync

```csharp
Task OnTestSessionFinishingAsync(ITestSessionContext testSessionContext)
```

Called when a test session is finishing.

**Parameters:**

- `testSessionContext`: A test session context containing the unique identifier of the session as well as cancellation token.

**Returns:** A task representing the asynchronous operation.

### OnTestSessionStartingAsync

```csharp
Task OnTestSessionStartingAsync(ITestSessionContext testSessionContext)
```

Called when a test session is starting.

**Parameters:**

- `testSessionContext`: A test session context containing the unique identifier of the session as well as cancellation token.

**Returns:** A task representing the asynchronous operation.
