# MSTEST0041: Use 'ConditionBaseAttribute' on test classes

| Property                            | Value                                                                  |
|-------------------------------------|------------------------------------------------------------------------|
| **Rule ID**                         | MSTEST0041                                                             |
| **Title**                           | Use 'ConditionBaseAttribute' on test classes                           |
| **Category**                        | Usage                                                                  |
| **Fix is breaking or non-breaking** | Non-breaking                                                           |
| **Enabled by default**              | Yes                                                                    |
| **Default severity**                | Warning                                                                |
| **Introduced in version**           | 3.8.0                                                                  |
| **Is there a code fix**             | Yes, starting with MSTest 4.4                                          |

## Cause

The use of an attribute that inherits from [`ConditionBaseAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/ConditionBaseAttribute.md) on a class that is not marked with [`TestClassAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestClassAttribute.md).

## Rule description

An attribute that derives from [`ConditionBaseAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/ConditionBaseAttribute.md) only has an effect when applied to a class that's marked with [`TestClassAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestClassAttribute.md).

## How to fix violations

Depending on the intent, either add the missing [`TestClassAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestClassAttribute.md) or remove the attribute that derives from [`ConditionBaseAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/ConditionBaseAttribute.md).

Starting with MSTest 4.4, the code fix adds `[TestClass]` to the affected type.

## When to suppress warnings

Do not suppress a warning from this rule.
