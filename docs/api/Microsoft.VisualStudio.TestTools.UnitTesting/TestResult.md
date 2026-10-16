# TestResult class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

TestResult object to be returned to adapter.

```csharp
public class TestResult
```

## Constructors

### TestResult

```csharp
public TestResult()
```

## Properties

### DebugTrace

```csharp
public string? DebugTrace { get; set; }
```

Gets or sets the debug traces by test code.

### DisplayName

```csharp
public string? DisplayName { get; set; }
```

Gets or sets the display name of the result. Useful when returning multiple results. If null then Method name is used as DisplayName.

### Duration

```csharp
public TimeSpan Duration { get; set; }
```

Gets or sets the duration of test execution.

### ExecutionId

```csharp
public Guid ExecutionId { get; set; }
```

Gets or sets the execution id of the result.

### LogError

```csharp
public string? LogError { get; set; }
```

Gets or sets the output of the message logged by test code.

### LogOutput

```csharp
public string? LogOutput { get; set; }
```

Gets or sets the output of the message logged by test code.

### Outcome

```csharp
public UnitTestOutcome Outcome { get; set; }
```

Gets or sets the outcome of the test execution.

### ParentExecId

```csharp
public Guid ParentExecId { get; set; }
```

Gets or sets the parent execution id of the result.

### ResultFiles

```csharp
public IList<string>? ResultFiles { get; set; }
```

Gets or sets the result files attached by the test.

### TestContextMessages

```csharp
public string? TestContextMessages { get; set; }
```

Gets or sets the debug traces by test code.

### TestFailureException

```csharp
public Exception? TestFailureException { get; set; }
```

Gets or sets the exception thrown when test is failed.
