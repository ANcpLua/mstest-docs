# ITestCoverageCapabilities interface

- Namespace: `Microsoft.Testing.Platform.Services`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Describes the test-coverage messaging capabilities available in the current test application.

```csharp
public interface ITestCoverageCapabilities
```

## Properties

### EnabledProducerUids

```csharp
IReadOnlyCollection<string> EnabledProducerUids { get; }
```

Gets the UIDs of enabled data producers that declare at least one test-coverage message type.

#### Remarks

The collection is a snapshot of the producers registered when this property is read. Extensions should query it from a test-session lifecycle callback, after extension construction has completed, rather than from their factory or constructor.

### SupportsTestCoverageMessages

```csharp
bool SupportsTestCoverageMessages { get; }
```

Gets a value indicating whether this platform supports the test-coverage message contract.
