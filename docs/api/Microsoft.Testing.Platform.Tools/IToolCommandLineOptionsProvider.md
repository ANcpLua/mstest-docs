# IToolCommandLineOptionsProvider interface

- Namespace: `Microsoft.Testing.Platform.Tools`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents command-line options that apply to a specific `ITool`.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public interface IToolCommandLineOptionsProvider : ICommandLineOptionsProvider, IExtension
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Properties

### ToolName

```csharp
string ToolName { get; }
```

Gets the name of the tool to which these options apply.
