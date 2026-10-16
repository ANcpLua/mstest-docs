# IgnoreAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

This attribute is used to ignore a test class or a test method, with an optional message.

```csharp
[AttributeUsage(AttributeTargets.Class | AttributeTargets.Method, Inherited = false)]
public sealed class IgnoreAttribute : ConditionBaseAttribute
```

## Remarks

This attribute isn't inherited. Applying it to a base class will not cause derived classes to be ignored.

## Constructors

### IgnoreAttribute

```csharp
public IgnoreAttribute()
```

Initializes a new instance of the `IgnoreAttribute` class with an empty message.

```csharp
public IgnoreAttribute(string? message)
```

Initializes a new instance of the `IgnoreAttribute` class.

**Parameters:**

- `message`: Message specifies reason for ignoring.

## Properties

### GroupName

```csharp
public override string GroupName { get; }
```

Gets the group name for this attribute. This is relevant when multiple attributes that inherit `ConditionBaseAttribute` are present. The `ConditionBaseAttribute.IsConditionMet` values of attributes in the same group are "OR"ed together. While the value from different groups is "AND"ed together. In other words, a test will be ignored if any group has all its `ConditionBaseAttribute.IsConditionMet` values as false.

#### Remarks

Usually, you can use `nameof` to return the group name.

### IsConditionMet

```csharp
public override bool IsConditionMet { get; }
```

Gets a value indicating whether the condition is met. The implementation of this property shouldn't read the `ConditionBaseAttribute.Mode` property.
