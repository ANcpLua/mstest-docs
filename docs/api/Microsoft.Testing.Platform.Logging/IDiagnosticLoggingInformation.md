# IDiagnosticLoggingInformation interface

- Namespace: `Microsoft.Testing.Platform.Logging`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Provides information about the built-in diagnostic file logger.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public interface IDiagnosticLoggingInformation
```

## Remarks

This service is registered only when diagnostic logging is enabled. This API is experimental. It may change, break, or be removed at any time without notice.

## Properties

### LogFile

```csharp
FileInfo LogFile { get; }
```

Gets the diagnostic log file that is currently receiving log entries.

#### Remarks

The path can change during test application construction if the platform relocates the log to the effective results directory. Extensions created during that phase should retain this service and read this property when the path is needed instead of caching the returned `FileInfo`.

If the platform cannot safely move an earlier log file during recovery, that partial file can remain in its original location while this property identifies the replacement file that receives new entries.

Use `FileInfo.Directory` or `FileInfo.DirectoryName` to get the resolved diagnostic output directory.

### LogLevel

```csharp
LogLevel LogLevel { get; }
```

Gets the minimum log level written to the diagnostic log file.

### SynchronousWrite

```csharp
bool SynchronousWrite { get; }
```

Gets a value indicating whether diagnostic log entries are written synchronously.
