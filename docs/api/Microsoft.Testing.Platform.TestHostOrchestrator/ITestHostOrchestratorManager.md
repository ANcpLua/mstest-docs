# ITestHostOrchestratorManager interface

- Namespace: `Microsoft.Testing.Platform.TestHostOrchestrator`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents a manager for test host orchestrators.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public interface ITestHostOrchestratorManager
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Methods

### AddTestHostOrchestrator

```csharp
void AddTestHostOrchestrator(Func<IServiceProvider, ITestHostExecutionOrchestrator> factory)
```

Adds a test host orchestrator.

**Parameters:**

- `factory`: The factory method for creating the test host orchestrator.

### AddTestHostOrchestratorApplicationLifetime

```csharp
void AddTestHostOrchestratorApplicationLifetime(
    Func<IServiceProvider, ITestHostOrchestratorApplicationLifetime> testHostOrchestratorApplicationLifetimeFactory)
```

Adds a test host orchestrator application lifetime.

**Parameters:**

- `testHostOrchestratorApplicationLifetimeFactory`: The factory method for creating the test host orchestrator application lifetime.
