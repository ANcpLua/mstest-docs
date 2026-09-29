# IConfigurationSource interface

- Namespace: `Microsoft.Testing.Platform.Configurations`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents a configuration source.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public interface IConfigurationSource : IExtension
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Properties

### Order

```csharp
int Order { get; }
```

Gets the order of the configuration source.

## Methods

### BuildAsync

```csharp
Task<IConfigurationProvider> BuildAsync(CommandLineParseResult commandLineParseResult)
```

Builds the configuration provider.

**Parameters:**

- `commandLineParseResult`: The result of the command line parsing.

**Returns:** The configuration provider.
