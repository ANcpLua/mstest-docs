# IExecuteRequestCompletionNotifier interface

- Namespace: `Microsoft.Testing.Platform.Requests`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Interface to notify the completion of a request.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public interface IExecuteRequestCompletionNotifier
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Methods

### Complete

```csharp
void Complete()
```

Notifies the completion of the request.
