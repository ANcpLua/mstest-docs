# IToolsManager interface

- Namespace: `Microsoft.Testing.Platform.Tools`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Registers tools with a test application.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public interface IToolsManager
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Methods

### AddTool

```csharp
void AddTool(Func<IServiceProvider, ITool> toolFactory)
```

Adds a tool factory.

**Parameters:**

- `toolFactory`: The factory used to create the tool.
