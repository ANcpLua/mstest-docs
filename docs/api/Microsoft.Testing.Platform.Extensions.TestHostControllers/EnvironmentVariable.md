# EnvironmentVariable class

- Namespace: `Microsoft.Testing.Platform.Extensions.TestHostControllers`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents an environment variable.

```csharp
public class EnvironmentVariable
```

## Constructors

### EnvironmentVariable

```csharp
public EnvironmentVariable(
    string variable,
    string? value,
    bool isSecret,
    bool isLocked)
```

Represents an environment variable.

**Parameters:**

- `variable`: The name of the environment variable.
- `value`: The value of the environment variable.
- `isSecret`: Indicates whether the environment variable is a secret.
- `isLocked`: Indicates whether the environment variable is locked.

## Properties

### IsLocked

```csharp
public bool IsLocked { get; }
```

Gets a value indicating whether the environment variable is locked.

### IsSecret

```csharp
public bool IsSecret { get; }
```

Gets a value indicating whether the environment variable is a secret.

### Value

```csharp
public string? Value { get; }
```

Gets the value of the environment variable.

### Variable

```csharp
public string Variable { get; }
```

Gets the name of the environment variable.
