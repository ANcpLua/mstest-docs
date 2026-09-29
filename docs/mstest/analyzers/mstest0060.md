# MSTEST0060: Avoid duplicate test method attributes

| Property                            | Value                                              |
|-------------------------------------|----------------------------------------------------|
| **Rule ID**                         | MSTEST0060                                         |
| **Title**                           | Avoid duplicate test method attributes            |
| **Category**                        | Usage                                              |
| **Fix is breaking or non-breaking** | Non-breaking                                       |
| **Enabled by default**              | Yes                                                |
| **Default severity**                | Warning                                            |
| **Introduced in version**           | 4.1.0                                              |
| **Is there a code fix**             | No                                                 |

## Cause

A test method has multiple [`TestMethodAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestMethodAttribute.md) declarations.

## Rule description

A test method should have only one attribute that derives from [`TestMethodAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestMethodAttribute.md). Having multiple test method attributes (such as `[TestMethod]` and `[UITestMethod]`) on the same method causes only one attribute to be used (the first one returned by reflection), which can be confusing and lead to unintended test execution.

```csharp
[TestClass]
public class TestClass
{
    [TestMethod]
    [UITestMethod] // Violation
    public void TestMethod1()
    {
        // Test code
    }
}
```

## How to fix violations

Remove the duplicate attribute and keep only the one that matches your test method's purpose.

```csharp
[TestClass]
public class TestClass
{
    [TestMethod]
    public void TestMethod1()
    {
        // Test code
    }
}
```

## When to suppress warnings

Do not suppress warnings from this rule. Having multiple test method attributes creates ambiguous test configuration where only one attribute is used, which can cause confusion about which test behavior is actually applied.

## Suppress a warning

If you just want to suppress a single violation, add preprocessor directives to your source file to disable and then re-enable the rule.

```csharp
#pragma warning disable MSTEST0060
// The code that's violating the rule is on this line.
#pragma warning restore MSTEST0060
```

To disable the rule for a file, folder, or project, set its severity to `none` in the [configuration file](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/configuration-files).

```ini
[*.{cs,vb}]
dotnet_diagnostic.MSTEST0060.severity = none
```

For more information, see [How to suppress code analysis warnings](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/suppress-warnings).
