# MSTEST0043: Use retry attribute on test method

| Property                            | Value                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------------|
| **Rule ID**                         | MSTEST0043                                                                               |
| **Title**                           | Use retry attribute on test method                                                       |
| **Category**                        | Usage                                                                                    |
| **Fix is breaking or non-breaking** | Non-breaking                                                                             |
| **Enabled by default**              | Yes                                                                                      |
| **Default severity**                | Warning (escalated to Error when setting `MSTestAnalysisMode` to `Recommended` or `All`) |
| **Introduced in version**           | 3.9.0                                                                                    |
| **Is there a code fix**             | No                                                                                       |

## Cause

A method has an attribute that derives from [`RetryBaseAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/RetryBaseAttribute.md) and does not have an attribute that derives from [`TestMethodAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestMethodAttribute.md).

## Rule description

[`RetryBaseAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/RetryBaseAttribute.md) only applies to test methods.

## How to fix violations

Add [`TestMethodAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestMethodAttribute.md) to the method, or remove the [`RetryBaseAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/RetryBaseAttribute.md).

## When to suppress warnings

Do not suppress a warning from this rule.
