# ITestHostProcessLifetimeHandler interface

- Namespace: `Microsoft.Testing.Platform.Extensions.TestHostControllers`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents an interface for handling the lifetime of the test host process.

```csharp
public interface ITestHostProcessLifetimeHandler : ITestHostControllersExtension, IExtension
```

## Methods

### BeforeTestHostProcessStartAsync

```csharp
Task BeforeTestHostProcessStartAsync(CancellationToken cancellationToken)
```

Executes before the test host process starts.

**Parameters:**

- `cancellationToken`: The cancellation token.

**Returns:** A task representing the asynchronous operation.

### OnTestHostProcessExitedAsync

```csharp
Task OnTestHostProcessExitedAsync(ITestHostProcessInformation testHostProcessInformation, CancellationToken cancellationToken)
```

Executes when the test host process has exited.

**Parameters:**

- `testHostProcessInformation`: Information about the test host process.
- `cancellationToken`: The cancellation token.

**Returns:** A task representing the asynchronous operation.

### OnTestHostProcessStartedAsync

```csharp
Task OnTestHostProcessStartedAsync(ITestHostProcessInformation testHostProcessInformation, CancellationToken cancellationToken)
```

Executes when the test host process has started.

**Parameters:**

- `testHostProcessInformation`: Information about the test host process.
- `cancellationToken`: The cancellation token.

**Returns:** A task representing the asynchronous operation.
