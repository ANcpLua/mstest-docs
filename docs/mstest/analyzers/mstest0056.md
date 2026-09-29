# MSTEST0056: Use DisplayName property for test method display names

| Property                            | Value                                              |
|-------------------------------------|----------------------------------------------------|
| **Rule ID**                         | MSTEST0056                                         |
| **Title**                           | Use DisplayName property for test method display names |
| **Category**                        | Usage                                              |
| **Fix is breaking or non-breaking** | Non-breaking                                       |
| **Enabled by default**              | Yes                                                |
| **Default severity**                | Warning                                            |
| **Introduced in version**           | 4.0.0                                              |
| **Is there a code fix**             | Yes                                                |

## Cause

A test method attribute uses a string constructor argument instead of the [`DisplayName`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestMethodAttribute.md) property.

## Rule description

When specifying a custom display name for a test method, you should use the [`DisplayName`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestMethodAttribute.md) property instead of passing a string as a constructor argument. In MSTest 4.0 and later, the string constructor argument is used for source information (caller file path) rather than display name, which is a breaking change from MSTest 3.x. Using the `DisplayName` property ensures your code works correctly and avoids potential confusion.

```csharp
[TestClass]
public class TestClass
{
    [TestMethod("My Test Name")] // Violation
    public void TestMethod()
    {
        // Test code
    }
}
```

## How to fix violations

Replace the constructor argument with the `DisplayName` property.

```csharp
[TestClass]
public class TestClass
{
    [TestMethod(DisplayName = "My Test Name")]
    public void TestMethod()
    {
        // Test code
    }
}
```

## When to suppress warnings

Do not suppress warnings from this rule. Using the `DisplayName` property is the only way to specify custom display names for test methods. If your intent is to explicitly pass a value for the caller file path parameter instead of setting a display name, you can suppress this warning, but this is rarely needed.

## Suppress a warning

If you just want to suppress a single violation, add preprocessor directives to your source file to disable and then re-enable the rule.

```csharp
#pragma warning disable MSTEST0056
// The code that's violating the rule is on this line.
#pragma warning restore MSTEST0056
```

To disable the rule for a file, folder, or project, set its severity to `none` in the [configuration file](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/configuration-files).

```ini
[*.{cs,vb}]
dotnet_diagnostic.MSTEST0056.severity = none
```

For more information, see [How to suppress code analysis warnings](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/suppress-warnings).
