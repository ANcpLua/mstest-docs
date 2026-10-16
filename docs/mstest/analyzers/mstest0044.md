# MSTEST0044: Prefer TestMethod over DataTestMethod

| Property                            | Value                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------------|
| **Rule ID**                         | MSTEST0044                                                                               |
| **Title**                           | Prefer TestMethod over DataTestMethod                                                    |
| **Category**                        | Design                                                                                   |
| **Fix is breaking or non-breaking** | Non-breaking                                                                             |
| **Enabled by default**              | Yes                                                                                      |
| **Default severity**                | Warning                                                                                  |
| **Introduced in version**           | 3.10.0                                                                                    |
| **Is there a code fix**             | Yes                                                                                       |

## Cause

A method or type uses [`DataTestMethodAttribute`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.testtools.unittesting.datatestmethodattribute?view=mstest-net-4.5) or inherits from it.

## Rule description

[`DataTestMethodAttribute`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.testtools.unittesting.datatestmethodattribute?view=mstest-net-4.5) provides no additional value over [`TestMethodAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestMethodAttribute.md) and will be removed in a future version. Use [`TestMethodAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestMethodAttribute.md) instead for all test methods, including those that use data source attributes like [`DataRowAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/DataRowAttribute.md).

## How to fix violations

Use the provided code fixer to automatically replace [`DataTestMethodAttribute`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.testtools.unittesting.datatestmethodattribute?view=mstest-net-4.5) with [`TestMethodAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestMethodAttribute.md). You can also manually replace the attribute if needed. If you have a custom attribute that inherits from [`DataTestMethodAttribute`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.testtools.unittesting.datatestmethodattribute?view=mstest-net-4.5), change it to inherit from [`TestMethodAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestMethodAttribute.md) instead.

## When to suppress warnings

Don't suppress warnings from this rule. [`DataTestMethodAttribute`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.testtools.unittesting.datatestmethodattribute?view=mstest-net-4.5) will be removed in a future version, so you should migrate to [`TestMethodAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestMethodAttribute.md).
