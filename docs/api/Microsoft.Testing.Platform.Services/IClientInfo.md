# IClientInfo interface

- Namespace: `Microsoft.Testing.Platform.Services`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents the client information.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public interface IClientInfo
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Properties

### Capabilities

```csharp
IClientCapabilities Capabilities { get; }
```

Gets the capabilities declared by the client.

### Id

```csharp
string Id { get; }
```

Gets the client ID.

### Version

```csharp
string Version { get; }
```

Gets the client version.
