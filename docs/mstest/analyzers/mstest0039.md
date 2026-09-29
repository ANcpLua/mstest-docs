# MSTEST0039: Use newer 'Assert.Throws' methods

| Property                            | Value                                                                  |
|-------------------------------------|------------------------------------------------------------------------|
| **Rule ID**                         | MSTEST0039                                                             |
| **Title**                           | Use newer 'Assert.Throws' methods                                      |
| **Category**                        | Usage                                                                  |
| **Fix is breaking or non-breaking** | Non-breaking                                                           |
| **Enabled by default**              | Yes                                                                    |
| **Default severity**                | Warning starting with 3.10, Info before                                |
| **Introduced in version**           | 3.8.0                                                                  |
| **Is there a code fix**             | Yes                                                                    |

> [!NOTE]
> This analyzer is no longer relevant for MSTest 4 as the old assertion APIs were removed.

## Cause

The use of `Assert.ThrowsException` or `Assert.ThrowsExceptionAsync`, which are no longer recommended.

## Rule description

The `Assert.ThrowsException` and `Assert.ThrowsExceptionAsync` methods aren't recommended and might be deprecated in the future.

## How to fix violations

Use [`Assert.ThrowsExactly`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/Assert.md) or [`Assert.ThrowsExactlyAsync`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/Assert.md) instead of `Assert.ThrowsException` or `Assert.ThrowsExceptionAsync`.

## When to suppress warnings

Do not suppress a warning from this rule. It's strongly recommended to move from the old APIs to the new ones.
