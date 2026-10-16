# IConfigurationSection interface

- Namespace: `Microsoft.Testing.Platform.Configurations`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents a section of an aggregated hierarchical configuration.

```csharp
public interface IConfigurationSection : IConfigurationRoot, IConfiguration
```

## Properties

### HasValue

```csharp
bool HasValue { get; }
```

Gets a value indicating whether a provider supplied a scalar value for this section.

### Key

```csharp
string Key { get; }
```

Gets the key occupying this section's final path segment.

### Path

```csharp
string Path { get; }
```

Gets the full path to this section from the configuration root.

### Value

```csharp
string? Value { get; }
```

Gets the scalar value associated with this section.
