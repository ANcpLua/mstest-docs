# IReadOnlyEnvironmentVariables interface

- Namespace: `Microsoft.Testing.Platform.Extensions.TestHostControllers`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents an interface for reading environment variables.

```csharp
public interface IReadOnlyEnvironmentVariables
```

## Methods

### TryGetVariable

```csharp
bool TryGetVariable(string variable, [NotNullWhen(true)] out OwnedEnvironmentVariable? environmentVariable)
```

Tries to get the value of the specified environment variable.

**Parameters:**

- `variable`: The name of the environment variable.
- `environmentVariable`: When this method returns, contains the value of the environment variable, if it is found; otherwise, null.

**Returns:** true if the environment variable is found; otherwise, false.
