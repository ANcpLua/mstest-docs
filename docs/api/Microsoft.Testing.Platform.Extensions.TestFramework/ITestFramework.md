# ITestFramework interface

- Namespace: `Microsoft.Testing.Platform.Extensions.TestFramework`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

A specialized extension that represents a test framework.

```csharp
public interface ITestFramework : IExtension
```

## Methods

### CloseTestSessionAsync

```csharp
Task<CloseTestSessionResult> CloseTestSessionAsync(CloseTestSessionContext context)
```

Ask to the test framework to destroy the test session and release all the resources.

**Parameters:**

- `context`: The test session destruction context.

### CreateTestSessionAsync

```csharp
Task<CreateTestSessionResult> CreateTestSessionAsync(CreateTestSessionContext context)
```

Ask to the test framework to create a test session.

**Parameters:**

- `context`: The test session creation context.

### ExecuteRequestAsync

```csharp
Task ExecuteRequestAsync(ExecuteRequestContext context)
```

Ask to the test framework to execute a test execution request.

**Parameters:**

- `context`: The test execution request context.
