# TestApplicationOptions class

- Namespace: `Microsoft.Testing.Platform.Builder`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents the options for a test application.

```csharp
public sealed class TestApplicationOptions
```

## Constructors

### TestApplicationOptions

```csharp
public TestApplicationOptions()
```

## Properties

### CancellationToken

```csharp
public CancellationToken CancellationToken { get; set; }
```

Gets or sets a token that requests cooperative cancellation of the test application.

#### Remarks

Cancellation is observed while the test application is running and uses the same application cancellation path as timeouts, Ctrl+C, controller cancellation, and test framework stop policies. A canceled test run returns the test-session-aborted exit code after cleanup completes.

### Configuration

```csharp
public ConfigurationOptions Configuration { get; }
```

Gets the configuration options for the test application.

### EnableTelemetry

```csharp
public bool EnableTelemetry { get; set; }
```

Gets or sets a value indicating whether telemetry is enabled.
