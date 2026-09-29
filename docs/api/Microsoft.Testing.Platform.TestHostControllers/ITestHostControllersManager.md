# ITestHostControllersManager interface

- Namespace: `Microsoft.Testing.Platform.TestHostControllers`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents a manager for test host controllers.

```csharp
public interface ITestHostControllersManager
```

## Methods

### AddEnvironmentVariableProvider

```csharp
void AddEnvironmentVariableProvider(Func<IServiceProvider, ITestHostEnvironmentVariableProvider> environmentVariableProviderFactory)
```

Adds an environment variable provider to the test host controller manager.

**Parameters:**

- `environmentVariableProviderFactory`: The factory method that creates the environment variable provider.

```csharp
void AddEnvironmentVariableProvider<T>(CompositeExtensionFactory<T> compositeServiceFactory)
```

Adds an environment variable provider to the test host controller manager.

**Type parameters:**

- `T`: The type of the environment variable provider.

**Parameters:**

- `compositeServiceFactory`: The factory method that creates the composite service.

### AddProcessLifetimeHandler

```csharp
void AddProcessLifetimeHandler(Func<IServiceProvider, ITestHostProcessLifetimeHandler> lifetimeHandler)
```

Adds a process lifetime handler to the test host controller manager.

**Parameters:**

- `lifetimeHandler`: The factory method that creates the process lifetime handler.

```csharp
void AddProcessLifetimeHandler<T>(CompositeExtensionFactory<T> compositeServiceFactory)
```

Adds a process lifetime handler to the test host controller manager.

**Type parameters:**

- `T`: The type of the process lifetime handler.

**Parameters:**

- `compositeServiceFactory`: The factory method that creates the composite service.

### AddTestHostLauncher

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
void AddTestHostLauncher(Func<IServiceProvider, ITestHostLauncher> testHostLauncherFactory)
```

Adds a test host launcher to the test host controller manager, replacing the platform's default `Process.Start` behavior. At most one launcher can be registered.

**Parameters:**

- `testHostLauncherFactory`: The factory method that creates the test host launcher.

#### Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
void AddTestHostLauncher<T>(CompositeExtensionFactory<T> compositeServiceFactory)
```

Adds a test host launcher to the test host controller manager, replacing the platform's default `Process.Start` behavior. At most one launcher can be registered.

**Type parameters:**

- `T`: The type of the test host launcher.

**Parameters:**

- `compositeServiceFactory`: The factory method that creates the composite service.

#### Remarks

This API is experimental. It may change, break, or be removed at any time without notice.
