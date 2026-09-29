# TestExecutionRequest class

- Namespace: `Microsoft.Testing.Platform.Requests`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents a request for test execution.

```csharp
public abstract class TestExecutionRequest : IRequest
```

## Constructors

### TestExecutionRequest

```csharp
protected TestExecutionRequest(TestSessionContext session, ITestExecutionFilter filter)
```

Initializes a new instance of the `TestExecutionRequest` class.

**Parameters:**

- `session`: The test session context.
- `filter`: The test execution filter.

## Properties

### Filter

```csharp
public ITestExecutionFilter Filter { get; }
```

Gets the test execution filter.

### Session

```csharp
public TestSessionContext Session { get; }
```

Gets the test session context.
