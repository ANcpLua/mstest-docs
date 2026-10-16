# IConfiguration interface

- Namespace: `Microsoft.Testing.Platform.Configurations`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents a configuration interface.

```csharp
public interface IConfiguration
```

## Properties

### Item

```csharp
string? this[string key] { get; }
```

Gets or sets the value associated with the specified key.

**Parameters:**

- `key`: The key of the value to get or set.
