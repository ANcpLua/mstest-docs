# CreateTestSessionResult class

- Namespace: `Microsoft.Testing.Platform.Extensions.TestFramework`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents the result of creating a test session.

```csharp
public sealed class CreateTestSessionResult
```

## Constructors

### CreateTestSessionResult

```csharp
public CreateTestSessionResult()
```

## Properties

### ErrorMessage

```csharp
public string? ErrorMessage { get; set; }
```

Gets or sets the error message, if any.

### IsSuccess

```csharp
public bool IsSuccess { get; set; }
```

Gets or sets a value indicating whether the test session creation was successful.

### WarningMessage

```csharp
public string? WarningMessage { get; set; }
```

Gets or sets the warning message, if any.
