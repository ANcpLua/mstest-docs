# TestCleanupAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

The test cleanup attribute marks methods that are executed after every test marked with a `TestMethodAttribute`.

```csharp
[AttributeUsage(AttributeTargets.Method, Inherited = false)]
public sealed class TestCleanupAttribute : Attribute
```

## Constructors

### TestCleanupAttribute

```csharp
public TestCleanupAttribute()
```
