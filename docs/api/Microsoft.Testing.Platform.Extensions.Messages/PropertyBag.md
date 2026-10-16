# PropertyBag class

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents a property bag.

```csharp
public sealed class PropertyBag
```

## Constructors

### PropertyBag

```csharp
public PropertyBag()
```

Initializes a new instance of the `PropertyBag` class.

```csharp
public PropertyBag(IEnumerable<IProperty> properties)
```

Initializes a new instance of the `PropertyBag` class.

**Parameters:**

- `properties`: The collection of properties.

```csharp
public PropertyBag(params IProperty[] properties)
```

Initializes a new instance of the `PropertyBag` class.

**Parameters:**

- `properties`: The collection of properties.

## Properties

### Count

```csharp
public int Count { get; }
```

Gets the number of properties in the bag.

## Methods

### Add

```csharp
public void Add(IProperty property)
```

Adds a property to the bag.

**Parameters:**

- `property`: The property to add.

### Any

```csharp
public bool Any<TProperty>()
```

Determines whether the bag contains a property of the specified type.

**Type parameters:**

- `TProperty`: The type of the property.

**Returns:** `true` if the bag contains a property of the specified type; `false` otherwise.

### AsEnumerable

```csharp
public IEnumerable<IProperty> AsEnumerable()
```

Returns an enumerable that iterates through the collection.

**Returns:** The collection of properties.

### FirstOrDefault

```csharp
public TProperty? FirstOrDefault<TProperty>()
```

Returns the first property of the `TProperty` type, or default if none is found. Unlike `PropertyBag.SingleOrDefault`, this method does not throw when multiple properties of the same type are present — it simply returns the first one encountered.

**Type parameters:**

- `TProperty`: The type of the property.

**Returns:** The first property of the given type, or default if none is found.

### GetEnumerator

```csharp
public IEnumerator<IProperty> GetEnumerator()
```

Returns an enumerator that iterates through the collection.

**Returns:** The enumerator of `IProperty`.

### OfType

```csharp
public TProperty[] OfType<TProperty>()
```

Gets the properties of the `TProperty` type.

**Type parameters:**

- `TProperty`: The property type.

**Returns:** An array of properties matching the given type.

### Single

```csharp
public TProperty Single<TProperty>()
```

Returns the only property of the `TProperty` type, and throws an exception if there is not exactly one element.

**Type parameters:**

- `TProperty`: The type of the property.

**Returns:** The single property of the given type.

**Exceptions:**

- `InvalidOperationException`: Thrown when not exactly one property of the given type was found.

### SingleOrDefault

```csharp
public TProperty? SingleOrDefault<TProperty>()
```

Returns the only property of the `TProperty` type, or default, and throws an exception if there is more than one element.

**Type parameters:**

- `TProperty`: The type of the property.

**Returns:** The single item of the given type or default.

**Exceptions:**

- `InvalidOperationException`: Thrown when more than one property of the given type was found.
