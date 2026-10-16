# UnitTestAssertException class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

Base class for Framework Exceptions.

```csharp
public abstract class UnitTestAssertException : Exception
```

## Constructors

### UnitTestAssertException

```csharp
protected UnitTestAssertException()
```

Initializes a new instance of the `UnitTestAssertException` class.

```csharp
protected UnitTestAssertException(string msg)
```

Initializes a new instance of the `UnitTestAssertException` class.

**Parameters:**

- `msg`: The message.

```csharp
protected UnitTestAssertException(string msg, Exception ex)
```

Initializes a new instance of the `UnitTestAssertException` class.

**Parameters:**

- `msg`: The message.
- `ex`: The exception.
