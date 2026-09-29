# TestNode class

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Represents a test node.

```csharp
public class TestNode
```

## Constructors

### TestNode

```csharp
[Obsolete("Constructors of types with required members are not supported in this version of your compiler.", true)]
public TestNode()
```

## Properties

### DisplayName

```csharp
public string DisplayName { get; init; }
```

Gets the display name of the test node.

### Properties

```csharp
public PropertyBag Properties { get; init; }
```

Gets the properties of the test node.

### Uid

```csharp
public TestNodeUid Uid { get; init; }
```

Gets the unique identifier of the test node.

## Methods

### ToString

```csharp
public override string ToString()
```
