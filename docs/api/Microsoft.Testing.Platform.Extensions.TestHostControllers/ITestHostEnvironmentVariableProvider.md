# ITestHostEnvironmentVariableProvider interface

- Namespace: `Microsoft.Testing.Platform.Extensions.TestHostControllers`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents an interface for providing environment variables to the test host.

```csharp
public interface ITestHostEnvironmentVariableProvider : ITestHostControllersExtension, IExtension
```

## Methods

### UpdateAsync

```csharp
Task UpdateAsync(IEnvironmentVariables environmentVariables)
```

Updates the environment variables for the test host asynchronously.

**Parameters:**

- `environmentVariables`: The environment variables to update.

**Returns:** A task representing the asynchronous operation.

### ValidateTestHostEnvironmentVariablesAsync

```csharp
Task<ValidationResult> ValidateTestHostEnvironmentVariablesAsync(IReadOnlyEnvironmentVariables environmentVariables)
```

Validates the test host environment variables asynchronously.

**Parameters:**

- `environmentVariables`: The environment variables to validate.

**Returns:** A task representing the asynchronous operation and containing the validation result.
