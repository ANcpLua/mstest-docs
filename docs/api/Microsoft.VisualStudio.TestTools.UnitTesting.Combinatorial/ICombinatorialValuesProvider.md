# ICombinatorialValuesProvider interface

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting.Combinatorial`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

Provides values for a parameter on a combinatorial test method.

```csharp
public interface ICombinatorialValuesProvider
```

## Methods

### GetValues

```csharp
object?[] GetValues(ParameterInfo parameter)
```

Gets the values that should be passed to the parameter.

**Parameters:**

- `parameter`: The parameter to get values for.

**Returns:** An array of values.
