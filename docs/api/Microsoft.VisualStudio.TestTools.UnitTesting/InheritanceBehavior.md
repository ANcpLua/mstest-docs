# InheritanceBehavior enum

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

Enumeration for inheritance behavior, that can be used with both the `ClassInitializeAttribute` class and `ClassCleanupAttribute` class. Defines the behavior of the ClassInitialize and ClassCleanup methods of base classes. The type of the enumeration must match.

```csharp
public enum InheritanceBehavior
```

## Fields

| Name | Value | Description |
| --- | --- | --- |
| `None` | `0` | None. |
| `BeforeEachDerivedClass` | `1` | Before each derived class. |
