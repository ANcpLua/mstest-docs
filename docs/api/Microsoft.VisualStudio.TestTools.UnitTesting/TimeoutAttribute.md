# TimeoutAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

Timeout attribute; used to specify the timeout of a unit test.

```csharp
[AttributeUsage(AttributeTargets.Method, Inherited = false)]
public sealed class TimeoutAttribute : Attribute
```

## Constructors

### TimeoutAttribute

```csharp
public TimeoutAttribute(int timeout)
```

Initializes a new instance of the `TimeoutAttribute` class.

**Parameters:**

- `timeout`: The timeout in milliseconds.

## Properties

### CooperativeCancellation

```csharp
public bool CooperativeCancellation { get; set; }
```

Gets or sets a value indicating whether the test method should be cooperatively canceled on timeout. When set to `true`, the cancellation token is canceled on timeout, and the method completion is awaited. The test method and all the code it calls, must be designed in a way that it observes the cancellation and cancels cooperatively. If the test method does not complete, the timeout does not force it to complete. When set to `false`, the cancellation token is canceled on timeout, timeout result is reported and the method task will continue running on background. This may lead to conflicts in file access on test cleanup, unobserved exceptions, and memory leaks.

### Timeout

```csharp
public int Timeout { get; }
```

Gets the timeout in milliseconds.
