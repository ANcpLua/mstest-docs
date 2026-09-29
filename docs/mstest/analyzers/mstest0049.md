# MSTEST0049: Flow TestContext cancellation token

| Property                            | Value                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------------|
| **Rule ID**                         | MSTEST0049                                                                               |
| **Title**                           | Flow TestContext cancellation token                                                     |
| **Category**                        | Usage                                                                                    |
| **Fix is breaking or non-breaking** | Non-breaking                                                                             |
| **Enabled by default**              | Yes                                                                                      |
| **Default severity**                | Info                                                                                     |
| **Introduced in version**           | 3.10.0                                                                                   |
| **Is there a code fix**             | Yes                                                                                      |

## Cause

A method call within a test context doesn't use the [`CancellationToken`](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken) available from [`TestContext`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) when the called method has a parameter or overload that accepts a [`CancellationToken`](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken).

## Rule description

When [`TestContext`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) is available in your test methods, you should flow its [`CancellationToken`](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken) to async operations. This enables cooperative cancellation when timeouts occur and ensures proper resource cleanup. The [`TestContext`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) cancellation token is especially important when using cooperative cancellation with timeout attributes.

This rule triggers when:

- A method call has an optional [`CancellationToken`](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken) parameter that isn't explicitly provided.
- A method call has an overload that accepts a [`CancellationToken`](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken) but the non-cancellable overload is used instead.

## How to fix violations

Use the provided code fixer to automatically pass the [`CancellationToken`](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken) from [`TestContext`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) to method calls that support cancellation. You can also manually update method calls to include `TestContext.CancellationToken` as a parameter.

### Example: TestContext property

The following code triggers MSTEST0049 because `Task.Delay` and `HttpClient.GetAsync` accept a [`CancellationToken`](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken) but none is passed:

```csharp
[TestClass]
public class MyTestClass
{
    public TestContext TestContext { get; set; }

    [TestMethod]
    public async Task TestMethod()
    {
        using var client = new HttpClient();
        // MSTEST0049: these calls accept a CancellationToken but none is passed
        await Task.Delay(1000);
        var response = await client.GetAsync("https://example.com");
    }
}
```

The fix is to pass `TestContext.CancellationToken` to each call:

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

### Example: constructor injection (MSTest 3.6+)

With constructor injection, use the `_testContext` field to access the cancellation token:

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

## When to suppress warnings

Suppress this warning if you intentionally don't want to support cancellation for specific operations, or if the operation should continue even when the test is cancelled.

## Suppress a warning

If you just want to suppress a single violation, add preprocessor directives to your source file to disable and then re-enable the rule.

```csharp
#pragma warning disable MSTEST0049
// The code that's violating the rule is on this line.
#pragma warning restore MSTEST0049
```

To disable the rule for a file, folder, or project, set its severity to `none` in the [configuration file](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/configuration-files).

```ini
[*.{cs,vb}]
dotnet_diagnostic.MSTEST0049.severity = none
```

For more information, see [How to suppress code analysis warnings](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/suppress-warnings).
