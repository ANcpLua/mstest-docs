# TestMethodAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

This attribute is used to mark test methods.

```csharp
[AttributeUsage(AttributeTargets.Method, Inherited = false)]
public class TestMethodAttribute : Attribute
```

## Remarks

- When using other attributes like `DataRowAttribute` or `DynamicDataAttribute`, the use of `TestMethodAttribute` is still required.
- Test methods must be: - public, or if `DiscoverInternalsAttribute` is used then it can be internal. - not static - not generic - not abstract - return type is either `void`, `Task`, or `ValueTask`. If `void`, then it shouldn't be `async`.

## Constructors

### TestMethodAttribute

```csharp
public TestMethodAttribute([CallerFilePath] string callerFilePath = "", [CallerLineNumber] int callerLineNumber = -1)
```

Initializes a new instance of the `TestMethodAttribute` class.

## Properties

### DeclaringFilePath

```csharp
public string DeclaringFilePath { get; }
```

Gets the file path that declares the attribute.

### DeclaringLineNumber

```csharp
public int? DeclaringLineNumber { get; }
```

Gets the line number within `TestMethodAttribute.DeclaringFilePath` that declares the attribute.

### DisplayName

```csharp
public string? DisplayName { get; set; }
```

Gets or sets display name for the test.

### UnfoldingStrategy

```csharp
public TestDataSourceUnfoldingStrategy UnfoldingStrategy { get; set; }
```

Gets or sets the strategy for unfolding parameterized tests.

## Methods

### ExecuteAsync

```csharp
public virtual Task<TestResult[]> ExecuteAsync(ITestMethod testMethod)
```

Executes a test method.

**Parameters:**

- `testMethod`: The test method to execute.

**Returns:** An array of TestResult objects that represent the outcome(s) of the test.

#### Remarks

Extensions can override this method to customize running a TestMethod.
