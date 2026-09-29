# DiscoverTestExecutionRequest class

- Namespace: `Microsoft.Testing.Platform.Requests`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents a request to discover test execution.

```csharp
public class DiscoverTestExecutionRequest : TestExecutionRequest
```

## Constructors

### DiscoverTestExecutionRequest

```csharp
public DiscoverTestExecutionRequest(TestSessionContext session)
```

Initializes a new instance of the `DiscoverTestExecutionRequest` class.

**Parameters:**

- `session`: The test session context.

```csharp
public DiscoverTestExecutionRequest(TestSessionContext session, ITestExecutionFilter executionFilter)
```

Represents a request to discover test execution.
