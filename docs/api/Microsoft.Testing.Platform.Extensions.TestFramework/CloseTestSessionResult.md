# CloseTestSessionResult class

- Namespace: `Microsoft.Testing.Platform.Extensions.TestFramework`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents the result of closing a test session.

```csharp
public sealed class CloseTestSessionResult
```

## Constructors

### CloseTestSessionResult

```csharp
public CloseTestSessionResult()
```

## Properties

### ErrorMessage

```csharp
public string? ErrorMessage { get; set; }
```

Gets or sets the error message associated with the test session closing.

### IsSuccess

```csharp
public bool IsSuccess { get; set; }
```

Gets or sets a value indicating whether the test session closing was successful.

### WarningMessage

```csharp
public string? WarningMessage { get; set; }
```

Gets or sets the warning message associated with the test session closing.
