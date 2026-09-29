# CIConditionAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

This attribute is used to conditionally control whether a test class or a test method will run or be ignored based on whether the test is running in a CI environment.

```csharp
[AttributeUsage(AttributeTargets.Class | AttributeTargets.Method, Inherited = false, AllowMultiple = false)]
public sealed class CIConditionAttribute : ConditionBaseAttribute
```

## Remarks

This attribute isn't inherited. Applying it to a base class will not affect derived classes.

## Constructors

### CIConditionAttribute

```csharp
public CIConditionAttribute(ConditionMode mode)
```

Initializes a new instance of the `CIConditionAttribute` class.

**Parameters:**

- `mode`: Decides whether the test should be included or excluded in CI environments.

## Properties

### GroupName

```csharp
public override string GroupName { get; }
```

Gets the group name for this attribute.

### IsConditionMet

```csharp
public override bool IsConditionMet { get; }
```

Gets a value indicating whether the condition is met. The implementation of this property shouldn't read the `ConditionBaseAttribute.Mode` property.
