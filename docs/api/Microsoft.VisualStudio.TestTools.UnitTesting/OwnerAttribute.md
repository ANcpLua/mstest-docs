# OwnerAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

Test Owner.

```csharp
[AttributeUsage(AttributeTargets.Method)]
public sealed class OwnerAttribute : TestPropertyAttribute
```

## Constructors

### OwnerAttribute

```csharp
public OwnerAttribute(string? owner)
```

Initializes a new instance of the `OwnerAttribute` class.

**Parameters:**

- `owner`: The owner.

## Properties

### Owner

```csharp
public string? Owner { get; }
```

Gets the owner.
