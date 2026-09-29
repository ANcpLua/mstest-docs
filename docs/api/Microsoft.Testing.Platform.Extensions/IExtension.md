# IExtension interface

- Namespace: `Microsoft.Testing.Platform.Extensions`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

The interface that all extensions must implement. Extensions are a special kind of services that have some identity.

```csharp
public interface IExtension
```

## Properties

### Description

```csharp
string Description { get; }
```

Gets the description of the extension.

### DisplayName

```csharp
string DisplayName { get; }
```

Gets the display name of the extension.

### Uid

```csharp
string Uid { get; }
```

Gets the unique identifier for the extension.

#### Remarks

The value must be a **stable** string constant that survives class renames. It is SHA-256-hashed for telemetry, displayed verbatim in `--info` output and error messages, embedded in artifact metadata, and used for feature detection, so changing it silently breaks telemetry continuity and any consumer relying on the previous value.

Do **not** derive the value from `nameof(ImplementingClass)`: an IDE "Rename Symbol" refactor would then change the UID without any visible diff at the call site. Use an explicit string literal or `const` instead, even if its initial value happens to match the class name.

### Version

```csharp
string Version { get; }
```

Gets the version of the extension (ideally semantic version).

## Methods

### IsEnabledAsync

```csharp
Task<bool> IsEnabledAsync()
```

Controls whether the extension is enabled or not. This is useful for extensions that are always registered but only enabled when certain conditions are met. For example, an extension that would want to be run only when its associated command line option is provided by the user.
