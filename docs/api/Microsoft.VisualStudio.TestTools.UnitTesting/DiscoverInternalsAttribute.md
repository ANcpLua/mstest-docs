# DiscoverInternalsAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

The presence of this attribute in a test assembly causes MSTest to discover test classes (i.e. classes having the "TestClass" attribute) and test methods (i.e. methods having the "TestMethod" attribute) which are declared internal in addition to test classes and test methods which are declared public. When this attribute is not present in a test assembly the tests in such classes will not be discovered.

```csharp
[AttributeUsage(AttributeTargets.Assembly)]
public class DiscoverInternalsAttribute : Attribute
```

## Constructors

### DiscoverInternalsAttribute

```csharp
public DiscoverInternalsAttribute()
```
