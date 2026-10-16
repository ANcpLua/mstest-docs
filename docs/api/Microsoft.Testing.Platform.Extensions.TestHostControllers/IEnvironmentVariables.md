# IEnvironmentVariables interface

- Namespace: `Microsoft.Testing.Platform.Extensions.TestHostControllers`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents an interface for managing environment variables.

```csharp
public interface IEnvironmentVariables : IReadOnlyEnvironmentVariables
```

## Methods

### RemoveVariable

```csharp
void RemoveVariable(string variable)
```

Removes the specified environment variable.

**Parameters:**

- `variable`: The name of the environment variable to remove.

### SetVariable

```csharp
void SetVariable(EnvironmentVariable environmentVariable)
```

Sets the value of the specified environment variable.

**Parameters:**

- `environmentVariable`: The environment variable to set.
