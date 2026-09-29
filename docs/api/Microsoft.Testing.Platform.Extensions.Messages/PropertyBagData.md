# PropertyBagData class

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents a property bag data.

```csharp
public abstract class PropertyBagData : IData
```

## Constructors

### PropertyBagData

```csharp
protected PropertyBagData(string displayName, string? description)
```

Represents a property bag data.

**Parameters:**

- `displayName`: The display name.
- `description`: The description.

## Properties

### Description

```csharp
public string? Description { get; }
```

Gets the description.

### DisplayName

```csharp
public string DisplayName { get; }
```

Gets the display name.

### Properties

```csharp
public PropertyBag Properties { get; }
```

Gets the properties.

## Methods

### ToString

```csharp
public override string ToString()
```
