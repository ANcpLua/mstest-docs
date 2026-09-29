# IConfigurationRoot interface

- Namespace: `Microsoft.Testing.Platform.Configurations`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents the root of an aggregated hierarchical configuration.

```csharp
public interface IConfigurationRoot : IConfiguration
```

## Methods

### GetChildren

```csharp
IEnumerable<IConfigurationSection> GetChildren()
```

Gets the immediate child sections of the current configuration root or section.

**Returns:** The immediate child sections.

#### Remarks

Configuration providers must implement `IHierarchicalConfigurationProvider` for their keys to be discoverable through enumeration. Values from other providers remain accessible by requesting a known section path.

### GetSection

```csharp
IConfigurationSection GetSection(string key)
```

Gets the configuration section at the specified path.

**Parameters:**

- `key`: The section path relative to the current configuration root or section.

**Returns:** The requested configuration section.
