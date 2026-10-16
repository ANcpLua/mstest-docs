# MSTEST0007: Use test attributes only on test methods

| Property                            | Value                                    |
|-------------------------------------|------------------------------------------|
| **Rule ID**                         | MSTEST0007                               |
| **Title**                           | Use test attributes only on test methods |
| **Category**                        | Usage                                    |
| **Fix is breaking or non-breaking** | Non-breaking                             |
| **Enabled by default**              | Yes                                      |
| **Default severity**                | Warning starting with 4.0.0, Info before |
| **Introduced in version**           | 3.3.0                                    |
| **Is there a code fix**             | Yes                                      |

## Cause

A method that's not marked with [`TestMethodAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestMethodAttribute.md) has one or more test attributes applied to it.

## Rule description

The following test attributes should only be applied on methods marked with the [`TestMethodAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestMethodAttribute.md) attribute:

- [`ConditionBaseAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/ConditionBaseAttribute.md)
- [`CssIterationAttribute`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.testtools.unittesting.cssiterationattribute?view=mstest-net-4.5)
- [`CssProjectStructureAttribute`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.testtools.unittesting.cssprojectstructureattribute?view=mstest-net-4.5)
- [`DescriptionAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/DescriptionAttribute.md)
- [`ExpectedExceptionBaseAttribute`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.testtools.unittesting.expectedexceptionbaseattribute?view=mstest-net-4.5)
- [`OwnerAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/OwnerAttribute.md)
- [`PriorityAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/PriorityAttribute.md)
- [`TestPropertyAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestPropertyAttribute.md)
- [`WorkItemAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/WorkItemAttribute.md)

## How to fix violations

To fix a violation of this rule, either convert the method on which you applied the test attributes to a test method by setting the `[TestMethod]` attribute or remove the test attributes altogether.

## When to suppress warnings

Do not suppress a warning from this rule. If you ignore this rule, your attributes will be ignored since they are designed for use only in a test context.

## Suppress a warning

If you just want to suppress a single violation, add preprocessor directives to your source file to disable and then re-enable the rule.

```csharp
#pragma warning disable MSTEST0007
// The code that's violating the rule is on this line.
#pragma warning restore MSTEST0007
```

To disable the rule for a file, folder, or project, set its severity to `none` in the [configuration file](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/configuration-files).

```ini
[*.{cs,vb}]
dotnet_diagnostic.MSTEST0007.severity = none
```

For more information, see [How to suppress code analysis warnings](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/suppress-warnings).
