# MessageLevel enum

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.Extensions.dll`
- Package: `MSTest.TestFramework` 4.5.1

Specifies the severity level of messages displayed using the `TestContext.DisplayMessage(MessageLevel,String)` API.

```csharp
public enum MessageLevel
```

## Fields

| Name | Value | Description |
| --- | --- | --- |
| `Informational` | `0` | The message will be displayed as informational, typically used for general updates or non-critical messages. |
| `Warning` | `1` | The message will be displayed as a warning, indicating a potential issue or something requiring attention. |
| `Error` | `2` | The message will be displayed as an error, representing a significant issue or failure. |
