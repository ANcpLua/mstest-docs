# AssertInconclusiveException class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

The assert inconclusive exception.

```csharp
public class AssertInconclusiveException : UnitTestAssertException
```

## Constructors

### AssertInconclusiveException

```csharp
public AssertInconclusiveException()
```

Initializes a new instance of the `AssertInconclusiveException` class.

```csharp
public AssertInconclusiveException(string msg)
```

Initializes a new instance of the `AssertInconclusiveException` class.

**Parameters:**

- `msg`: The message.

```csharp
public AssertInconclusiveException(string msg, Exception ex)
```

Initializes a new instance of the `AssertInconclusiveException` class.

**Parameters:**

- `msg`: The message.
- `ex`: The exception.
