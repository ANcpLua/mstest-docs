# The `TestContext` class

The [`TestContext`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) class gives useful information and tools to help manage test execution. It lets you access details about the test run and adjust the test environment. This class is part of the [`UnitTesting`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.testtools.unittesting?view=mstest-net-4.5) namespace.

## Accessing the `TestContext` object

The [`TestContext`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) object is available in the following contexts:

- As a parameter to [AssemblyInitialize](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/AssemblyInitializeAttribute.md), the [ClassInitialize](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/ClassInitializeAttribute.md) methods. In this context, the properties related to the test run are not available.
- Starting with 3.6, optionally, as a parameter to [AssemblyCleanup](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/AssemblyCleanupAttribute.md), the [ClassCleanup](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/ClassCleanupAttribute.md) methods. In this context, the properties related to the test run are not available.
- As a property of a test class. In this context, the properties related to the test run are available.
- As a constructor parameter of a test class (starting with v3.6). This way is recommended over using the property, because it gives access to the object in the constructor. While the property is only available after the constructor has run. This way also helps to ensure immutability of the object and allows the compiler to enforce that the object is not null.

```csharp
using Microsoft.VisualStudio.TestTools.UnitTesting;

[TestClass]
public class MyTestClassTestContext
{
    public TestContext TestContext { get; set; }

    [AssemblyInitialize]
    public static void AssemblyInitialize(TestContext context)
    {
        // Access TestContext properties and methods here. The properties related to the test run are not available.
    }

    [ClassInitialize]
    public static void ClassInitialize(TestContext context)
    {
        // Access TestContext properties and methods here. The properties related to the test run are not available.
    }

    [TestMethod]
    public void MyTestMethod()
    {
        // Access TestContext properties and methods here
    }
}
```

Or with MSTest 3.6+:

```csharp
using Microsoft.VisualStudio.TestTools.UnitTesting;

[TestClass]
public class MyTestClassTestContextThroughCtor
{
    private readonly TestContext _testContext;

    public MyTestClassTestContextThroughCtor(TestContext testContext)
    {
        _testContext = testContext;
    }

    [AssemblyInitialize]
    public static void AssemblyInitialize(TestContext context)
    {
        // Access TestContext properties and methods here. The properties related to the test run are not available.
    }

    [ClassInitialize]
    public static void ClassInitialize(TestContext context)
    {
        // Access TestContext properties and methods here. The properties related to the test run are not available.
    }

    [TestMethod]
    public void MyTestMethod()
    {
        // Access TestContext properties and methods here
    }
}
```

## The `TestContext` members

The [`TestContext`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) class provides properties about the test run along with methods to manipulate the test environment. This section covers the most commonly used properties and methods.

### Test run information

The [`TestContext`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) provides information about the test run, such as:

- [`TestContext.TestName`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) – the name of the currently executing test.
- [`TestContext.CurrentTestOutcome`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) - the result of the current test.
- [`TestContext.FullyQualifiedTestClassName`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) - the full name of the test class.
- [`TestContext.TestRunDirectory`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) - the directory where the test run is executed.
- [`TestContext.DeploymentDirectory`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) - the directory where the deployment items are located. To populate this directory, use [`DeploymentItemAttribute`](deployment-items.md).
- [`TestContext.ResultsDirectory`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) - the directory where the test results are stored.  Typically a subdirectory of the [`TestContext.TestRunDirectory`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md).
- [`TestContext.TestRunResultsDirectory`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) - the directory where the test results are stored. Typically a subdirectory of the [`TestContext.ResultsDirectory`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md).
- [`TestContext.TestResultsDirectory`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) - the directory where the test results are stored. Typically a subdirectory of the [`TestContext.ResultsDirectory`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md).
- Starting with MSTest 3.9, [`TestContext.TestRunCount`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) - the number of times the current test has run, counting from 1. The value is greater than 1 when a test is retried with `[Retry]`.

### Per-test temporary directory

Use `TestContext.TestTempDirectory` as private scratch space for a test. MSTest creates the directory only when you first access the property, and each test execution receives a unique directory. Each data row also receives its own directory, so parallel tests don't share paths.

```csharp
string path = Path.Combine(TestContext.TestTempDirectory!, "output.json");
File.WriteAllText(path, json);
```

MSTest creates the directory under `TestResultsDirectory` when possible and falls back to the system temporary directory when the results path is unavailable, too long, or read-only. MSTest deletes the directory after a passing test and retains it after any non-passing outcome. Set the `MSTEST_TEST_TEMP_DIRECTORY_RETAIN` environment variable to `1` or `true` to retain directories for all outcomes.

When a passing test registers a file from the directory with `AddResultFile`, MSTest retains the directory until the host collects the attachment. Cleanup is best effort and doesn't change the test outcome.

`TestTempDirectory` is available for .NET and .NET Framework targets, but not for UWP or WinUI targets. The property doesn't change the process current directory.

In MSTest 3.7 and later, the [`TestContext`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) class also provides new properties helpful for `TestInitialize` and `TestCleanup` methods:

- [`TestContext.TestData`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) - the data that will be provided to the parameterized test method, or `null` if the test is not parameterized.
- [`TestContext.TestDisplayName`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) - the display name of the test method.
- [`TestContext.TestException`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) - the exception thrown by either the test method or test initialize, or `null` if the test method did not throw an exception.

### Data-driven tests

In MSTest 3.7 and later, the property [`TestContext.TestData`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) can be used to access the data for the current test during `TestInitialize` and `TestCleanup` methods.

When targeting .NET framework, the [`TestContext`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) enables you to retrieve and set data for each iteration in a data-driven test, using properties like `DataRow` and `DataConnection` (for [DataSource](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/DataSourceAttribute.md)-based tests).

Consider the following CSV file `TestData.csv`:

```csv
Number,Name
1,TestValue1
2,TestValue2
3,TestValue3
```

You can use the `DataSource` attribute to read the data from the CSV file:

```csharp
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;

namespace YourNamespace
{
    [TestClass]
    public class CsvDataDrivenTest
    {
        public TestContext TestContext { get; set; }

        [TestMethod]
        [DataSource(
            "Microsoft.VisualStudio.TestTools.DataSource.CSV",
            "|DataDirectory|\\TestData.csv",
            "TestData#csv",
            DataAccessMethod.Sequential)]
        public void TestWithCsvDataSource()
        {
            // Access data from the current row
            int number = Convert.ToInt32(TestContext.DataRow["Number"]);
            string name = TestContext.DataRow["Name"].ToString();

            Console.WriteLine($"Number: {number}, Name: {name}");

            // Example assertions or logic
            Assert.IsTrue(number > 0);
            Assert.IsFalse(string.IsNullOrEmpty(name));
        }
    }
}
```

### Store and retrieve runtime data

You can use [`TestContext.Properties`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) to store custom key-value pairs that can be accessed across different methods in the same test session.

Starting with MSTest 4.4, the indexer consistently returns `null` when a custom key doesn't exist.

```csharp
TestContext.Properties["MyKey"] = "MyValue";
string value = TestContext.Properties["MyKey"]?.ToString();
```

> [!NOTE]
> Starting with MSTest 4.2, test categories from `[TestCategory]` are included in [`TestContext.Properties`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md).
>
> Starting with MSTest 4.3, custom properties added to `TestContext.Properties` in `[AssemblyInitialize]` flow to every class and test in the assembly, and properties added in `[ClassInitialize]` flow to every test in that class. This lets fixtures publish shared context that test methods can read.
>
> Starting with MSTest 4.3.3, `[TestProperty]` values, test categories, host-provided properties, and properties that a test adds remain scoped to that test and don't flow to sibling tests.

### Access `TestContext` from the current call stack

Starting with MSTest 4.2, [`TestContext.Current`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) returns the current test's [`TestContext`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) from anywhere in the call stack during test method execution. This API is experimental, uses the `[Experimental]` attribute, and might change in a future MSTest version.

### Associate data to a test

The [`TestContext.AddResultFile`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) method allows you to add a file to the test results, making it available for review in the test output. This can be useful if you generate files during your test (for example, log files, screenshots, or data files) that you want to attach to the test results.

```csharp
using Microsoft.VisualStudio.TestTools.UnitTesting;

[TestClass]
public class TestClassResultFile
{
    public TestContext TestContext { get; set; }

    [TestMethod]
    public void TestMethodWithResultFile()
    {
        // Simulate creating a log file for this test
        string logFilePath = Path.Combine(TestContext.TestRunDirectory, "TestLog.txt");
        File.WriteAllText(logFilePath, "This is a sample log entry for the test.");

        // Add the log file to the test result
        TestContext.AddResultFile(logFilePath);

        // Perform some assertions (example only)
        Assert.IsTrue(File.Exists(logFilePath), "The log file was not created.");
        Assert.IsTrue(new FileInfo(logFilePath).Length > 0, "The log file is empty.");
    }
}
```

Starting with MSTest 4.5, the native MTP adapter preserves these result files as test attachments so MTP report extensions can include them.

You can also use [`TestContext.Write`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) or [`TestContext.WriteLine`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) methods to write custom messages directly to the test output. Starting with MSTest 4.4, the `Live` output capture mode echoes these messages while the test runs and still attaches them to the final test result. For more information, see [Configure MSTest output](../running-tests/configure.md#output-settings).

### Cancellation token

The [`TestContext`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) exposes a [`CancellationToken`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) property that is signaled when the test times out or the test run is aborted. You should pass this token to async operations so that they can respond to cancellation cooperatively. This is especially important when using [Timeout](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TimeoutAttribute.md) attributes.

When [`TestContext`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) is accessed as a property:

```csharp
using Microsoft.VisualStudio.TestTools.UnitTesting;

[TestClass]
public class TestClassCancellationToken
{
    // MSTest automatically sets the TestContext property before each test runs.
    // MSTest.Analyzers includes a diagnostic suppressor that removes CS8618
    // (non-nullable property uninitialized) for this property.
    public TestContext TestContext { get; set; }

    [TestMethod]
    [Timeout(5000, CooperativeCancellation = true)]
    public async Task MyAsyncTest()
    {
        using var client = new HttpClient();
        var response = await client.GetAsync(
            "https://example.com", TestContext.CancellationToken);

        Assert.IsTrue(response.IsSuccessStatusCode);
    }
}
```

When [`TestContext`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) is injected through the constructor (MSTest 3.6+):

```csharp
using Microsoft.VisualStudio.TestTools.UnitTesting;

[TestClass]
public class TestClassCancellationTokenCtor
{
    private readonly TestContext _testContext;

    public TestClassCancellationTokenCtor(TestContext testContext)
    {
        _testContext = testContext;
    }

    [TestMethod]
    [Timeout(5000, CooperativeCancellation = true)]
    public async Task MyAsyncTest()
    {
        using var client = new HttpClient();
        var response = await client.GetAsync(
            "https://example.com", _testContext.CancellationToken);

        Assert.IsTrue(response.IsSuccessStatusCode);
    }
}
```

> [!TIP]
> MSTest analyzer rule [MSTEST0049](../analyzers/mstest0049.md) helps identify async calls where `TestContext.CancellationToken` should be passed. It also provides a code fixer to apply the change automatically.

## Related analyzers

The following analyzers help ensure proper usage of the `TestContext` class:

- [MSTEST0005](../analyzers/mstest0005.md) - TestContext property should have valid layout.
- [MSTEST0024](../analyzers/mstest0024.md) - Do not store TestContext in a static member.
- [MSTEST0033](../analyzers/mstest0033.md) - Suppresses CS8618 for TestContext property.
- [MSTEST0048](../analyzers/mstest0048.md) - Avoid TestContext properties in fixture methods.
- [MSTEST0049](../analyzers/mstest0049.md) - Flow TestContext CancellationToken.
- [MSTEST0054](../analyzers/mstest0054.md) - Use CancellationToken property.
