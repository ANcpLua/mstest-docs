# TestCategoryBaseAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

Base class for the "Category" attribute.

```csharp
[AttributeUsage(AttributeTargets.Assembly | AttributeTargets.Class | AttributeTargets.Method, AllowMultiple = true)]
public abstract class TestCategoryBaseAttribute : Attribute
```

## Remarks

The reason for this attribute is to let the users create their own implementation of test categories. - test framework (discovery, etc) deals with TestCategoryBaseAttribute. - The reason that TestCategories property is a collection rather than a string, is to give more flexibility to the user. For instance the implementation may be based on enums for which the values can be OR'ed in which case it makes sense to have single attribute rather than multiple ones on the same test.

## Constructors

### TestCategoryBaseAttribute

```csharp
protected TestCategoryBaseAttribute()
```

Initializes a new instance of the `TestCategoryBaseAttribute` class. Applies the category to the test. The strings returned by TestCategories are used with the /category command to filter tests.

## Properties

### TestCategories

```csharp
public abstract IList<string> TestCategories { get; }
```

Gets the test category that has been applied to the test.
