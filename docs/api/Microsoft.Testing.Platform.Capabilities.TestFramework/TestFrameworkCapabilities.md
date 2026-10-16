# TestFrameworkCapabilities class

- Namespace: `Microsoft.Testing.Platform.Capabilities.TestFramework`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents the capabilities of a test framework.

```csharp
public sealed class TestFrameworkCapabilities : ITestFrameworkCapabilities, ICapabilities<ITestFrameworkCapability>
```

## Constructors

### TestFrameworkCapabilities

```csharp
public TestFrameworkCapabilities(IReadOnlyCollection<ITestFrameworkCapability> capabilities)
```

Represents the capabilities of a test framework.

```csharp
public TestFrameworkCapabilities(params ITestFrameworkCapability[] capabilities)
```

Initializes a new instance of the `TestFrameworkCapabilities` class.

**Parameters:**

- `capabilities`: The test framework capabilities.

## Properties

### Capabilities

```csharp
public IReadOnlyCollection<ITestFrameworkCapability> Capabilities { get; }
```

Gets the test framework capabilities.
