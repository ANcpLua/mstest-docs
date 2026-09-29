# IClientCapabilities interface

- Namespace: `Microsoft.Testing.Platform.Services`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents the capabilities declared by the client that is driving the test host.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public interface IClientCapabilities
```

## Remarks

Capabilities are opt-in: unless a client explicitly declares a capability, the platform assumes the most conservative (default) behavior. Use `ClientCapabilitiesExtensions.GetIsStateful(IClientCapabilities)` when the distinction between an explicitly stateless client and an undeclared capability is required.

This API is experimental. It may change, break, or be removed at any time without notice.

## Properties

### IsStateful

```csharp
bool IsStateful { get; }
```

Gets a value indicating whether the client is stateful.

#### Remarks

A stateful client persists an addressable set of test nodes for the whole session and keeps each node in its last-known state until it is explicitly updated (for example, an IDE test explorer). A stateless client consumes updates as a stream and does not retain node state after the run (for example, `dotnet test`). The default is `false` (stateless); a client opts into stateful behavior. This capability is independent of connection lifetime and multi-request support.
