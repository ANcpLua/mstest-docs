# IArtifactNamingService interface

- Namespace: `Microsoft.Testing.Platform.Services`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Provides file-name templating for artifacts produced by the test platform and its extensions.

```csharp
public interface IArtifactNamingService
```

## Remarks

The service expands the standard placeholders and sanitizes the resulting leaf file name so it is valid on the current operating system. It is registered as a common service and can be resolved through `ServiceProviderExtensions.GetArtifactNamingService(IServiceProvider)`.

## Methods

### ResolveFileName

```csharp
string ResolveFileName(string template)
```

Resolves a file-name template into a concrete file name.

**Parameters:**

- `template`: The template to resolve. The following placeholders are expanded: - `{pname}` — the current test application process name. - `{pid}` — the current process id. - `{asm}` — the entry assembly name (or `unknown` if not available). - `{tfm}` — the short target framework moniker including platform (or `unknown` if not available). - `{arch}` — the process architecture. - `{time}` — the current UTC timestamp. Unknown placeholders are preserved as-is. Any directory portion of the template is preserved while only the leaf file name is sanitized.

**Returns:** The resolved file name, with the leaf sanitized to be valid for the current file system.
