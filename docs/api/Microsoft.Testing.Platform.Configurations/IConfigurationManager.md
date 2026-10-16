# IConfigurationManager interface

- Namespace: `Microsoft.Testing.Platform.Configurations`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents a configuration manager.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public interface IConfigurationManager
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Methods

### AddConfigurationSource

```csharp
void AddConfigurationSource(Func<IConfigurationSource> source)
```

Adds a configuration source.

**Parameters:**

- `source`: The source.
