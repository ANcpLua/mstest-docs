# ITestApplication interface

- Namespace: `Microsoft.Testing.Platform.Builder`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents an interface for a test application.

```csharp
public interface ITestApplication : IDisposable
```

## Methods

### RunAsync

```csharp
Task<int> RunAsync()
```

Runs the test application asynchronously.

**Returns:** The exit code of the test application.
