# DataRowAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

Attribute to define in-line data for a test method.

```csharp
[AttributeUsage(AttributeTargets.Method, AllowMultiple = true, Inherited = false)]
public class DataRowAttribute : Attribute, ITestDataSource, ITestDataSourceIgnoreCapability
```

## Constructors

### DataRowAttribute

```csharp
public DataRowAttribute()
```

Initializes a new instance of the `DataRowAttribute` class.

```csharp
public DataRowAttribute(object? data)
```

Initializes a new instance of the `DataRowAttribute` class with an array of object arguments.

**Parameters:**

- `data`: The data.

#### Remarks

This constructor is only kept for CLS compliant tests.

```csharp
public DataRowAttribute(params object?[]? data)
```

Initializes a new instance of the `DataRowAttribute` class with an array of object arguments.

**Parameters:**

- `data`: The data.

```csharp
public DataRowAttribute(string?[]? stringArrayData)
```

Initializes a new instance of the `DataRowAttribute` class with an array of string arguments.

**Parameters:**

- `stringArrayData`: The string array data.

## Properties

### ArgumentsDisplayName

```csharp
public string? ArgumentsDisplayName { get; set; }
```

Gets or sets the text displayed in place of the test arguments, while retaining the test method display name.

#### Remarks

A null, empty, or whitespace-only value uses the default argument display text. Otherwise, the value is displayed verbatim using the default data-driven test name format. A non-empty, non-whitespace `DataRowAttribute.DisplayName` takes precedence over this property.

### Data

```csharp
public object?[] Data { get; }
```

Gets data for calling test method.

### DisplayName

```csharp
public string? DisplayName { get; set; }
```

Gets or sets display name in test results for customization.

### IgnoreMessage

```csharp
public string? IgnoreMessage { get; set; }
```

Gets or sets a reason to ignore the specific test case. Setting the property to non-null value will ignore the test case.

## Methods

### GetData

```csharp
public IEnumerable<object?[]> GetData(MethodInfo methodInfo)
```

Gets the test data from custom test data source.

**Parameters:**

- `methodInfo`: The method info of test method.

**Returns:** Test data for calling test method.

#### Remarks

Each element of the returned sequence represents the arguments for a single invocation of the test method. In the common case, an element is an `Object` array whose items are the positional arguments passed to the test method.

To attach per-row metadata (such as a custom display name, an ignore reason, or test categories), return a single-element `Object` array whose only item is a `TestDataRow` instance, for example `new object[] { new TestDataRow<(int, int, int)>((1, 2, 3)) { DisplayName = "my row" } }`. When MSTest sees a `TestDataRow`, it unwraps its `TestDataRow.Value` to obtain the actual test method arguments and applies the row's `TestDataRow.DisplayName`, `TestDataRow.ArgumentsDisplayName`, `TestDataRow.IgnoreMessage`, and `TestDataRow.TestCategories`.

The whole data source can be ignored (rather than a single row) by implementing `ITestDataSourceIgnoreCapability` on the data source type.

### GetDisplayName

```csharp
public virtual string? GetDisplayName(MethodInfo methodInfo, object?[]? data)
```

Gets the display name corresponding to test data row for displaying in TestResults.

**Parameters:**

- `methodInfo`: The method info of test method.
- `data`: The test data which is passed to test method.

**Returns:** The `String`.
