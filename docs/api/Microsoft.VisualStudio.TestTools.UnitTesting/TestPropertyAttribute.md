# TestPropertyAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

The test property attribute.

```csharp
[AttributeUsage(AttributeTargets.Class | AttributeTargets.Method, AllowMultiple = true)]
public class TestPropertyAttribute : Attribute
```

## Constructors

### TestPropertyAttribute

```csharp
public TestPropertyAttribute(string name, string value)
```

Initializes a new instance of the `TestPropertyAttribute` class.

**Parameters:**

- `name`: The name.
- `value`: The value.

## Properties

### Name

```csharp
public string Name { get; }
```

Gets the name.

### Value

```csharp
public string Value { get; }
```

Gets the value.
