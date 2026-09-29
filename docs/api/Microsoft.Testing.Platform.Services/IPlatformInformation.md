# IPlatformInformation interface

- Namespace: `Microsoft.Testing.Platform.Services`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Provides information about the platform.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public interface IPlatformInformation
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Properties

### BuildDate

```csharp
DateTimeOffset? BuildDate { get; }
```

Gets the platform's build date.

### CommitHash

```csharp
string? CommitHash { get; }
```

Gets the platform's commit hash.

### Name

```csharp
string Name { get; }
```

Gets the platform's name.

### Version

```csharp
string? Version { get; }
```

Gets the platform's version.
