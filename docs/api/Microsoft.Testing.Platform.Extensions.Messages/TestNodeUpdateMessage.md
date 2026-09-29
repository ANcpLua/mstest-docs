# TestNodeUpdateMessage class

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

A message representing a test node update.

```csharp
public sealed class TestNodeUpdateMessage : DataWithSessionUid
```

## Constructors

### TestNodeUpdateMessage

```csharp
public TestNodeUpdateMessage(
    SessionUid sessionUid,
    TestNode testNode,
    TestNodeUid? parentTestNodeUid = null)
```

A message representing a test node update.

**Parameters:**

- `sessionUid`: The session UID.
- `testNode`: The test node.
- `parentTestNodeUid`: The test node parent UID.

## Properties

### ParentTestNodeUid

```csharp
public TestNodeUid? ParentTestNodeUid { get; }
```

Gets the parent test node UID.

### TestNode

```csharp
public TestNode TestNode { get; }
```

Gets the test node.

## Methods

### ToString

```csharp
public override string ToString()
```
