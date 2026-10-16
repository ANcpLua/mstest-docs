# IConfigurationProvider interface

- Namespace: `Microsoft.Testing.Platform.Configurations`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents a configuration provider.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public interface IConfigurationProvider
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Methods

### LoadAsync

```csharp
Task LoadAsync()
```

Loads the configuration.

**Returns:** Async method.

### TryGet

```csharp
bool TryGet(string key, out string? value)
```

Tries to get the value for the specified key.

**Parameters:**

- `key`: The key.
- `value`: The associated value.

**Returns:** `true` if the key was found; `false` otherwise.
