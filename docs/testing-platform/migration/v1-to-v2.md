# Migrate from Microsoft.Testing.Platform (MTP) v1 to v2

The stable version MTP v2 is now available. This migration guide explores what's changed in MTP v2 and how you can migrate to this version.

## Source breaking changes

These are breaking changes that might cause build errors after migration.

### Dropped unsupported target frameworks

Support for target frameworks from .NET Core 3.1 to .NET 7 is dropped. The minimum supported .NET version is .NET 8.
This change doesn't affect .NET Framework. .NET Framework 4.6.2 continues to be the minimum supported .NET Framework target.

### Removed obsolete types

The following types were marked obsolete in MTP v1. In MTP v2, they are removed completely:

- `ITestApplicationLifecycleCallbacks`: use `ITestHostApplicationLifetime` instead.
- `TestNodeFileArtifact`: use `FileArtifactProperty` instead.
- `KeyValuePairStringProperty`: use `TestMetadataProperty` instead.
- `TestSessionContext.Client`: use `IClientInfo` instead.

This breaking change doesn't affect typical users of test frameworks. It only affects test framework authors and extension authors.

### API signature changes

- A `CancellationToken` parameter was added to [`IOutputDevice.DisplayAsync`](../../api/Microsoft.Testing.Platform.OutputDevice/IOutputDevice.md).
- Methods in [`ITestSessionLifetimeHandler`](../../api/Microsoft.Testing.Platform.Extensions.TestHost/ITestSessionLifetimeHandler.md) interface are changed to have an `ITestSessionContext` parameter instead of both [`SessionUid`](../../api/Microsoft.Testing.Platform.TestHost/SessionUid.md) and [`CancellationToken`](https://learn.microsoft.com/en-us/dotnet/api/system.threading.cancellationtoken) parameters.
- `IDataConsumer` is moved from `Microsoft.Testing.Platform.Extensions.TestHost` namespace to `Microsoft.Testing.Platform.Extensions`.

This breaking change doesn't affect typical users of test frameworks. It only affects test framework authors and extension authors.

## Behavior breaking changes

These are breaking changes that might affect the behavior at runtime.

### `dotnet test` requires the MTP mode

Running MTP test projects with .NET 10 SDK now requires opting-in to the MTP-based `dotnet test`. The `TestingPlatformDotnetTestSupport` MSBuild property from MTP v1 no longer enables running them.

To opt-in the MTP-based implementation, create global.json in repository or solution root (or update existing global.json if you have one already), to have test runner set as Microsoft.Testing.Platform, as shown in the following example:

```json
{
  "test": {
    "runner": "Microsoft.Testing.Platform"
  }
}
```

### Rename of command-line options

- The `--diagnostic-output-fileprefix` command-line option was renamed to `--diagnostic-file-prefix`.
- The `--diagnostic-filelogger-synchronouswrite` command-line option was renamed to `--diagnostic-synchronous-write`.
