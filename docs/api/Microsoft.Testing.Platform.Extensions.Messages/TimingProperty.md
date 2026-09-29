# TimingProperty class

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Property that represents the timing of a test node.

```csharp
public sealed class TimingProperty : IProperty, IEquatable<TimingProperty>
```

## Constructors

### TimingProperty

```csharp
public TimingProperty(TimingInfo globalTiming)
```

Initializes a new instance of the `TimingProperty` class with only global timing.

**Parameters:**

- `globalTiming`: The global timing information.

```csharp
public TimingProperty(TimingInfo globalTiming, StepTimingInfo[] stepTimings)
```

Initializes a new instance of the `TimingProperty` class with global and step timings.

**Parameters:**

- `globalTiming`: The global timing information.
- `stepTimings`: The step timing information.

## Properties

### GlobalTiming

```csharp
public TimingInfo GlobalTiming { get; }
```

Gets the global timing information.

### StepTimings

```csharp
public StepTimingInfo[] StepTimings { get; }
```

Gets the step timing information.

## Methods

### Equals

```csharp
public bool Equals(TimingProperty? other)
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
