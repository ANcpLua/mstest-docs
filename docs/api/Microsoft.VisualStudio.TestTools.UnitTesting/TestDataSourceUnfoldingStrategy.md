# TestDataSourceUnfoldingStrategy enum

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

Specifies how parameterized tests should be executed, either as individual test cases for each data row or as a single test case. This affects the test results and the UI representation of the tests.

```csharp
public enum TestDataSourceUnfoldingStrategy : byte
```

## Fields

| Name | Value | Description |
| --- | --- | --- |
| `Auto` | `0` | MSTest will decide whether to unfold the parameterized test based on value from the assembly level attribute `TestDataSourceOptionsAttribute`. If no assembly level attribute is specified, then the default configuration is to unfold. |
| `Unfold` | `1` | Each data row is treated as a separate test case. |
| `Fold` | `2` | The parameterized test is not unfolded; all data rows are treated as a single test case. |
