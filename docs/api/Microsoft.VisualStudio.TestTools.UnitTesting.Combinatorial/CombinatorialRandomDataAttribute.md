# CombinatorialRandomDataAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting.Combinatorial`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

Specifies randomly generated integer values for a parameter on a combinatorial test method.

```csharp
[AttributeUsage(AttributeTargets.Parameter)]
public sealed class CombinatorialRandomDataAttribute : Attribute, ICombinatorialValuesProvider
```

## Constructors

### CombinatorialRandomDataAttribute

```csharp
public CombinatorialRandomDataAttribute()
```

Initializes a new instance of the `CombinatorialRandomDataAttribute` class.

## Fields

### NoSeed

```csharp
public const int NoSeed = 0
```

Specifies that `Random` should choose its own seed.

## Properties

### Count

```csharp
public int Count { get; set; }
```

Gets or sets the positive number of values to generate.

### Maximum

```csharp
public int Maximum { get; set; }
```

Gets or sets the maximum value, inclusive.

### Minimum

```csharp
public int Minimum { get; set; }
```

Gets or sets the minimum value, inclusive.

### Seed

```csharp
public int Seed { get; set; }
```

Gets or sets the seed used for random number generation.

## Methods

### GetValues

```csharp
public object[] GetValues(ParameterInfo parameter)
```

Gets the values that should be passed to the parameter.

**Parameters:**

- `parameter`: The parameter to get values for.

**Returns:** An array of values.
