# TestExecutionRequestKind enum

- Namespace: `Microsoft.Testing.Platform.Requests`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Specifies the kind of test execution request.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public enum TestExecutionRequestKind
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Fields

| Name | Value | Description |
| --- | --- | --- |
| `Discovery` | `0` | A test discovery request. |
| `Run` | `1` | A test run request. |
