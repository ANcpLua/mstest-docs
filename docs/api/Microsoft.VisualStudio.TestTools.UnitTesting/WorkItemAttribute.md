# WorkItemAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

WorkItem attribute; used to specify a work item associated with this test.

```csharp
[AttributeUsage(AttributeTargets.Method, AllowMultiple = true)]
public class WorkItemAttribute : Attribute
```

## Constructors

### WorkItemAttribute

```csharp
public WorkItemAttribute(int id)
```

Initializes a new instance of the `WorkItemAttribute` class for the WorkItem Attribute.

**Parameters:**

- `id`: The Id to a work item.

## Properties

### Id

```csharp
public int Id { get; }
```

Gets the Id to a work item associated.
