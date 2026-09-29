# TestClassAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

This attribute is used to mark test classes.

```csharp
[AttributeUsage(AttributeTargets.Class, Inherited = false)]
public class TestClassAttribute : Attribute
```

## Remarks

Test classes must be:

- public, or if `DiscoverInternalsAttribute` is used then it can be internal.
- not static
- not generic

## Constructors

### TestClassAttribute

```csharp
public TestClassAttribute()
```

## Methods

### GetTestMethodAttribute

```csharp
public virtual TestMethodAttribute? GetTestMethodAttribute(TestMethodAttribute testMethodAttribute)
```

Gets a test method attribute that enables running this test.

**Parameters:**

- `testMethodAttribute`: The test method attribute instance defined on this method.

**Returns:** The `TestMethodAttribute` to be used to run this test.

#### Remarks

Extensions can override this method to customize how all methods in a class are run.
