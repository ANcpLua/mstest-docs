# MSTEST0042: Avoid duplicated 'DataRow' entries

| Property                            | Value                                                                  |
|-------------------------------------|------------------------------------------------------------------------|
| **Rule ID**                         | MSTEST0042                                                             |
| **Title**                           | Avoid duplicated 'DataRow' entries                                     |
| **Category**                        | Usage                                                                  |
| **Fix is breaking or non-breaking** | Non-breaking                                                           |
| **Enabled by default**              | Yes                                                                    |
| **Default severity**                | Warning                                                                |
| **Introduced in version**           | 3.9.0                                                                  |
| **Is there a code fix**             | No                                                                     |

## Cause

A test method has two or more [DataRow](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/DataRowAttribute.md) attributes that are equivalent.

## Rule description

[`DataRowAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/DataRowAttribute.md) is used to denote inputs to test methods. It's not expected that a test will intentionally run twice with the exact same data. Duplicated `DataRow`s are often a copy/paste error.

## How to fix violations

Either remove the duplicate `DataRow` attribute, or fix it to make unique.

## When to suppress warnings

Do not suppress a warning from this rule, unless you intended to use the same input more than once.
