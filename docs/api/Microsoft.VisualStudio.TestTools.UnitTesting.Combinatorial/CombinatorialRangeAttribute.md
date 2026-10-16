# CombinatorialRangeAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting.Combinatorial`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

Specifies a range of values for a parameter on a combinatorial test method.

```csharp
[AttributeUsage(AttributeTargets.Parameter)]
public sealed class CombinatorialRangeAttribute : Attribute, ICombinatorialValuesProvider
```

## Constructors

### CombinatorialRangeAttribute

```csharp
public CombinatorialRangeAttribute(int from, int count)
```

Initializes a new instance of the `CombinatorialRangeAttribute` class.

**Parameters:**

- `from`: The value at the beginning of the range.
- `count`: The positive number of consecutive values to include.

```csharp
public CombinatorialRangeAttribute(uint from, uint count)
```

Initializes a new instance of the `CombinatorialRangeAttribute` class.

**Parameters:**

- `from`: The value at the beginning of the range.
- `count`: The positive number of consecutive values to include.

```csharp
public CombinatorialRangeAttribute(
    int from,
    int to,
    int step)
```

Initializes a new instance of the `CombinatorialRangeAttribute` class.

**Parameters:**

- `from`: The value at the beginning of the range.
- `to`: The inclusive value at the end of the range.
- `step`: The non-zero amount by which each value changes.

```csharp
public CombinatorialRangeAttribute(
    uint from,
    uint to,
    uint step)
```

Initializes a new instance of the `CombinatorialRangeAttribute` class.

**Parameters:**

- `from`: The value at the beginning of the range.
- `to`: The inclusive value at the end of the range.
- `step`: The positive amount by which each value changes.

## Methods

### GetValues

```csharp
public object[] GetValues(ParameterInfo parameter)
```

Gets the values that should be passed to the parameter.

**Parameters:**

- `parameter`: The parameter to get values for.

**Returns:** An array of values.
