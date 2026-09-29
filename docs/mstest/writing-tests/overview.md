# Write tests with MSTest

In this article, you learn about the APIs and conventions used by MSTest to help you write and shape your tests.

> [!NOTE]
> Attribute names ending with "Attribute" can use the short form. `TestClass` and `TestClassAttribute` are equivalent. Attributes with parameterless constructors can omit parentheses.

## Test structure

Every MSTest test class must have the `TestClass` attribute, and every test method must have the `TestMethod` attribute:

```csharp
using Microsoft.VisualStudio.TestTools.UnitTesting;

[TestClass]
public class CalculatorTests
{
    [TestMethod]
    public void Add_TwoNumbers_ReturnsSum()
    {
        // Arrange
        var calculator = new Calculator();

        // Act
        int result = calculator.Add(2, 3);

        // Assert
        Assert.AreEqual(5, result);
    }
}
```

### `TestClassAttribute`

The [`TestClassAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestClassAttribute.md) marks a class that contains tests and, optionally, initialize or cleanup methods. You can extend this attribute to customize test class behavior.

### `TestMethodAttribute`

The [`TestMethodAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestMethodAttribute.md) marks a method as a test to run. Test methods must be:

- Instance methods (not static)
- Public
- Return `void`, `Task`, or `ValueTask` (MSTest v3.3+)
- Parameterless, unless using [data-driven attributes](data-driven.md)

```csharp
[TestClass]
public class TestMethodExamples
{
    [TestMethod]
    public void SynchronousTest()
    {
        Assert.IsTrue(true);
    }

    [TestMethod]
    public async Task AsynchronousTest()
    {
        await Task.Delay(100);
        Assert.IsTrue(true);
    }
}
```

> [!WARNING]
> Don't use `async void` for test methods. Use `async Task` or `async ValueTask` instead.

### `DiscoverInternalsAttribute`

The [`DiscoverInternalsAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/DiscoverInternalsAttribute.md) assembly attribute enables MSTest to discover `internal` test classes and methods. By default, only `public` tests are discovered. This attribute is particularly useful when you have parameterized tests that use internal types as parameters:

```csharp
[assembly: DiscoverInternals]

internal record TestInput(int Value, string Description);

[TestClass]
public class CalculatorTests
{
    internal static IEnumerable<TestInput> TestData
    {
        get
        {
            yield return new TestInput(1, "one");
            yield return new TestInput(2, "two");
        }
    }

    [TestMethod]
    [DynamicData(nameof(TestData))]
    internal void Add_WithTestInput_ReturnsExpected(TestInput input)
    {
        var calculator = new Calculator();
        int result = calculator.Add(input.Value, 1);
        Assert.AreEqual(input.Value + 1, result);
    }
}
```

Without `DiscoverInternals`, the test method and its internal `TestInput` parameter type wouldn't be discovered by the test runner.

## Core concepts

MSTest documentation is organized by topic:

| Topic | Description |
|-------|-------------|
| [Assertions](assertions.md) | Verify expected results with Assert classes |
| [Data-driven testing](data-driven.md) | Run tests with multiple inputs (`DataRow`, `CombinatorialData`, `DynamicData`) |
| [Test lifecycle](lifecycle.md) | Setup and cleanup at assembly, class, and test levels |
| [Execution control](controlling-execution.md) | Threading, parallelization, timeouts, retries, and conditional execution |
| [Test organization](organizing.md) | Categories, priorities, owners, and metadata |
| [TestContext](testcontext.md) | Access test runtime information |
| [Deployment items](deployment-items.md) | Copy files and folders alongside test assemblies |

## Attribute quick reference

| Category | Attributes | See |
|----------|-----------|------|
| Test identification | `TestClass`, `TestMethod`, `DiscoverInternals` | This page |
| Data-driven | `DataRow`, `CombinatorialData`, `CombinatorialValues`, `CombinatorialRange`, `CombinatorialRandomData`, `DynamicData`, `TestDataRow` | [Data-driven testing](data-driven.md) |
| Lifecycle | `AssemblyInitialize`, `ClassInitialize`, `TestInitialize`, and cleanup counterparts | [Test lifecycle](lifecycle.md) |
| Threading | `STATestClass`, `STATestMethod` | [Execution control](controlling-execution.md) |
| Parallelization | `Parallelize`, `DoNotParallelize` | [Execution control](controlling-execution.md) |
| Timeout/Retry | `Timeout`, `Retry` | [Execution control](controlling-execution.md) |
| Conditional | `Ignore`, `OSCondition`, `CICondition` | [Execution control](controlling-execution.md) |
| Metadata | `TestCategory`, `TestProperty`, `Owner`, `Priority` | [Test organization](organizing.md) |
| Work tracking | `WorkItem`, `GitHubWorkItem` | [Test organization](organizing.md) |
| Test resources | `DeploymentItem` | [Deployment items](deployment-items.md) |

## Assertions

Use the Assert classes of the [`UnitTesting`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.testtools.unittesting?view=mstest-net-4.4) namespace to verify specific functionality. A test method exercises code in your application, but it reports correctness only when you include Assert statements.

MSTest assertions are divided into:

- **[`Assert` class](assertions.md#the-assert-class)**: General-purpose assertions (`AreEqual`, `IsTrue`, `ThrowsException`)
- **[`StringAssert` class](assertions.md#the-stringassert-class)**: String-specific assertions (`Contains`, `Matches`, `StartsWith`)
- **[`CollectionAssert` class](assertions.md#the-collectionassert-class)**: Collection assertions (`Contains`, `AllItemsAreUnique`, `AreEquivalent`)

## Testing private members

You can test private members using reflection wrapper classes:

- [`PrivateObject`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.testtools.unittesting.privateobject?view=mstest-net-4.4): For private instance methods
- [`PrivateType`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.testtools.unittesting.privatetype?view=mstest-net-4.4): For private static methods

> [!TIP]
> Consider whether private methods need direct testing. Often, testing through public interfaces provides better coverage and more maintainable tests.

## See also

- [Get started with MSTest](../getting-started/overview.md)
- [MSTest analyzers](../analyzers/overview.md)
- [Unit testing best practices](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-best-practices)
- [Run selective unit tests](../running-tests/filter.md)
