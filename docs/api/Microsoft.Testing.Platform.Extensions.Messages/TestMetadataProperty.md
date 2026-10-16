# TestMetadataProperty class

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Property that represents a generic test metadata property in the shape of a key-value pair associated with a `TestNode`.

```csharp
public sealed class TestMetadataProperty : IProperty, IEquatable<TestMetadataProperty>
```

## Constructors

### TestMetadataProperty

```csharp
public TestMetadataProperty(string key)
```

Initializes a new instance of the `TestMetadataProperty` class with a key and an empty value.

**Parameters:**

- `key`: The metadata key.

```csharp
public TestMetadataProperty(string key, string value)
```

Initializes a new instance of the `TestMetadataProperty` class with a key and value.

**Parameters:**

- `key`: The metadata key.
- `value`: The metadata value.

## Properties

### Key

```csharp
public string Key { get; }
```

Gets the metadata key.

### Value

```csharp
public string Value { get; }
```

Gets the metadata value.

## Methods

### Equals

```csharp
public bool Equals(TestMetadataProperty? other)
```

```csharp
public override bool Equals(object? obj)
```

### GetHashCode

```csharp
public override int GetHashCode()
```

### ToString

```csharp
public override string ToString()
```
