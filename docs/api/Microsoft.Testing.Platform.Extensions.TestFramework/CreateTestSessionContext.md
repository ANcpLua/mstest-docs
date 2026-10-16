# CreateTestSessionContext class

- Namespace: `Microsoft.Testing.Platform.Extensions.TestFramework`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Context passed to a test framework adapter when `ITestFramework.CreateTestSessionAsync(CreateTestSessionContext)` is called.

```csharp
public sealed class CreateTestSessionContext : TestSessionContext
```

## Properties

### CancellationToken

```csharp
public CancellationToken CancellationToken { get; }
```

Gets the cancellation token used to cancel the operation.
