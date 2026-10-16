# ArchitectureConditionAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

This attribute is used to ignore a test class or a test method based on the current process architecture.

```csharp
[AttributeUsage(AttributeTargets.Class | AttributeTargets.Method, Inherited = false, AllowMultiple = false)]
public sealed class ArchitectureConditionAttribute : ConditionBaseAttribute
```

## Remarks

This attribute isn't inherited. Applying it to a base class will not cause derived classes to be ignored. It can be combined with `OSConditionAttribute` (or any other condition attribute) to gate a test on both the operating system and the process architecture, because condition attributes that expose a different `ConditionBaseAttribute.GroupName` are combined with a logical AND.

## Constructors

### ArchitectureConditionAttribute

```csharp
public ArchitectureConditionAttribute(TestArchitectures architectures)
```

Initializes a new instance of the `ArchitectureConditionAttribute` class.

**Parameters:**

- `architectures`: The process architectures that this test supports.

```csharp
public ArchitectureConditionAttribute(ConditionMode mode, TestArchitectures architectures)
```

Initializes a new instance of the `ArchitectureConditionAttribute` class.

**Parameters:**

- `mode`: Decides whether the architectures will be included or excluded.
- `architectures`: The process architectures that this test includes/excludes.

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

Gets a value indicating whether the test method or test class should be ignored.
