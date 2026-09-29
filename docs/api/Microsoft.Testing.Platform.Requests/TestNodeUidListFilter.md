# TestNodeUidListFilter class

- Namespace: `Microsoft.Testing.Platform.Requests`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents a filter based on test node UIDs.

```csharp
public sealed class TestNodeUidListFilter : ITestExecutionFilter
```

## Constructors

### TestNodeUidListFilter

```csharp
public TestNodeUidListFilter(TestNodeUid[] testNodeUids)
```

Initializes a new instance of the `TestNodeUidListFilter` class.

**Parameters:**

- `testNodeUids`: The test node UIDs to filter. An empty array selects no tests.

## Properties

### TestNodeUids

```csharp
public TestNodeUid[] TestNodeUids { get; }
```

Gets the test node UIDs to filter.
