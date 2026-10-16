# ICapabilities<TCapability> interface

- Namespace: `Microsoft.Testing.Platform.Capabilities`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents the capabilities provided by an extension.

```csharp
public interface ICapabilities<TCapability>
```

**Type parameters:**

- `TCapability`: The type of capability.

## Properties

### Capabilities

```csharp
IReadOnlyCollection<TCapability> Capabilities { get; }
```

Gets the collection of capabilities.
