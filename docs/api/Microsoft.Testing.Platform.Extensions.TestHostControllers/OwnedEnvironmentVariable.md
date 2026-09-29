# OwnedEnvironmentVariable class

- Namespace: `Microsoft.Testing.Platform.Extensions.TestHostControllers`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents an owned environment variable.

```csharp
public sealed class OwnedEnvironmentVariable : EnvironmentVariable
```

## Remarks

This class extends the `EnvironmentVariable` class and adds an owner property.

## Constructors

### OwnedEnvironmentVariable

```csharp
public OwnedEnvironmentVariable(
    IExtension owner,
    string variable,
    string? value,
    bool isSecret,
    bool isLocked)
```

Represents an owned environment variable.

#### Remarks

This class extends the `EnvironmentVariable` class and adds an owner property.

## Properties

### Owner

```csharp
public IExtension Owner { get; }
```

Gets the owner of the environment variable.
