# CloseTestSessionContext class

- Namespace: `Microsoft.Testing.Platform.Extensions.TestFramework`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Context passed to a test framework adapter when `ITestFramework.CloseTestSessionAsync(CloseTestSessionContext)` is called.

```csharp
public sealed class CloseTestSessionContext : TestSessionContext
```

## Properties

### CancellationToken

```csharp
public CancellationToken CancellationToken { get; }
```

Gets the cancellation token used to cancel the operation.
