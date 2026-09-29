# DynamicDataAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

Attribute to define dynamic data for a test method.

```csharp
[AttributeUsage(AttributeTargets.Method, AllowMultiple = true, Inherited = false)]
public sealed class DynamicDataAttribute : Attribute, ITestDataSource, ITestDataSourceEmptyDataSourceExceptionInfo, ITestDataSourceIgnoreCapability
```

## Constructors

### DynamicDataAttribute

```csharp
public DynamicDataAttribute(string dynamicDataSourceName)
```

Initializes a new instance of the `DynamicDataAttribute` class.

**Parameters:**

- `dynamicDataSourceName`: The name of method, property, or field having test data.

```csharp
public DynamicDataAttribute(string dynamicDataSourceName, Type dynamicDataDeclaringType)
```

Initializes a new instance of the `DynamicDataAttribute` class when the test data is present in a class different from test method's class.

**Parameters:**

- `dynamicDataSourceName`: The name of method, property, or field having test data.
- `dynamicDataDeclaringType`: The declaring type of property, method, or field having data. Useful in cases when declaring type is present in a class different from test method's class. If null, declaring type defaults to test method's class type.

```csharp
public DynamicDataAttribute(string dynamicDataSourceName, params object?[] dynamicDataSourceArguments)
```

Initializes a new instance of the `DynamicDataAttribute` class.

**Parameters:**

- `dynamicDataSourceName`: The name of method, property, or field having test data.
- `dynamicDataSourceArguments`: Arguments to be passed to method referred to by `dynamicDataSourceName`.

```csharp
public DynamicDataAttribute(
    string dynamicDataSourceName,
    Type dynamicDataDeclaringType,
    params object?[] dynamicDataSourceArguments)
```

Initializes a new instance of the `DynamicDataAttribute` class when the test data is present in a class different from test method's class.

**Parameters:**

- `dynamicDataSourceName`: The name of method, property, or field having test data.
- `dynamicDataDeclaringType`: The declaring type of property, method, or field having data. Useful in cases when declaring type is present in a class different from test method's class. If null, declaring type defaults to test method's class type.
- `dynamicDataSourceArguments`: Arguments to be passed to method referred to by `dynamicDataSourceName`.

## Properties

### DynamicDataDisplayName

```csharp
public string? DynamicDataDisplayName { get; set; }
```

Gets or sets the name of method used to customize the display name in test results.

### DynamicDataDisplayNameDeclaringType

```csharp
public Type? DynamicDataDisplayNameDeclaringType { get; set; }
```

Gets or sets the declaring type used to customize the display name in test results.

### IgnoreMessage

```csharp
public string? IgnoreMessage { get; set; }
```

Gets or sets a reason to ignore this dynamic data source. Setting the property to non-null value will ignore the dynamic data source.

## Methods

### GetData

```csharp
public IEnumerable<object[]> GetData(MethodInfo methodInfo)
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
public string? GetDisplayName(MethodInfo methodInfo, object?[]? data)
```

Gets the display name corresponding to test data row for displaying in TestResults.

**Parameters:**

- `methodInfo`: The method info of test method.
- `data`: The test data which is passed to test method.

**Returns:** The `String`.
