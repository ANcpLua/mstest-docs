# ClassInitializeAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

The class initialize attribute.

```csharp
[AttributeUsage(AttributeTargets.Method, Inherited = false)]
public sealed class ClassInitializeAttribute : Attribute
```

## Constructors

### ClassInitializeAttribute

```csharp
public ClassInitializeAttribute()
```

Initializes a new instance of the `ClassInitializeAttribute` class. ClassInitializeAttribute.

```csharp
public ClassInitializeAttribute(InheritanceBehavior inheritanceBehavior)
```

Initializes a new instance of the `ClassInitializeAttribute` class. ClassInitializeAttribute.

**Parameters:**

- `inheritanceBehavior`: Specifies the ClassInitialize Inheritance Behavior.

## Properties

### InheritanceBehavior

```csharp
public InheritanceBehavior InheritanceBehavior { get; }
```

Gets the Inheritance Behavior.
