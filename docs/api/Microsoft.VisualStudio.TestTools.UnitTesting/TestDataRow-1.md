# TestDataRow<T> class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

When this type is returned from `ITestDataSource.GetData(MethodInfo)` (for example, through `DynamicDataAttribute`), it determines information related to the specific test case.

```csharp
public sealed class TestDataRow<T>
```

**Type parameters:**

- `T`: The type parameter corresponding to the type of the value held by this type. It can be a tuple for test methods with more than one parameter.

## Remarks

To use this type from a custom `ITestDataSource`, wrap each instance in a single-element `Object` array, for example `new object[] { new TestDataRow<int>(42) { DisplayName = "my row" } }`. MSTest unwraps the `TestDataRow.Value` to obtain the test method arguments and applies the `TestDataRow.DisplayName`, `TestDataRow.IgnoreMessage`, and `TestDataRow.TestCategories` metadata to the generated test case.

## Constructors

### TestDataRow

```csharp
public TestDataRow(T? value)
```

Initializes a new instance of the `TestDataRow` class.

**Parameters:**

- `value`: The value to be held by this instance, which could be a `Tuple` or `ValueTuple` if the test method has more than one parameter.

## Properties

### DisplayName

```csharp
public string? DisplayName { get; set; }
```

Gets or sets the display name for the test case.

### IgnoreMessage

```csharp
public string? IgnoreMessage { get; set; }
```

Gets or sets the ignore message. A non-null value means the test case is ignored with the message provided.

### TestCategories

```csharp
public IList<string>? TestCategories { get; set; }
```

Gets or sets the test categories for the test case.

### Value

```csharp
public T? Value { get; }
```

Gets the value held by this instance.
