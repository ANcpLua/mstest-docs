# RunTestExecutionRequest class

- Namespace: `Microsoft.Testing.Platform.Requests`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents a request to run test execution.

```csharp
public class RunTestExecutionRequest : TestExecutionRequest
```

## Constructors

### RunTestExecutionRequest

```csharp
public RunTestExecutionRequest(TestSessionContext session)
```

Initializes a new instance of the `RunTestExecutionRequest` class.

**Parameters:**

- `session`: The test session context.

```csharp
public RunTestExecutionRequest(TestSessionContext session, ITestExecutionFilter executionFilter)
```

Represents a request to run test execution.
