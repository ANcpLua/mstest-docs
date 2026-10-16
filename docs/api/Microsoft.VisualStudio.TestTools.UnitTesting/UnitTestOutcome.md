# UnitTestOutcome enum

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

unit test outcomes.

```csharp
public enum UnitTestOutcome
```

## Fields

| Name | Value | Description |
| --- | --- | --- |
| `Failed` | `0` | Test was executed, but there were issues. Issues may involve exceptions or failed assertions. |
| `Inconclusive` | `1` | Test has completed, but we can't say if it passed or failed. May be used for aborted tests. |
| `Passed` | `2` | Test was executed without any issues. |
| `InProgress` | `3` | Test is currently executing. |
| `Error` | `4` | There was a system error while we were trying to execute a test. |
| `Timeout` | `5` | The test timed out. |
| `Aborted` | `6` | Test was aborted by the user. |
| `Unknown` | `7` | Test is in an unknown state. |
| `NotRunnable` | `8` | Test cannot be executed. |
| `NotFound` | `9` | The specific test cannot be found. |
| `Ignored` | `10` | Test is marked as ignored. |
