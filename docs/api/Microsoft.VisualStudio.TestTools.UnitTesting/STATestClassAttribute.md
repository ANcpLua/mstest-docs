# STATestClassAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

The test class attribute.

```csharp
[AttributeUsage(AttributeTargets.Class, Inherited = false)]
public class STATestClassAttribute : TestClassAttribute
```

## Constructors

### STATestClassAttribute

```csharp
public STATestClassAttribute()
```

## Methods

### GetTestMethodAttribute

```csharp
public override TestMethodAttribute? GetTestMethodAttribute(TestMethodAttribute testMethodAttribute)
```

Gets a test method attribute that enables running this test.

**Parameters:**

- `testMethodAttribute`: The test method attribute instance defined on this method.

**Returns:** The `TestMethodAttribute` to be used to run this test.

#### Remarks

Extensions can override this method to customize how all methods in a class are run.
