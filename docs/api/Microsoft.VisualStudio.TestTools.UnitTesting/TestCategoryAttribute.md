# TestCategoryAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

TestCategory attribute; used to specify the category of a unit test.

```csharp
[AttributeUsage(AttributeTargets.Assembly | AttributeTargets.Class | AttributeTargets.Method, AllowMultiple = true)]
public sealed class TestCategoryAttribute : TestCategoryBaseAttribute
```

## Constructors

### TestCategoryAttribute

```csharp
public TestCategoryAttribute(string testCategory)
```

Initializes a new instance of the `TestCategoryAttribute` class and applies the category to the test.

**Parameters:**

- `testCategory`: The test Category.

## Properties

### TestCategories

```csharp
public override IList<string> TestCategories { get; }
```

Gets the test categories that has been applied to the test.
