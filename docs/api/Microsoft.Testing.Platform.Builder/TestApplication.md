# TestApplication class

- Namespace: `Microsoft.Testing.Platform.Builder`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents a test application.

```csharp
public sealed class TestApplication : ITestApplication, IDisposable
```

## Methods

### CreateBuilderAsync

```csharp
public static Task<ITestApplicationBuilder> CreateBuilderAsync(string[] args, TestApplicationOptions? testApplicationOptions = null)
```

Creates a builder asynchronously.

**Parameters:**

- `args`: The command line arguments.
- `testApplicationOptions`: The test application options.

**Returns:** The task representing the asynchronous operation.

### CreateServerModeBuilderAsync

```csharp
[Obsolete("This method is obsolete. Use CreateBuilderAsync instead.", DiagnosticId = "MTP0002", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public static Task<ITestApplicationBuilder> CreateServerModeBuilderAsync(string[] args, TestApplicationOptions? testApplicationOptions = null)
```

Creates a server mode builder asynchronously.

**Parameters:**

- `args`: The command line arguments.
- `testApplicationOptions`: The test application options.

**Returns:** The task representing the asynchronous operation.

### Dispose

```csharp
public void Dispose()
```

### RunAsync

```csharp
public Task<int> RunAsync()
```

Runs the test application asynchronously.

**Returns:** The exit code of the test application.
