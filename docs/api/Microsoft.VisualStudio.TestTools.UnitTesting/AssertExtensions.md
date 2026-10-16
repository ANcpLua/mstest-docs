# AssertExtensions class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

Provides That extension to Assert class.

```csharp
public static class AssertExtensions
```

## Methods

### That

```csharp
public static void That(
    Expression<Func<bool>> condition,
    string? message = null,
    [CallerArgumentExpression("condition")] string? conditionExpression = null)
```

Evaluates a boolean condition and throws an `AssertFailedException` if the condition is `false`.

**Parameters:**

- `condition`: An expression representing the condition to evaluate. Cannot be `null`.
- `message`: An optional message to include in the exception if the assertion fails.
- `conditionExpression`: The source code of the condition expression. This parameter is automatically populated by the compiler.

**Exceptions:**

- `ArgumentNullException`: Thrown if `condition` is `null`.
- `AssertFailedException`: Thrown if the evaluated condition is `false`.
