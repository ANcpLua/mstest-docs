# OSConditionAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

This attribute is used to ignore a test class or a test method, with an optional message.

```csharp
[AttributeUsage(AttributeTargets.Class | AttributeTargets.Method, Inherited = false, AllowMultiple = false)]
public sealed class OSConditionAttribute : ConditionBaseAttribute
```

## Remarks

This attribute isn't inherited. Applying it to a base class will not cause derived classes to be ignored.

## Constructors

### OSConditionAttribute

```csharp
public OSConditionAttribute(OperatingSystems operatingSystems)
```

Initializes a new instance of the `OSConditionAttribute` class.

**Parameters:**

- `operatingSystems`: The operating systems that this test supports.

```csharp
public OSConditionAttribute(ConditionMode mode, OperatingSystems operatingSystems)
```

Initializes a new instance of the `OSConditionAttribute` class.

**Parameters:**

- `mode`: Decides whether the OSes will be included or excluded.
- `operatingSystems`: The operating systems that this test includes/excludes.

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
