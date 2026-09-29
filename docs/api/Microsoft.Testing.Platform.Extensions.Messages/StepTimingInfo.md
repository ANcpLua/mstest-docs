# StepTimingInfo class

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Information about the timing of a test node step.

```csharp
public sealed class StepTimingInfo : IEquatable<StepTimingInfo>
```

## Constructors

### StepTimingInfo

```csharp
public StepTimingInfo(
    string id,
    string description,
    TimingInfo timing)
```

Initializes a new instance of the `StepTimingInfo` class.

**Parameters:**

- `id`: Step identifier.
- `description`: Step description.
- `timing`: Step timing info.

## Properties

### Description

```csharp
public string Description { get; }
```

Gets the step description.

### Id

```csharp
public string Id { get; }
```

Gets the step identifier.

### Timing

```csharp
public TimingInfo Timing { get; }
```

Gets the step timing info.

## Methods

### Equals

```csharp
public bool Equals(StepTimingInfo? other)
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
