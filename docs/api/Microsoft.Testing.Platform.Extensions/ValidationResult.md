# ValidationResult struct

- Namespace: `Microsoft.Testing.Platform.Extensions`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents the result of a validation operation.

```csharp
public readonly struct ValidationResult
```

## Properties

### ErrorMessage

```csharp
public string? ErrorMessage { get; }
```

Gets the error message associated with an invalid validation result.

### IsValid

```csharp
public bool IsValid { get; }
```

Gets a value indicating whether the validation result is valid.

### ValidTask

```csharp
public static Task<ValidationResult> ValidTask { get; }
```

Gets a task that represents a valid validation result.

## Methods

### Invalid

```csharp
public static ValidationResult Invalid(string errorMessage)
```

Creates an invalid validation result with the specified error message.

**Parameters:**

- `errorMessage`: The error message.

**Returns:** An invalid validation result.

### InvalidTask

```csharp
public static Task<ValidationResult> InvalidTask(string errorMessage)
```

Creates a task that represents an invalid validation result with the specified error message.

**Parameters:**

- `errorMessage`: The error message.

**Returns:** A task that represents an invalid validation result.

### Valid

```csharp
public static ValidationResult Valid()
```

Creates a valid validation result.

**Returns:** A valid validation result.
