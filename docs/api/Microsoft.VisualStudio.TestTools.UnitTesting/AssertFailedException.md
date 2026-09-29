# AssertFailedException class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

AssertFailedException class. Used to indicate failure for a test case.

```csharp
public class AssertFailedException : UnitTestAssertException
```

## Constructors

### AssertFailedException

```csharp
public AssertFailedException()
```

Initializes a new instance of the `AssertFailedException` class.

```csharp
public AssertFailedException(string msg)
```

Initializes a new instance of the `AssertFailedException` class.

**Parameters:**

- `msg`: The message.

```csharp
public AssertFailedException(string msg, Exception ex)
```

Initializes a new instance of the `AssertFailedException` class.

**Parameters:**

- `msg`: The message.
- `ex`: The exception.

## Properties

### ActualText

```csharp
public string? ActualText { get; }
```

Gets the pre-formatted text representation of the actual value, as displayed in the `actual:` line of the structured assertion message. Returns `null` when the assertion has no natural actual value.

### ExpectedText

```csharp
public string? ExpectedText { get; }
```

Gets the pre-formatted text representation of the expected value, as displayed in the `expected:` line of the structured assertion message. Returns `null` when the assertion has no natural expected value (e.g. `Assert.Fail(String)`).
