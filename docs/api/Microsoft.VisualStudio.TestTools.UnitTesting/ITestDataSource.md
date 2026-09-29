# ITestDataSource interface

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

Test data source for data driven tests.

```csharp
public interface ITestDataSource
```

## Methods

### GetData

```csharp
IEnumerable<object?[]> GetData(MethodInfo methodInfo)
```

Gets the test data from custom test data source.

**Parameters:**

- `methodInfo`: The method info of test method.

**Returns:** Test data for calling test method.

#### Remarks

Each element of the returned sequence represents the arguments for a single invocation of the test method. In the common case, an element is an `Object` array whose items are the positional arguments passed to the test method.

To attach per-row metadata (such as a custom display name, an ignore reason, or test categories), return a single-element `Object` array whose only item is a `TestDataRow` instance, for example `new object[] { new TestDataRow<(int, int, int)>((1, 2, 3)) { DisplayName = "my row" } }`. When MSTest sees a `TestDataRow`, it unwraps its `TestDataRow.Value` to obtain the actual test method arguments and applies the row's `TestDataRow.DisplayName`, `TestDataRow.IgnoreMessage`, and `TestDataRow.TestCategories`.

The whole data source can be ignored (rather than a single row) by implementing `ITestDataSourceIgnoreCapability` on the data source type.

### GetDisplayName

```csharp
string? GetDisplayName(MethodInfo methodInfo, object?[]? data)
```

Gets the display name corresponding to test data row for displaying in TestResults.

**Parameters:**

- `methodInfo`: The method info of test method.
- `data`: The test data which is passed to test method.

**Returns:** The `String`.
