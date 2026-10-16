# ITool interface

- Namespace: `Microsoft.Testing.Platform.Tools`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents a non-test command that can be invoked by passing its `ITool.Name` as the first positional command-line argument.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public interface ITool : IExtension
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Properties

### Name

```csharp
string Name { get; }
```

Gets the command-line name of the tool.

## Methods

### RunAsync

```csharp
Task<int> RunAsync(CancellationToken cancellationToken)
```

Runs the tool.

**Parameters:**

- `cancellationToken`: The cancellation token.

**Returns:** The process exit code.
