# Order unit tests

Occasionally, you may want to have unit tests run in a specific order. Ideally, the order in which unit tests run should _not_ matter, and it is [best practice](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-best-practices) to avoid ordering unit tests. Regardless, there may be a need to do so. In that case, this article demonstrates how to order test runs.

> [!NOTE]
> Test ordering and test parallelization are separate concerns. Specifying an execution order determines the sequence in which tests start, but if parallelization is enabled, multiple tests can still run concurrently. To guarantee that tests run one at a time in the specified order, you must also disable parallelization.

If you prefer to browse the source code, see the [order .NET Core unit tests](https://learn.microsoft.com/en-us/samples/dotnet/samples/order-unit-tests-cs) sample repository.

> [!TIP]
> In addition to the ordering capabilities outlined in this article, consider [creating custom playlists with Visual Studio](https://learn.microsoft.com/en-us/visualstudio/test/run-unit-tests-with-test-explorer#create-custom-playlists) as an alternative.

## Order alphabetically

> [!NOTE]
> MSTest runs tests sequentially within a class by default. If you configure parallelism using the `<Parallelize>` setting in a `.runsettings` file, tests across classes can run concurrently, and ordering affects only the sequence within each class. For all ways to enable or disable MSTest parallelization, see [Configure parallelization](controlling-execution.md#configure-parallelization).

MSTest discovers tests in the same order in which they are defined in the test class.

When running through Test Explorer (in Visual Studio, or in Visual Studio Code), the tests are ordered in alphabetical order based on their test name.

When running outside of Test Explorer, tests are executed in the order in which they are defined in the test class.

> [!NOTE]
> A test named `Test14` will run before `Test2` even though the number  `2` is less than `14`. This is because test name ordering uses the text name of the test.

```csharp
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace MSTest.Project;

[TestClass]
public class ByAlphabeticalOrder
{
    public static bool Test1Called;
    public static bool Test2Called;
    public static bool Test3Called;

    [TestMethod]
    public void Test2()
    {
        Test2Called = true;

        Assert.IsTrue(Test1Called);
        Assert.IsFalse(Test3Called);
    }

    [TestMethod]
    public void Test1()
    {
        Test1Called = true;

        Assert.IsFalse(Test2Called);
        Assert.IsFalse(Test3Called);
    }

    [TestMethod]
    public void Test3()
    {
        Test3Called = true;

        Assert.IsTrue(Test1Called);
        Assert.IsTrue(Test2Called);
    }
}
```

Starting with MSTest 3.6, a new runsettings option lets you run tests by test names both in Test Explorers and on the command line. To enable this feature, add the `OrderTestsByNameInClass` setting to your runsettings file:

```xml
<?xml version="1.0" encoding="utf-8"?>
<RunSettings>

  <MSTest>
    <OrderTestsByNameInClass>true</OrderTestsByNameInClass>
  </MSTest>

</RunSettings>
```

## Order randomly

In MSTest 4.3 and later, run tests in a random order to surface hidden ordering dependencies between tests. To enable random order, set the `RandomizeTestOrder` setting to **true** in your runsettings file:

```xml
<?xml version="1.0" encoding="utf-8"?>
<RunSettings>

  <MSTest>
    <RandomizeTestOrder>true</RandomizeTestOrder>
  </MSTest>

</RunSettings>
```

To make the random order reproducible, set the `RandomTestOrderSeed` setting to an integer seed. MSTest then replays the same order on every run. When you leave the seed unset, MSTest generates a new seed for each run. Don't combine `RandomizeTestOrder` with `OrderTestsByNameInClass`, because MSTest applies only one ordering mode at a time. For more information, see [Configure MSTest](../running-tests/configure.md).

## Next steps

> [Unit test code coverage](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-code-coverage)
