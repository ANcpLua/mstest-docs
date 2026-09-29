# ITestHostApplicationLifetime interface

- Namespace: `Microsoft.Testing.Platform.Extensions.TestHost`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents the interface for test application lifecycle callbacks.

```csharp
public interface ITestHostApplicationLifetime : ITestHostExtension, IExtension
```

## Methods

### AfterRunAsync

```csharp
Task AfterRunAsync(int exitCode, CancellationToken cancellationToken)
```

Executes after the test run.

**Parameters:**

- `exitCode`: The exit code of the test run.
- `cancellationToken`: The cancellation token.

**Returns:** A task representing the asynchronous operation.

### BeforeRunAsync

```csharp
Task BeforeRunAsync(CancellationToken cancellationToken)
```

Executes before the test run.

**Parameters:**

- `cancellationToken`: The cancellation token.

**Returns:** A task representing the asynchronous operation.
