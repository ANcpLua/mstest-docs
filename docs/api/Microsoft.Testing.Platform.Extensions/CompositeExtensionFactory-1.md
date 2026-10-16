# CompositeExtensionFactory<TExtension> class

- Namespace: `Microsoft.Testing.Platform.Extensions`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents a factory for creating composite extensions.

```csharp
public class CompositeExtensionFactory<TExtension> : ICloneable
```

**Type parameters:**

- `TExtension`: The type of the extension.

## Remarks

This helper type is used to create a composite extension that is composed of multiple extensions without having to handle either the communication between the extensions or the lifetime of the extensions instances.

## Constructors

### CompositeExtensionFactory

```csharp
public CompositeExtensionFactory(Func<IServiceProvider, TExtension> factory)
```

Initializes a new instance of the `CompositeExtensionFactory` class.

**Parameters:**

- `factory`: The factory function that creates the extension with a service provider.

```csharp
public CompositeExtensionFactory(Func<TExtension> factory)
```

Initializes a new instance of the `CompositeExtensionFactory` class.

**Parameters:**

- `factory`: The factory function that creates the extension.
