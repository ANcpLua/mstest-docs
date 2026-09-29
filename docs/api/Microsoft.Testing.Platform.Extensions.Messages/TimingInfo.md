# TimingInfo struct

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Information about the timing of a test node.

```csharp
public readonly struct TimingInfo : IEquatable<TimingInfo>
```

## Constructors

### TimingInfo

```csharp
public TimingInfo(
    DateTimeOffset startTime,
    DateTimeOffset endTime,
    TimeSpan duration)
```

Initializes a new instance of the `TimingInfo` struct.

**Parameters:**

- `startTime`: Test start time.
- `endTime`: Test end time.
- `duration`: Total test duration.

## Properties

### Duration

```csharp
public TimeSpan Duration { get; }
```

Gets the total test duration.

### EndTime

```csharp
public DateTimeOffset EndTime { get; }
```

Gets the test end time.

### StartTime

```csharp
public DateTimeOffset StartTime { get; }
```

Gets the test start time.

## Methods

### Equals

```csharp
public bool Equals(TimingInfo other)
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

## Operators

### Equality

```csharp
public static bool operator Equality(TimingInfo left, TimingInfo right)
```

Implementation of the equality operator.

### Inequality

```csharp
public static bool operator Inequality(TimingInfo left, TimingInfo right)
```

Implementation of the non-equality operator.
