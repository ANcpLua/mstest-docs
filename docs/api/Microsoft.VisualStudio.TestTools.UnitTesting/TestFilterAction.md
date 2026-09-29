# TestFilterAction enum

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

Indicates how the MSTest adapter should treat a test for which an `ITestFilter` returned a particular `TestFilterResult`.

```csharp
[Experimental("MSTESTEXP", UrlFormat = "https://aka.ms/mstest/diagnostics#{0}")]
public enum TestFilterAction
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Fields

| Name | Value | Description |
| --- | --- | --- |
| `Run` | `0` | Run the test normally. This is the default action so that `default(TestFilterResult)` is the safe choice when an implementation forgets to set a result explicitly. |
| `Drop` | `1` | Silently drop the test. No `TestResult` is emitted, the test does not appear in the test count, and the declaring class's `[ClassInitialize]` is not invoked unless another (non-dropped) test in the same class still has to run. This matches the semantics of the platform `--filter` command-line option. |
| `Skip` | `2` | Report the test as Skipped, with the reason supplied to `TestFilterResult.Skip(String)`. The test appears in the test count, the TRX/console output, and IDE test explorers. |
