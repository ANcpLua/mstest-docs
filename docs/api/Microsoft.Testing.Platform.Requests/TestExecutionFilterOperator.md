# TestExecutionFilterOperator enum

- Namespace: `Microsoft.Testing.Platform.Requests`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Specifies how child test execution filters are combined.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public enum TestExecutionFilterOperator
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Fields

| Name | Value | Description |
| --- | --- | --- |
| `And` | `0` | Every child filter must match. |
