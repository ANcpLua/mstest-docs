# ITestApplicationBuilder interface

- Namespace: `Microsoft.Testing.Platform.Builder`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents an interface for building test applications.

```csharp
public interface ITestApplicationBuilder
```

## Properties

### CommandLine

```csharp
ICommandLineManager CommandLine { get; }
```

Gets the command line manager.

### Configuration

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
IConfigurationManager Configuration { get; }
```

Gets the configuration manager.

#### Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

### Logging

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
ILoggingManager Logging { get; }
```

Gets the logging manager.

#### Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

### TestHost

```csharp
ITestHostManager TestHost { get; }
```

Gets the test host manager.

### TestHostControllers

```csharp
ITestHostControllersManager TestHostControllers { get; }
```

Gets the test host controllers manager.

### TestHostOrchestrator

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
ITestHostOrchestratorManager TestHostOrchestrator { get; }
```

Gets the test host orchestrator manager.

#### Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Methods

### BuildAsync

```csharp
Task<ITestApplication> BuildAsync()
```

Builds the test application asynchronously.

**Returns:** A task representing the asynchronous operation. The task result is the built test application.

### RegisterTestFramework

```csharp
ITestApplicationBuilder RegisterTestFramework(
    Func<IServiceProvider, ITestFrameworkCapabilities> capabilitiesFactory,
    Func<ITestFrameworkCapabilities, IServiceProvider, ITestFramework> frameworkFactory)
```

Registers a test framework with the application builder.

**Parameters:**

- `capabilitiesFactory`: The factory method for creating test framework capabilities.
- `frameworkFactory`: The factory method for creating a test framework adapter.

**Returns:** The updated test application builder.
