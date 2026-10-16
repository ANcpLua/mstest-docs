# DescriptionAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

Description of the test.

```csharp
[AttributeUsage(AttributeTargets.Method)]
public sealed class DescriptionAttribute : TestPropertyAttribute
```

## Constructors

### DescriptionAttribute

```csharp
public DescriptionAttribute(string? description)
```

Initializes a new instance of the `DescriptionAttribute` class to describe a test.

**Parameters:**

- `description`: The description.

## Properties

### Description

```csharp
public string? Description { get; }
```

Gets the description of a test.
