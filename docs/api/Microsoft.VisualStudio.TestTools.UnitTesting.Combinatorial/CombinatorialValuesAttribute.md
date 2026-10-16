# CombinatorialValuesAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting.Combinatorial`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

Specifies the values for a parameter on a combinatorial test method.

```csharp
[AttributeUsage(AttributeTargets.Parameter)]
public sealed class CombinatorialValuesAttribute : Attribute, ICombinatorialValuesProvider
```

## Constructors

### CombinatorialValuesAttribute

```csharp
public CombinatorialValuesAttribute(params object?[]? values)
```

Initializes a new instance of the `CombinatorialValuesAttribute` class.

**Parameters:**

- `values`: The values to pass to this parameter.

## Properties

### Values

```csharp
public object?[] Values { get; }
```

Gets the values that should be passed to this parameter.

## Methods

### GetValues

```csharp
public object?[] GetValues(ParameterInfo parameter)
```

Gets the values that should be passed to the parameter.

**Parameters:**

- `parameter`: The parameter to get values for.

**Returns:** An array of values.
