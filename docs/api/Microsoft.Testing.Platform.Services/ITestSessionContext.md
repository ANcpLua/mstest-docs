# ITestSessionContext interface

- Namespace: `Microsoft.Testing.Platform.Services`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Interface representing the context of a test session. It's used in ITestSessionLifetimeHandler to provide information about the session.

```csharp
public interface ITestSessionContext
```

## Properties

### CancellationToken

```csharp
CancellationToken CancellationToken { get; }
```

Gets the cancellation token for the test session.

### SessionUid

```csharp
SessionUid SessionUid { get; }
```

Gets a unique identifier for the test session.
