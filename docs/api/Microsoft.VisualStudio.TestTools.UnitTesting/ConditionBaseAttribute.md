# ConditionBaseAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

This attribute is used to conditionally control whether a test class or a test method will run or be ignored, based on a condition and using an optional message.

```csharp
[AttributeUsage(AttributeTargets.Class | AttributeTargets.Method, Inherited = false)]
public abstract class ConditionBaseAttribute : Attribute
```

## Remarks

This attribute isn't inherited. Applying it to a base class will not affect derived classes.

Whether the same condition attribute type can be applied more than once to a single test class or test method is decided by each derived attribute through its own `AttributeUsageAttribute.AllowMultiple` value:

- `MemberConditionAttribute` and `ExecutableConditionAttribute` set `AttributeUsageAttribute.AllowMultiple` to `true`. Stacked usages with distinct `ConditionBaseAttribute.GroupName` values are combined with a logical AND, while repeated usages that produce the same `ConditionBaseAttribute.GroupName` are combined with a logical OR.
- `OSConditionAttribute`, `CIConditionAttribute` and `ArchitectureConditionAttribute` set `AttributeUsageAttribute.AllowMultiple` to `false`: stacking them is a compile-time error. `OSConditionAttribute` and `ArchitectureConditionAttribute` take a flags enum, so combine the values with the bitwise OR operator instead, for example `[OSCondition(OperatingSystems.Windows \| OperatingSystems.Linux)]`. There is nothing to combine for `CIConditionAttribute`, which only carries a `ConditionMode`.

Condition attributes are grouped by their `ConditionBaseAttribute.GroupName` value, regardless of attribute type. Values within the same group are combined with a logical OR, and different groups are combined with a logical AND. The built-in condition attribute types use distinct group names for different condition kinds, so combining those different built-in kinds requires all of them to be satisfied.

## Constructors

### ConditionBaseAttribute

```csharp
protected ConditionBaseAttribute(ConditionMode mode)
```

Initializes a new instance of the `ConditionBaseAttribute` class.

**Parameters:**

- `mode`: The condition mode.

## Properties

### GroupName

```csharp
public abstract string GroupName { get; }
```

Gets the group name for this attribute. This is relevant when multiple attributes that inherit `ConditionBaseAttribute` are present. The `ConditionBaseAttribute.IsConditionMet` values of attributes in the same group are "OR"ed together. While the value from different groups is "AND"ed together. In other words, a test will be ignored if any group has all its `ConditionBaseAttribute.IsConditionMet` values as false.

#### Remarks

Usually, you can use `nameof` to return the group name.

### IgnoreMessage

```csharp
public string? IgnoreMessage { get; set; }
```

Gets or sets the ignore message indicating the reason for ignoring the test method or test class.

### IsConditionMet

```csharp
public abstract bool IsConditionMet { get; }
```

Gets a value indicating whether the condition is met. The implementation of this property shouldn't read the `ConditionBaseAttribute.Mode` property.

### Mode

```csharp
public ConditionMode Mode { get; }
```

Gets the condition mode.
