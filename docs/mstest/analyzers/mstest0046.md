# MSTEST0046: Use Assert instead of StringAssert

| Property                            | Value                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------------|
| **Rule ID**                         | MSTEST0046                                                                               |
| **Title**                           | Use Assert instead of StringAssert                                                       |
| **Category**                        | Usage                                                                                    |
| **Fix is breaking or non-breaking** | Non-breaking                                                                             |
| **Enabled by default**              | Yes                                                                                      |
| **Default severity**                | Info                                                                                     |
| **Introduced in version**           | 3.10.0                                                                                   |
| **Is there a code fix**             | Yes                                                                                      |

## Cause

A test method uses [`StringAssert`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/StringAssert.md) methods instead of equivalent [`Assert`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/Assert.md) methods.

## Rule description

[`StringAssert`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/StringAssert.md) methods have equivalent counterparts in [`Assert`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/Assert.md) that provide the same functionality. Use the [`Assert`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/Assert.md) methods for consistency, better readability, improved discoverability, and alignment with behavior across all test frameworks.

The following [`StringAssert`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/StringAssert.md) methods have equivalent [`Assert`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/Assert.md) methods:

- `StringAssert.Contains(value, substring)` → `Assert.Contains(substring, value)`
- `StringAssert.StartsWith(value, substring)` → `Assert.StartsWith(substring, value)`
- `StringAssert.EndsWith(value, substring)` → `Assert.EndsWith(substring, value)`
- `StringAssert.Matches(value, pattern)` → `Assert.MatchesRegex(pattern, value)`
- `StringAssert.DoesNotMatch(value, pattern)` → `Assert.DoesNotMatchRegex(pattern, value)`

> [!WARNING]
> When migrating from [`StringAssert`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/StringAssert.md) to [`Assert`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/Assert.md) methods, be careful about the change in parameter order. In [`Assert`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/Assert.md) methods, the expected value is always the first parameter.

## How to fix violations

Use the provided code fixer to automatically replace [`StringAssert`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/StringAssert.md) method calls with their equivalent [`Assert`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/Assert.md) methods. You can also manually replace the method calls if needed.

## When to suppress warnings

Don't suppress warnings from this rule. The [`Assert`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/Assert.md) methods provide the same functionality with better consistency.
