# TestDataSourceOptionsAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

Specifies options for all `ITestDataSource` of the current assembly.

```csharp
[AttributeUsage(AttributeTargets.Assembly, Inherited = false)]
public sealed class TestDataSourceOptionsAttribute : Attribute
```

## Remarks

These options can be override by individual `ITestDataSource` attribute.

## Constructors

### TestDataSourceOptionsAttribute

```csharp
public TestDataSourceOptionsAttribute(TestDataSourceUnfoldingStrategy unfoldingStrategy)
```

Initializes a new instance of the `TestDataSourceOptionsAttribute` class.

**Parameters:**

- `unfoldingStrategy`: The `TestDataSourceOptionsAttribute.UnfoldingStrategy` to use when executing parameterized tests.

## Properties

### UnfoldingStrategy

```csharp
public TestDataSourceUnfoldingStrategy UnfoldingStrategy { get; }
```

Gets the test unfolding strategy.
