# IHierarchicalConfigurationProvider interface

- Namespace: `Microsoft.Testing.Platform.Configurations`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents a configuration provider that exposes hierarchical configuration sections.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public interface IHierarchicalConfigurationProvider : IConfigurationProvider
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Methods

### GetChildKeys

```csharp
IEnumerable<string> GetChildKeys(string? parentPath)
```

Gets the immediate child keys below the specified configuration path.

**Parameters:**

- `parentPath`: The parent path, or `null` for the configuration root.

**Returns:** The immediate child keys.

### TryGetScalar

```csharp
bool TryGetScalar(string key, out string? value)
```

Tries to get the scalar value for the specified key.

**Parameters:**

- `key`: The key.
- `value`: The associated scalar value.

**Returns:** `true` if a scalar value was found; `false` if the key is absent or represents only a container.
