# ClassCleanupAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

The class cleanup attribute.

```csharp
[AttributeUsage(AttributeTargets.Method, Inherited = false)]
public sealed class ClassCleanupAttribute : Attribute
```

## Constructors

### ClassCleanupAttribute

```csharp
public ClassCleanupAttribute()
```

Initializes a new instance of the `ClassCleanupAttribute` class.

```csharp
public ClassCleanupAttribute(InheritanceBehavior inheritanceBehavior)
```

Initializes a new instance of the `ClassCleanupAttribute` class.

**Parameters:**

- `inheritanceBehavior`: Specifies the ClassCleanup Inheritance Behavior.

## Properties

### InheritanceBehavior

```csharp
public InheritanceBehavior InheritanceBehavior { get; }
```

Gets the Inheritance Behavior.
