# TestFrameworkCapabilitiesExtensions class

- Namespace: `Microsoft.Testing.Platform.Capabilities.TestFramework`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Provides extension methods for `ITestFrameworkCapabilities`.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public static class TestFrameworkCapabilitiesExtensions
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Methods

### GetCapability

```csharp
public static T? GetCapability<T>(this ITestFrameworkCapabilities capabilities)
```

Gets the capability of the specified type.

**Type parameters:**

- `T`: The type of the capability.

**Parameters:**

- `capabilities`: The test framework capabilities.

**Returns:** The capability.

### HasCapability

```csharp
public static bool HasCapability<T>(this ITestFrameworkCapabilities capabilities)
```

Checks whether the test framework capabilities contain a capability of the specified type.

**Type parameters:**

- `T`: The type of the capability.

**Parameters:**

- `capabilities`: The test framework capabilities.

**Returns:** `true` if the framework contains the capability; `false` otherwise.
