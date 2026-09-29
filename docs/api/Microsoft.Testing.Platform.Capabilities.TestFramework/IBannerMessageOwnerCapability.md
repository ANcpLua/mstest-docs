# IBannerMessageOwnerCapability interface

- Namespace: `Microsoft.Testing.Platform.Capabilities.TestFramework`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

An optional test framework capability that allows the test framework to provide the banner message to the platform. If the message is null or if the capability is not present, the platform will use its default banner message. This capability implementation allows to abstract away the various conditions that the test framework may need to consider to decide whether or not the banner message should be displayed.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public interface IBannerMessageOwnerCapability : ITestFrameworkCapability, ICapability
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Methods

### GetBannerMessageAsync

```csharp
Task<string?> GetBannerMessageAsync()
```

Process the banner message and return the message to be displayed.

**Returns:** The banner message to be displayed or `null` to use the default banner message.
