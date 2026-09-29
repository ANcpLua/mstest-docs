# ServiceProviderExtensions class

- Namespace: `Microsoft.Testing.Platform.Services`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Extension methods for getting services from an `IServiceProvider`.

```csharp
public static class ServiceProviderExtensions
```

## Methods

### GetArtifactNamingService

```csharp
public static IArtifactNamingService GetArtifactNamingService(this IServiceProvider serviceProvider)
```

Gets the artifact naming service from the `IServiceProvider`.

**Parameters:**

- `serviceProvider`: The service provider.

**Returns:** The artifact naming service.

### GetClientInfo

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public static IClientInfo GetClientInfo(this IServiceProvider serviceProvider)
```

Gets the IClientInfo from the `IServiceProvider`.

**Parameters:**

- `serviceProvider`: The service provider.

**Returns:** The IClientInfo object.

#### Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

### GetCommandLineOptions

```csharp
public static ICommandLineOptions GetCommandLineOptions(this IServiceProvider serviceProvider)
```

Gets the command line options from the `IServiceProvider`.

**Parameters:**

- `serviceProvider`: The service provider.

**Returns:** The command line options.

### GetConfiguration

```csharp
public static IConfiguration GetConfiguration(this IServiceProvider serviceProvider)
```

Gets the configuration from the `IServiceProvider`.

**Parameters:**

- `serviceProvider`: The service provider.

**Returns:** The configuration.

### GetConfigurationRoot

```csharp
public static IConfigurationRoot GetConfigurationRoot(this IServiceProvider serviceProvider)
```

Gets the hierarchical configuration root from the `IServiceProvider`.

**Parameters:**

- `serviceProvider`: The service provider.

**Returns:** The hierarchical configuration root.

### GetLoggerFactory

```csharp
public static ILoggerFactory GetLoggerFactory(this IServiceProvider serviceProvider)
```

Gets the logger factory from the `IServiceProvider`.

**Parameters:**

- `serviceProvider`: The service provider.

**Returns:** The logger factory.

### GetMessageBus

```csharp
public static IMessageBus GetMessageBus(this IServiceProvider serviceProvider)
```

Gets the message bus from the `IServiceProvider`.

**Parameters:**

- `serviceProvider`: The service provider.

**Returns:** The message bus.

### GetOutputDevice

```csharp
public static IOutputDevice GetOutputDevice(this IServiceProvider serviceProvider)
```

Gets the output device from the `IServiceProvider`.

**Parameters:**

- `serviceProvider`: The service provider.

**Returns:** The output device.

### GetRequiredService

```csharp
public static TService GetRequiredService<TService>(this IServiceProvider provider)
```

Gets the required service of type `TService` from the `IServiceProvider`.

**Type parameters:**

- `TService`: The type of the service.

**Parameters:**

- `provider`: The service provider.

**Returns:** The required service of type `TService`.

**Exceptions:**

- `ArgumentNullException`: Thrown when the `provider` is null.
- `InvalidOperationException`: Thrown when the required service is not found.

### GetService

```csharp
public static TService? GetService<TService>(this IServiceProvider provider)
```

Gets the service of type `TService` from the `IServiceProvider`.

**Type parameters:**

- `TService`: The type of the service.

**Parameters:**

- `provider`: The service provider.

**Returns:** The service of type `TService` or null if not found.

**Exceptions:**

- `ArgumentNullException`: Thrown when the `provider` is null.
