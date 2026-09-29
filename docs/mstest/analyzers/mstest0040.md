# MSTEST0040: Do not assert inside 'async void' contexts

| Property                            | Value                                                                  |
|-------------------------------------|------------------------------------------------------------------------|
| **Rule ID**                         | MSTEST0040                                                             |
| **Title**                           | Do not assert inside 'async void' contexts                             |
| **Category**                        | Usage                                                                  |
| **Fix is breaking or non-breaking** | Non-breaking                                                           |
| **Enabled by default**              | Yes                                                                    |
| **Default severity**                | Warning                                                                |
| **Introduced in version**           | 3.8.0                                                                  |
| **Is there a code fix**             | No                                                                     |

## Cause

The use of any assertion method in an `async void` method, local function, or lambda.

## Rule description

Exceptions that are thrown in an `async void` context are unhandled. Under .NET, a failing assertion in an `async void` method might crash the process when using MTP. In cases where a custom `SynchronizationContext` is present that catches the exception, the failing assertion might be silently swallowed.

## How to fix violations

Refactor the code to not use assertions in `async void`.

## When to suppress warnings

Do not suppress a warning from this rule.
