# GlobalTestInitializeAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

A global test initialize attribute that applies to every test method in the assembly. The method to which this attribute is applied must be public, static, non-generic, has a single parameter of type TestContext, and either returns void or a Task.

```csharp
[AttributeUsage(AttributeTargets.Method, AllowMultiple = false, Inherited = false)]
public sealed class GlobalTestInitializeAttribute : Attribute
```

## Remarks

Multiple methods with this attribute in the assembly is allowed, but there is no guarantee of the order in which they will be executed.

## Constructors

### GlobalTestInitializeAttribute

```csharp
public GlobalTestInitializeAttribute()
```
