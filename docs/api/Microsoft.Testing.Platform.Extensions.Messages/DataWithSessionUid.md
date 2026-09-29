# DataWithSessionUid class

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents data with a session UID.

```csharp
public abstract class DataWithSessionUid : PropertyBagData
```

## Constructors

### DataWithSessionUid

```csharp
protected DataWithSessionUid(
    string displayName,
    string? description,
    SessionUid sessionUid)
```

Initializes a new instance of the `DataWithSessionUid` class.

**Parameters:**

- `displayName`: The display name of the data.
- `description`: The description of the data.
- `sessionUid`: The session UID.

## Properties

### SessionUid

```csharp
public SessionUid SessionUid { get; }
```

Gets the session UID.

## Methods

### ToString

```csharp
public override string ToString()
```
