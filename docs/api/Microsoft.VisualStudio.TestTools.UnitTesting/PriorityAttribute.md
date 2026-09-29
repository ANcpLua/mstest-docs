# PriorityAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

Priority attribute; used to specify the priority of a unit test.

```csharp
[AttributeUsage(AttributeTargets.Method)]
public sealed class PriorityAttribute : TestPropertyAttribute
```

## Constructors

### PriorityAttribute

```csharp
public PriorityAttribute(int priority)
```

Initializes a new instance of the `PriorityAttribute` class.

**Parameters:**

- `priority`: The priority.

## Properties

### Priority

```csharp
public int Priority { get; }
```

Gets the priority.
