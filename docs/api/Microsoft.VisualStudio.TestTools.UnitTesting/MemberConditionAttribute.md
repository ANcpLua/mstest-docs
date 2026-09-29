# MemberConditionAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

Conditionally runs or ignores a test class or test method based on the value of one or more `static` `Boolean` members (property, field, or parameterless method) referenced by `Type` and member name.

```csharp
[AttributeUsage(AttributeTargets.Class | AttributeTargets.Method, Inherited = false, AllowMultiple = true)]
public sealed class MemberConditionAttribute : ConditionBaseAttribute
```

## Remarks

When multiple member names are supplied to a single attribute, their values are combined with a logical AND: the attribute's `MemberConditionAttribute.IsConditionMet` is `true` only if every referenced member evaluates to `true`.

Each `MemberConditionAttribute` instance forms its own `ConditionBaseAttribute.GroupName`, so stacking multiple `MemberConditionAttribute` declarations on the same target is combined with a logical AND, matching the typical `[ConditionalFact]` usage pattern in other test frameworks.

If the referenced member cannot be found as a `public` `static` `Boolean` property, field, or parameterless method, or (for methods) requires parameters, evaluating `MemberConditionAttribute.IsConditionMet` throws an `InvalidOperationException`. This surfaces as a test error rather than a silent skip so typos and refactors don't accidentally disable tests.

This attribute isn't inherited. Applying it to a base class will not affect derived classes.

```csharp
[TestMethod]
[MemberCondition(typeof(Environment), nameof(Environment.Is64BitProcess))]
public void Only_Runs_On_64Bit() { }
            
[TestMethod]
[MemberCondition(typeof(PlatformDetection),
    nameof(PlatformDetection.IsNotBrowser),
    nameof(PlatformDetection.IsThreadingSupported))]
public void Requires_Threading_And_Not_Browser() { }
            
[TestMethod]
[MemberCondition(ConditionMode.Exclude, typeof(PlatformDetection), nameof(PlatformDetection.IsMonoRuntime))]
public void Does_Not_Run_On_Mono() { }
```

## Constructors

### MemberConditionAttribute

```csharp
public MemberConditionAttribute(Type conditionType, string conditionMemberName)
```

Initializes a new instance of the `MemberConditionAttribute` class with `ConditionMode.Include` semantics: the test runs only when the referenced member evaluates to `true`.

**Parameters:**

- `conditionType`: The type declaring the static member to evaluate.
- `conditionMemberName`: The name of the `public` `static` `Boolean` member (property, field, or parameterless method) to evaluate.

```csharp
public MemberConditionAttribute(
    ConditionMode mode,
    Type conditionType,
    string conditionMemberName)
```

Initializes a new instance of the `MemberConditionAttribute` class.

**Parameters:**

- `mode`: Whether the test should be included (run when the condition is met) or excluded (skipped when the condition is met).
- `conditionType`: The type declaring the static member to evaluate.
- `conditionMemberName`: The name of the `public` `static` `Boolean` member (property, field, or parameterless method) to evaluate.

```csharp
public MemberConditionAttribute(
    Type conditionType,
    string conditionMemberName,
    params string[] additionalConditionMemberNames)
```

Initializes a new instance of the `MemberConditionAttribute` class with `ConditionMode.Include` semantics: the test runs only when every referenced member evaluates to `true`.

**Parameters:**

- `conditionType`: The type declaring the static member(s) to evaluate.
- `conditionMemberName`: The name of the first `public` `static` `Boolean` member (property, field, or parameterless method) to evaluate.
- `additionalConditionMemberNames`: Additional `public` `static` `Boolean` member name(s) to evaluate. All referenced members are AND-combined.

```csharp
public MemberConditionAttribute(
    ConditionMode mode,
    Type conditionType,
    string conditionMemberName,
    params string[] additionalConditionMemberNames)
```

Initializes a new instance of the `MemberConditionAttribute` class.

**Parameters:**

- `mode`: Whether the test should be included (run when the condition is met) or excluded (skipped when the condition is met).
- `conditionType`: The type declaring the static member(s) to evaluate.
- `conditionMemberName`: The name of the first `public` `static` `Boolean` member (property, field, or parameterless method) to evaluate.
- `additionalConditionMemberNames`: Additional `public` `static` `Boolean` member name(s) to evaluate. All referenced members are AND-combined.

## Properties

### ConditionMemberNames

```csharp
public IReadOnlyList<string> ConditionMemberNames { get; }
```

Gets the name(s) of the `static` `Boolean` member(s) (property, field, or parameterless method) on `MemberConditionAttribute.ConditionType` evaluated for this condition. Multiple values are combined with a logical AND.

### ConditionType

```csharp
public Type ConditionType { get; }
```

Gets the type declaring the `static` member(s) used to evaluate the condition.

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
