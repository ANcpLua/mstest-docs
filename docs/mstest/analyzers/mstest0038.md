# MSTEST0038: Don't use 'Assert.AreSame' or 'Assert.AreNotSame' with value types

| Property                            | Value                                                                  |
|-------------------------------------|------------------------------------------------------------------------|
| **Rule ID**                         | MSTEST0038                                                             |
| **Title**                           | Don't use 'Assert.AreSame' or 'Assert.AreNotSame' with value types     |
| **Category**                        | Usage                                                                  |
| **Fix is breaking or non-breaking** | Non-breaking                                                           |
| **Enabled by default**              | Yes                                                                    |
| **Default severity**                | Warning                                                                |
| **Introduced in version**           | 3.8.0                                                                  |
| **Is there a code fix**             | Yes                                                                    |

## Cause

The use of [`Assert.AreSame`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/Assert.md) or [`Assert.AreNotSame`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/Assert.md) with one or both arguments being a value type.

## Rule description

[`Assert.AreSame`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/Assert.md) and [`Assert.AreNotSame`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/Assert.md) work by comparing the *reference* of the given `expected`/`notExpected` and actual arguments via `ReferenceEquals`. Hence, when you pass a value type, it is [boxed](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/types/boxing-and-unboxing#boxing).

If using `AreSame`, the assert will always fail. If using `AreNotSame`, the assert will always pass.

For `AreSame`, the only case when the assert passes is if both arguments are nullable value types whose values are both null. In this case, it's clearer to have two separate `Assert.IsNull` calls.

## How to fix violations

Use `Assert.AreEqual` and `Assert.AreNotEqual` instead of `Assert.AreSame` and `Assert.AreNotSame`.
If using `Assert.AreSame` and both arguments are nullable value types whose values are expected to be null, then two separate `Assert.IsNull` calls might be a better fit than `AreEqual`, depending on the intent of the test.

## When to suppress warnings

Do not suppress a warning from this rule. Ignoring this rule will result in an assertion that will always fail or always pass.
