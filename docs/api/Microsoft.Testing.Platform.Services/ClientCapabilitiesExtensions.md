# ClientCapabilitiesExtensions class

- Namespace: `Microsoft.Testing.Platform.Services`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Provides extension methods for `IClientCapabilities`.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public static class ClientCapabilitiesExtensions
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Methods

### GetIsStateful

```csharp
public static bool? GetIsStateful(this IClientCapabilities capabilities)
```

Gets a value indicating whether the client is stateful. For the platform-provided capability service, returns `null` when the client did not declare the capability. Custom implementations fall back to `IClientCapabilities.IsStateful`.

**Parameters:**

- `capabilities`: The client capabilities.

**Returns:** `true` for a stateful client, `false` for a client that explicitly declares itself stateless, or `null` when the platform-provided capability service indicates that the capability was not declared. Custom implementations return their `IClientCapabilities.IsStateful` value.
