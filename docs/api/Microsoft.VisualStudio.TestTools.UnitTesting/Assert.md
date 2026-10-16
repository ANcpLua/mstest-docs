# Assert class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

A collection of helper classes to test various conditions within unit tests. If the condition being tested is not met, an exception is thrown.

```csharp
public sealed class Assert
```

## Properties

### That

```csharp
public static Assert That { get; }
```

Gets the singleton instance of the Assert functionality.

#### Remarks

Users can use this to plug-in custom assertions through C# extension methods. For instance, the signature of a custom assertion provider could be `public static void IsOfType<T>(this Assert assert, object obj)` and the call-site would be `Assert.That.IsOfType<Dog>(animal);`. For more information, see [Create custom assertions with Assert.That](https://learn.microsoft.com/dotnet/core/testing/unit-testing-mstest-writing-tests-assertions#create-custom-assertions-with-assertthat).

#### Example

The following example defines a custom `IsPrime` assertion as an extension method on `Assert` and invokes it through `Assert.That`:

```csharp
using System;
using System.Linq;
using Microsoft.VisualStudio.TestTools.UnitTesting;
            
public static class CustomAssertExtensions
{
    public static void IsPrime(this Assert assert, int value)
    {
        if (value < 2 || Enumerable.Range(2, (int)Math.Sqrt(value) - 1).Any(i => value % i == 0))
        {
            throw new AssertFailedException($"Assert.That.IsPrime failed. Value <{value}> is not a prime number.");
        }
    }
}
            
[TestClass]
public class CalculatorTests
{
    [TestMethod]
    public void NextPrime_ReturnsPrime()
    {
        int result = new Calculator().NextPrime(10);
        Assert.That.IsPrime(result);
    }
}
```

## Methods

### AddValueFormatter

```csharp
[Experimental("MSTESTEXP", UrlFormat = "https://aka.ms/mstest/diagnostics#{0}")]
public static IDisposable AddValueFormatter(Func<Func<object?, string>, Func<object?, string>> factory)
```

Registers a chain-of-responsibility value-formatter factory. The factory receives the `next` formatter in the chain and returns a new formatter; the returned formatter should either produce a string for the values it handles or delegate to `next` for the values it does not handle. The registration is scoped to the current asynchronous flow and is removed when the returned `IDisposable` is disposed.

**Parameters:**

- `factory`: A function that receives the next formatter in the chain and returns a formatter to install ahead of it.

**Returns:** An `IDisposable` whose disposal removes the registration.

**Exceptions:**

- `ArgumentNullException`: `factory` is `null`.

#### Remarks

Use this overload when you need to inspect more than a single type (for example to render any object that implements a marker interface) or when you need explicit control over delegation to `next`. For the common "format a specific type" case prefer `Assert.AddValueFormatter(Func<T0,String>)`.

`factory` is the chain builder, not the formatter itself: it is invoked every time a value is rendered while the registration is active (the chain is rebuilt per render so that out-of-order disposal of other registrations is honored), not just once at registration time. Keep it cheap and side-effect free; perform any expensive setup outside the factory and have it return a formatter that closes over the precomputed state.

This API is experimental. It may change, break, or be removed at any time without notice.

```csharp
[Experimental("MSTESTEXP", UrlFormat = "https://aka.ms/mstest/diagnostics#{0}")]
public static IDisposable AddValueFormatter<T>(Func<T?, string?> formatter)
```

Registers a custom formatter that controls how values of `T` are rendered inside structured assertion failure messages. The registration is scoped to the current asynchronous flow (backed by `AsyncLocal`) and is removed when the returned `IDisposable` is disposed.

**Type parameters:**

- `T`: The type whose rendered representation should be customized.

**Parameters:**

- `formatter`: A function that returns the string representation to use, or `null` to fall through to the next registered formatter (or the built-in renderer when no other formatter handles the value).

**Returns:** An `IDisposable` whose disposal removes the registration.

**Exceptions:**

- `ArgumentNullException`: `formatter` is `null`.

#### Remarks

Formatters affect only how values are rendered in failure messages. They do not change equality comparisons performed by assertions such as `Assert.AreEqual`. To customize equality, use the existing `IEqualityComparer` overloads.

Registrations stack newest-first: the most recently registered formatter is consulted first. A formatter returning `null` defers to the next formatter, and ultimately to the built-in renderer. `null` values are always rendered as `"null"` by the built-in renderer and are never passed to user formatters.

Common registration sites and their effective scope:

- Inside a `[TestMethod]`: that test method (and its async continuations).
- `[TestInitialize]`: each test in the containing class.
- `[ClassInitialize]`: all tests in the containing class.
- `[AssemblyInitialize]`: all tests in the containing assembly.

This API is experimental. It may change, break, or be removed at any time without notice.

#### Example

```csharp
[TestMethod]
public void DateTimeFailureShowsKind()
{
    using var _ = Assert.AddValueFormatter<DateTime>(dt => $"{dt:O} [{dt.Kind}]");
    Assert.AreEqual(DateTime.UtcNow, DateTime.Now);
}
```

### AreAllDistinct

```csharp
public static void AreAllDistinct(
    [NotNull] IEnumerable collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether all items in the specified collection are distinct (no two elements are equal) and throws an exception if any two elements in the collection are equal.

**Parameters:**

- `collection`: The collection in which to search for duplicate elements.
- `message`: The message to include in the exception when `collection` contains at least one duplicate element. The message is shown in test results.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `collection` is null or contains at least one duplicate element.

```csharp
public static void AreAllDistinct<T>(
    Memory<T> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether all items in the specified memory are distinct (no two elements are equal).

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `collection`: The memory in which to search for duplicate elements.
- `message`: The message to include in the exception when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreAllDistinct<T>(
    ReadOnlyMemory<T> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether all items in the specified memory are distinct (no two elements are equal).

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `collection`: The memory in which to search for duplicate elements.
- `message`: The message to include in the exception when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreAllDistinct<T>(
    ReadOnlySpan<T> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether all items in the specified span are distinct (no two elements are equal).

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `collection`: The span in which to search for duplicate elements.
- `message`: The message to include in the exception when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreAllDistinct<T>(
    Span<T> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether all items in the specified span are distinct (no two elements are equal).

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `collection`: The span in which to search for duplicate elements.
- `message`: The message to include in the exception when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreAllDistinct<T>(
    [NotNull] IEnumerable<T> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether all items in the specified collection are distinct (no two elements are equal) and throws an exception if any two elements in the collection are equal.

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `collection`: The collection in which to search for duplicate elements.
- `message`: The message to include in the exception when `collection` contains at least one duplicate element. The message is shown in test results.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `collection` is null or contains at least one duplicate element.

```csharp
public static void AreAllDistinct<T>(
    [NotNull] T[] collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether all elements in the specified array are distinct and throws an exception if any two elements are equal.

**Type parameters:**

- `T`: The type of the array elements.

**Parameters:**

- `collection`: The array whose elements must all be distinct.
- `message`: The message to include in the exception when two equal elements are found.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression.

**Exceptions:**

- `AssertFailedException`: Thrown if any two elements in `collection` are equal.

```csharp
public static void AreAllDistinct(
    [NotNull] IEnumerable collection,
    [NotNull] IEqualityComparer comparer,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether all items in the specified collection are distinct (no two elements are equal) using the supplied `comparer` and throws an exception if any two elements in the collection are equal.

**Parameters:**

- `collection`: The collection in which to search for duplicate elements.
- `comparer`: The equality comparer to use when comparing elements.
- `message`: The message to include in the exception when `collection` contains at least one duplicate element. The message is shown in test results.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `collection` is null or contains at least one duplicate element.

```csharp
public static void AreAllDistinct<T, TCollection>(
    [NotNull] TCollection collection,
    [NotNull] IEqualityComparer<T> comparer,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether all elements in the specified collection are distinct using the specified equality comparer and throws an exception if any two elements are equal.

**Type parameters:**

- `T`: The type of the collection elements.
- `TCollection`: The concrete type of the collection.

**Parameters:**

- `collection`: The collection whose elements must all be distinct.
- `comparer`: The equality comparer to use when comparing elements.
- `message`: The message to include in the exception when two equal elements are found.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if any two elements in `collection` are equal.

```csharp
public static void AreAllDistinct<T>(
    Memory<T> collection,
    [NotNull] IEqualityComparer<T> comparer,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether all items in the specified memory are distinct (no two elements are equal) using the supplied `comparer`.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `collection`: The memory in which to search for duplicate elements.
- `comparer`: The equality comparer to use when comparing elements.
- `message`: The message to include in the exception when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreAllDistinct<T>(
    ReadOnlyMemory<T> collection,
    [NotNull] IEqualityComparer<T> comparer,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether all items in the specified memory are distinct (no two elements are equal) using the supplied `comparer`.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `collection`: The memory in which to search for duplicate elements.
- `comparer`: The equality comparer to use when comparing elements.
- `message`: The message to include in the exception when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreAllDistinct<T>(
    ReadOnlySpan<T> collection,
    [NotNull] IEqualityComparer<T> comparer,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether all items in the specified span are distinct (no two elements are equal) using the supplied `comparer`.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `collection`: The span in which to search for duplicate elements.
- `comparer`: The equality comparer to use when comparing elements.
- `message`: The message to include in the exception when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreAllDistinct<T>(
    Span<T> collection,
    [NotNull] IEqualityComparer<T> comparer,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether all items in the specified span are distinct (no two elements are equal) using the supplied `comparer`.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `collection`: The span in which to search for duplicate elements.
- `comparer`: The equality comparer to use when comparing elements.
- `message`: The message to include in the exception when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreAllDistinct<T>(
    [NotNull] IEnumerable<T> collection,
    [NotNull] IEqualityComparer<T> comparer,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether all items in the specified collection are distinct (no two elements are equal) using the supplied `comparer` and throws an exception if any two elements in the collection are equal.

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `collection`: The collection in which to search for duplicate elements.
- `comparer`: The equality comparer to use when comparing elements.
- `message`: The message to include in the exception when `collection` contains at least one duplicate element. The message is shown in test results.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `collection` is null or contains at least one duplicate element.

```csharp
public static void AreAllDistinct<T>(
    [NotNull] T[] collection,
    [NotNull] IEqualityComparer<T> comparer,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether all elements in the specified array are distinct using the specified equality comparer and throws an exception if any two elements are equal.

**Type parameters:**

- `T`: The type of the array elements.

**Parameters:**

- `collection`: The array whose elements must all be distinct.
- `comparer`: The equality comparer to use when comparing elements.
- `message`: The message to include in the exception when two equal elements are found.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression.

**Exceptions:**

- `AssertFailedException`: Thrown if any two elements in `collection` are equal.

### AreAllNotNull

```csharp
public static void AreAllNotNull(
    [NotNull] IEnumerable collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether all items in the specified collection are non-null and throws an exception if any element is null.

**Parameters:**

- `collection`: The collection in which to search for null elements.
- `message`: The message to include in the exception when `collection` contains a null element. The message is shown in test results.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `collection` is null or contains at least one null element.

```csharp
public static void AreAllNotNull<T>(
    Memory<T> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether all items in the specified memory are non-null.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `collection`: The memory in which to search for null elements.
- `message`: The message to include in the exception when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreAllNotNull<T>(
    ReadOnlyMemory<T> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether all items in the specified memory are non-null.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `collection`: The memory in which to search for null elements.
- `message`: The message to include in the exception when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreAllNotNull<T>(
    ReadOnlySpan<T> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether all items in the specified span are non-null.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `collection`: The span in which to search for null elements.
- `message`: The message to include in the exception when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreAllNotNull<T>(
    Span<T> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether all items in the specified span are non-null.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `collection`: The span in which to search for null elements.
- `message`: The message to include in the exception when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreAllNotNull<T>(
    [NotNull] IEnumerable<T> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether all items in the specified collection are non-null and throws an exception if any element is null.

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `collection`: The collection in which to search for null elements.
- `message`: The message to include in the exception when `collection` contains a null element. The message is shown in test results.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `collection` is null or contains at least one null element.

```csharp
public static void AreAllNotNull<T>(
    [NotNull] T[] collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether all items in the specified array are non-null.

**Type parameters:**

- `T`: The type of the array items.

**Parameters:**

- `collection`: The array in which to search for null elements.
- `message`: The message to include in the exception when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

### AreAllOfType

```csharp
public static void AreAllOfType<TExpected, TItem>(
    Memory<TItem> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether all elements in the specified memory are instances of (or derived from) `TExpected`.

**Type parameters:**

- `TExpected`: The type each element of `collection` is expected to be.
- `TItem`: The element type of the memory.

**Parameters:**

- `collection`: The memory containing elements the test expects to be of the specified type.
- `message`: The message to include in the exception when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreAllOfType<TExpected, TItem>(
    ReadOnlyMemory<TItem> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether all elements in the specified memory are instances of (or derived from) `TExpected`.

**Type parameters:**

- `TExpected`: The type each element of `collection` is expected to be.
- `TItem`: The element type of the memory.

**Parameters:**

- `collection`: The memory containing elements the test expects to be of the specified type.
- `message`: The message to include in the exception when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreAllOfType<TExpected, TItem>(
    ReadOnlySpan<TItem> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether all elements in the specified span are instances of (or derived from) `TExpected`.

**Type parameters:**

- `TExpected`: The type each element of `collection` is expected to be.
- `TItem`: The element type of the span.

**Parameters:**

- `collection`: The span containing elements the test expects to be of the specified type.
- `message`: The message to include in the exception when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreAllOfType<TExpected, TItem>(
    Span<TItem> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether all elements in the specified span are instances of (or derived from) `TExpected`.

**Type parameters:**

- `TExpected`: The type each element of `collection` is expected to be.
- `TItem`: The element type of the span.

**Parameters:**

- `collection`: The span containing elements the test expects to be of the specified type.
- `message`: The message to include in the exception when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreAllOfType<TExpected>(
    [NotNull] IEnumerable collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether all elements in the specified collection are instances of (or derived from) the expected type and throws an exception if the expected type is not in the inheritance hierarchy of one or more of the elements, or if any element is null.

**Type parameters:**

- `TExpected`: The type each element of `collection` is expected to be.

**Parameters:**

- `collection`: The collection containing elements the test expects to be of the specified type.
- `message`: The message to include in the exception when an element in `collection` is null or not an instance of `TExpected`. The message is shown in test results.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `collection` is null or some elements of `collection` are null or do not inherit from / implement `TExpected`.

```csharp
public static void AreAllOfType(
    [NotNull] Type expectedType,
    [NotNull] IEnumerable collection,
    string? message = "",
    [CallerArgumentExpression("expectedType")] string expectedTypeExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether all elements in the specified collection are instances of (or derived from) the expected type and throws an exception if the expected type is not in the inheritance hierarchy of one or more of the elements, or if any element is null.

**Parameters:**

- `expectedType`: The expected type of each element of `collection`.
- `collection`: The collection containing elements the test expects to be of the specified type.
- `message`: The message to include in the exception when an element in `collection` is null or not an instance of `expectedType`. The message is shown in test results.
- `expectedTypeExpression`: The syntactic expression of expectedType as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `expectedType` or `collection` is null, or some elements of `collection` are null or do not inherit from / implement `expectedType`.

```csharp
public static void AreAllOfType<TItem>(
    [NotNull] Type expectedType,
    Memory<TItem> collection,
    string? message = "",
    [CallerArgumentExpression("expectedType")] string expectedTypeExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether all elements in the specified memory are instances of (or derived from) the expected type.

**Type parameters:**

- `TItem`: The element type of the memory.

**Parameters:**

- `expectedType`: The expected type of each element of `collection`.
- `collection`: The memory containing elements the test expects to be of the specified type.
- `message`: The message to include in the exception when the assertion fails.
- `expectedTypeExpression`: The syntactic expression of expectedType as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreAllOfType<TItem>(
    [NotNull] Type expectedType,
    ReadOnlyMemory<TItem> collection,
    string? message = "",
    [CallerArgumentExpression("expectedType")] string expectedTypeExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether all elements in the specified memory are instances of (or derived from) the expected type.

**Type parameters:**

- `TItem`: The element type of the memory.

**Parameters:**

- `expectedType`: The expected type of each element of `collection`.
- `collection`: The memory containing elements the test expects to be of the specified type.
- `message`: The message to include in the exception when the assertion fails.
- `expectedTypeExpression`: The syntactic expression of expectedType as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreAllOfType<TItem>(
    [NotNull] Type expectedType,
    ReadOnlySpan<TItem> collection,
    string? message = "",
    [CallerArgumentExpression("expectedType")] string expectedTypeExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether all elements in the specified span are instances of (or derived from) the expected type.

**Type parameters:**

- `TItem`: The element type of the span.

**Parameters:**

- `expectedType`: The expected type of each element of `collection`.
- `collection`: The span containing elements the test expects to be of the specified type.
- `message`: The message to include in the exception when the assertion fails.
- `expectedTypeExpression`: The syntactic expression of expectedType as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreAllOfType<TItem>(
    [NotNull] Type expectedType,
    Span<TItem> collection,
    string? message = "",
    [CallerArgumentExpression("expectedType")] string expectedTypeExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether all elements in the specified span are instances of (or derived from) the expected type.

**Type parameters:**

- `TItem`: The element type of the span.

**Parameters:**

- `expectedType`: The expected type of each element of `collection`.
- `collection`: The span containing elements the test expects to be of the specified type.
- `message`: The message to include in the exception when the assertion fails.
- `expectedTypeExpression`: The syntactic expression of expectedType as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

### AreEqual

```csharp
public static void AreEqual<T>(
    T? expected,
    T? actual,
    ref Assert.AssertAreEqualInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified values are equal and throws an exception if the two values are not equal. The equality is computed using the default `EqualityComparer`.

**Type parameters:**

- `T`: The type of values to compare.

**Parameters:**

- `expected`: The first value to compare. This is the value the tests expects.
- `actual`: The second value to compare. This is the value produced by the code under test.
- `message`: The message to include in the exception when `actual` is not equal to `expected`. The message is shown in test results.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `expected` is not equal to `actual`.

```csharp
public static void AreEqual<T>(
    T? expected,
    T? actual,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified values are equal and throws an exception if the two values are not equal. The equality is computed using the default `EqualityComparer`.

**Type parameters:**

- `T`: The type of values to compare.

**Parameters:**

- `expected`: The first value to compare. This is the value the tests expects.
- `actual`: The second value to compare. This is the value produced by the code under test.
- `message`: The message to include in the exception when `actual` is not equal to `expected`. The message is shown in test results.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `expected` is not equal to `actual`.

```csharp
public static void AreEqual(
    decimal expected,
    decimal actual,
    decimal delta,
    ref Assert.AssertNonGenericAreEqualInterpolatedStringHandler message,
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified decimals are equal and throws an exception if they are not equal.

**Parameters:**

- `expected`: The first decimal to compare. This is the decimal the tests expects.
- `actual`: The second decimal to compare. This is the decimal produced by the code under test.
- `delta`: The required accuracy. An exception will be thrown only if `actual` is different than `expected` by more than `delta`.
- `message`: The message to include in the exception when `actual` is different than `expected` by more than `delta`. The message is shown in test results.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `expected` is not equal to `actual`.

```csharp
public static void AreEqual(
    decimal expected,
    decimal actual,
    decimal delta,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified decimals are equal and throws an exception if they are not equal.

**Parameters:**

- `expected`: The first decimal to compare. This is the decimal the tests expects.
- `actual`: The second decimal to compare. This is the decimal produced by the code under test.
- `delta`: The required accuracy. An exception will be thrown only if `actual` is different than `expected` by more than `delta`.
- `message`: The message to include in the exception when `actual` is different than `expected` by more than `delta`. The message is shown in test results.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `expected` is not equal to `actual`.

```csharp
public static void AreEqual(
    double expected,
    double actual,
    double delta,
    ref Assert.AssertNonGenericAreEqualInterpolatedStringHandler message,
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified doubles are equal and throws an exception if they are not equal.

**Parameters:**

- `expected`: The first double to compare. This is the double the tests expects.
- `actual`: The second double to compare. This is the double produced by the code under test.
- `delta`: The required accuracy. An exception will be thrown only if `actual` is different than `expected` by more than `delta`.
- `message`: The message to include in the exception when `actual` is different than `expected` by more than `delta`. The message is shown in test results.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `expected` is not equal to `actual`.

```csharp
public static void AreEqual(
    double expected,
    double actual,
    double delta,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified doubles are equal and throws an exception if they are not equal.

**Parameters:**

- `expected`: The first double to compare. This is the double the tests expects.
- `actual`: The second double to compare. This is the double produced by the code under test.
- `delta`: The required accuracy. An exception will be thrown only if `actual` is different than `expected` by more than `delta`.
- `message`: The message to include in the exception when `actual` is different than `expected` by more than `delta`. The message is shown in test results.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `expected` is not equal to `actual`.

```csharp
public static void AreEqual(
    float expected,
    float actual,
    float delta,
    ref Assert.AssertNonGenericAreEqualInterpolatedStringHandler message,
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified floats are equal and throws an exception if they are not equal.

**Parameters:**

- `expected`: The first float to compare. This is the float the tests expects.
- `actual`: The second float to compare. This is the float produced by the code under test.
- `delta`: The required accuracy. An exception will be thrown only if `actual` is different than `expected` by more than `delta`.
- `message`: The message to include in the exception when `actual` is different than `expected` by more than `delta`. The message is shown in test results.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `expected` is not equal to `actual`.

```csharp
public static void AreEqual(
    float expected,
    float actual,
    float delta,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified floats are equal and throws an exception if they are not equal.

**Parameters:**

- `expected`: The first float to compare. This is the float the tests expects.
- `actual`: The second float to compare. This is the float produced by the code under test.
- `delta`: The required accuracy. An exception will be thrown only if `actual` is different than `expected` by more than `delta`.
- `message`: The message to include in the exception when `actual` is different than `expected` by more than `delta`. The message is shown in test results.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `expected` is not equal to `actual`.

```csharp
public static void AreEqual(
    long expected,
    long actual,
    long delta,
    ref Assert.AssertNonGenericAreEqualInterpolatedStringHandler message,
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified longs are equal and throws an exception if they are not equal.

**Parameters:**

- `expected`: The first long to compare. This is the long the tests expects.
- `actual`: The second long to compare. This is the long produced by the code under test.
- `delta`: The required accuracy. An exception will be thrown only if `actual` is different than `expected` by more than `delta`.
- `message`: The message to include in the exception when `actual` is different than `expected` by more than `delta`. The message is shown in test results.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `expected` is not equal to `actual`.

```csharp
public static void AreEqual(
    long expected,
    long actual,
    long delta,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified longs are equal and throws an exception if they are not equal.

**Parameters:**

- `expected`: The first long to compare. This is the long the tests expects.
- `actual`: The second long to compare. This is the long produced by the code under test.
- `delta`: The required accuracy. An exception will be thrown only if `actual` is different than `expected` by more than `delta`.
- `message`: The message to include in the exception when `actual` is different than `expected` by more than `delta`. The message is shown in test results.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `expected` is not equal to `actual`.

```csharp
public static void AreEqual(
    string? expected,
    string? actual,
    bool ignoreCase,
    ref Assert.AssertNonGenericAreEqualInterpolatedStringHandler message,
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified strings are equal and throws an exception if they are not equal. The invariant culture is used for the comparison.

**Parameters:**

- `expected`: The first string to compare. This is the string the tests expects.
- `actual`: The second string to compare. This is the string produced by the code under test.
- `ignoreCase`: A Boolean indicating a case-sensitive or insensitive comparison. (true indicates a case-insensitive comparison.)
- `message`: The message to include in the exception when `actual` is not equal to `expected`. The message is shown in test results.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `expected` is not equal to `actual`.

```csharp
public static void AreEqual(
    string? expected,
    string? actual,
    bool ignoreCase,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified strings are equal and throws an exception if they are not equal. The invariant culture is used for the comparison.

**Parameters:**

- `expected`: The first string to compare. This is the string the tests expects.
- `actual`: The second string to compare. This is the string produced by the code under test.
- `ignoreCase`: A Boolean indicating a case-sensitive or insensitive comparison. (true indicates a case-insensitive comparison.)
- `message`: The message to include in the exception when `actual` is not equal to `expected`. The message is shown in test results.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `expected` is not equal to `actual`.

```csharp
public static void AreEqual<T>(
    T? expected,
    T? actual,
    IEqualityComparer<T> comparer,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified values are equal and throws an exception if the two values are not equal. The equality is computed using the provided `comparer` parameter.

**Type parameters:**

- `T`: The type of values to compare.

**Parameters:**

- `expected`: The first value to compare. This is the value the tests expects.
- `actual`: The second value to compare. This is the value produced by the code under test.
- `comparer`: The `IEqualityComparer` implementation to use when comparing keys, or null to use the default `EqualityComparer`.
- `message`: The message to include in the exception when `actual` is not equal to `expected`. The message is shown in test results.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `expected` is not equal to `actual`.

```csharp
public static void AreEqual<T>(
    T? expected,
    T? actual,
    IEqualityComparer<T>? comparer,
    ref Assert.AssertAreEqualInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified values are equal and throws an exception if the two values are not equal. The equality is computed using the provided `comparer` parameter.

**Type parameters:**

- `T`: The type of values to compare.

**Parameters:**

- `expected`: The first value to compare. This is the value the tests expects.
- `actual`: The second value to compare. This is the value produced by the code under test.
- `comparer`: The `IEqualityComparer` implementation to use when comparing keys, or null to use the default `EqualityComparer`.
- `message`: The message to include in the exception when `actual` is not equal to `expected`. The message is shown in test results.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `expected` is not equal to `actual`.

```csharp
public static void AreEqual(
    string? expected,
    string? actual,
    bool ignoreCase,
    CultureInfo culture,
    ref Assert.AssertNonGenericAreEqualInterpolatedStringHandler message,
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified strings are equal and throws an exception if they are not equal.

**Parameters:**

- `expected`: The first string to compare. This is the string the tests expects.
- `actual`: The second string to compare. This is the string produced by the code under test.
- `ignoreCase`: A Boolean indicating a case-sensitive or insensitive comparison. (true indicates a case-insensitive comparison.)
- `culture`: A CultureInfo object that supplies culture-specific comparison information. If culture is null, the current culture is used.
- `message`: The message to include in the exception when `actual` is not equal to `expected`. The message is shown in test results.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `expected` is not equal to `actual`.

```csharp
public static void AreEqual(
    string? expected,
    string? actual,
    bool ignoreCase,
    CultureInfo culture,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified strings are equal and throws an exception if they are not equal.

**Parameters:**

- `expected`: The first string to compare. This is the string the tests expects.
- `actual`: The second string to compare. This is the string produced by the code under test.
- `ignoreCase`: A Boolean indicating a case-sensitive or insensitive comparison. (true indicates a case-insensitive comparison.)
- `culture`: A CultureInfo object that supplies culture-specific comparison information. If culture is null, the current culture is used.
- `message`: The message to include in the exception when `actual` is not equal to `expected`. The message is shown in test results.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `expected` is not equal to `actual`.

### AreEquivalent

```csharp
public static void AreEquivalent<T>(
    Memory<T> expected,
    Memory<T> actual,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two memory regions are structurally equivalent (deep, order-sensitive element comparison).

**Type parameters:**

- `T`: The element type of the memory regions.

**Parameters:**

- `expected`: The memory the test expects.
- `actual`: The memory produced by the code under test.
- `message`: The message to include in the exception when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreEquivalent<T>(
    ReadOnlyMemory<T> expected,
    ReadOnlyMemory<T> actual,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two memory regions are structurally equivalent (deep, order-sensitive element comparison).

**Type parameters:**

- `T`: The element type of the memory regions.

**Parameters:**

- `expected`: The memory the test expects.
- `actual`: The memory produced by the code under test.
- `message`: The message to include in the exception when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreEquivalent<T>(
    ReadOnlySpan<T> expected,
    ReadOnlySpan<T> actual,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two spans are structurally equivalent (deep, order-sensitive element comparison).

**Type parameters:**

- `T`: The element type of the spans.

**Parameters:**

- `expected`: The span the test expects.
- `actual`: The span produced by the code under test.
- `message`: The message to include in the exception when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreEquivalent<T>(
    Span<T> expected,
    Span<T> actual,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two spans are structurally equivalent (deep, order-sensitive element comparison).

**Type parameters:**

- `T`: The element type of the spans.

**Parameters:**

- `expected`: The span the test expects.
- `actual`: The span produced by the code under test.
- `message`: The message to include in the exception when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreEquivalent<T>(
    T? expected,
    T? actual,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two object graphs are structurally equivalent (deep equality) and throws an exception if they are not.

**Type parameters:**

- `T`: The type of values to compare.

**Parameters:**

- `expected`: The first value to compare. This is the value the test expects.
- `actual`: The second value to compare. This is the value produced by the code under test.
- `message`: The message to include in the exception when `actual` is not equivalent to `expected`. The message is shown in test results.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `expected` and `actual` are not structurally equivalent.

#### Remarks

This assertion performs a deep, order-sensitive structural comparison of two object graphs. It differs from `CollectionAssert.AreEquivalent(ICollection,ICollection)`, which checks only top-level collection equivalence without regard to element order.

The comparison rules are:

- Reference-equal values (including both `null`) are considered equivalent.
- Primitive-like types (numerics, `Boolean`, `Char`, `String`, enums, `DateTime`, `DateTimeOffset`, `TimeSpan`, `Guid`, `Uri`, `Type`, `Version`) are compared with `Object.Equals(Object)`. On target frameworks that ship them, `DateOnly`, `TimeOnly`, `Half`, `Int128`, and `UInt128` are also treated as primitive-like.
- If the static (compile-time) type of a value implements `IEquatable` for itself, `IEquatable.Equals(T0)` is used and recursion stops at that point. Plain `Object.Equals(Object)` overrides are ignored — the comparer always recurses into members for those.
- Dictionaries (`IDictionary`, `IDictionary`, or `IReadOnlyDictionary`) are compared by key set, with values compared recursively. Lookups are routed through the source dictionary so its `IEqualityComparer` for keys is preserved.
- Other enumerables (excluding `String`) are compared element-by-element in the iteration order. Comparison is **order-sensitive**; if order is irrelevant, use `CollectionAssert.AreEquivalent(ICollection,ICollection)` on the collection itself.
- Other reference types are compared by recursing into all public instance properties (with a public getter and no index parameters) and public instance fields. Static, non-public, and indexed members are ignored.
- Reference cycles are tracked and traversed at most once per (expected, actual) pair. The same mechanism enforces graph topology: if the same reference on one side is paired with different references on the other side, the assertion fails.
- If a user-defined `IEquatable.Equals(T0)`, member getter, or dictionary access (`TryGetValue`, `ContainsKey`, or enumeration) throws while being evaluated, the assertion fails with a message describing the exception type and message.
- Comparison stops after a bounded recursion depth to avoid `StackOverflowException` on unusually deep object graphs, and reports that condition as an assertion failure.

```csharp
public static void AreEquivalent<T>(
    Memory<T> expected,
    Memory<T> actual,
    bool strict,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two memory regions are structurally equivalent (deep, order-sensitive element comparison).

**Type parameters:**

- `T`: The element type of the memory regions.

**Parameters:**

- `expected`: The memory the test expects.
- `actual`: The memory produced by the code under test.
- `strict`: When `true`, the comparison is performed in strict mode.
- `message`: The message to include in the exception when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreEquivalent<T>(
    ReadOnlyMemory<T> expected,
    ReadOnlyMemory<T> actual,
    bool strict,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two memory regions are structurally equivalent (deep, order-sensitive element comparison).

**Type parameters:**

- `T`: The element type of the memory regions.

**Parameters:**

- `expected`: The memory the test expects.
- `actual`: The memory produced by the code under test.
- `strict`: When `true`, the comparison is performed in strict mode.
- `message`: The message to include in the exception when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreEquivalent<T>(
    ReadOnlySpan<T> expected,
    ReadOnlySpan<T> actual,
    bool strict,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two spans are structurally equivalent (deep, order-sensitive element comparison).

**Type parameters:**

- `T`: The element type of the spans.

**Parameters:**

- `expected`: The span the test expects.
- `actual`: The span produced by the code under test.
- `strict`: When `true`, the comparison is performed in strict mode.
- `message`: The message to include in the exception when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreEquivalent<T>(
    Span<T> expected,
    Span<T> actual,
    bool strict,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two spans are structurally equivalent (deep, order-sensitive element comparison).

**Type parameters:**

- `T`: The element type of the spans.

**Parameters:**

- `expected`: The span the test expects.
- `actual`: The span produced by the code under test.
- `strict`: When `true`, the comparison is performed in strict mode.
- `message`: The message to include in the exception when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreEquivalent<T>(
    T? expected,
    T? actual,
    bool strict,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two object graphs are structurally equivalent (deep equality) and throws an exception if they are not.

**Type parameters:**

- `T`: The type of values to compare.

**Parameters:**

- `expected`: The first value to compare. This is the value the test expects.
- `actual`: The second value to compare. This is the value produced by the code under test.
- `strict`: When `true`, the comparison fails if `actual` declares any public properties or fields that are not present on `expected`'s runtime type, or if any extra dictionary keys are present on `actual`. When `false` (the default), additional members and dictionary keys on `actual` are ignored. When the runtime types of `expected` and `actual` are identical, this flag has no effect on the public-member comparison, but it still rejects extra dictionary keys on `actual` when comparing dictionaries.
- `message`: The message to include in the exception when `actual` is not equivalent to `expected`. The message is shown in test results.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `expected` and `actual` are not structurally equivalent.

### AreNotEqual

```csharp
public static void AreNotEqual<T>(
    T? notExpected,
    T? actual,
    ref Assert.AssertAreNotEqualInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified values are unequal and throws an exception if the two values are equal. The equality is computed using the default `EqualityComparer`.

**Type parameters:**

- `T`: The type of values to compare.

**Parameters:**

- `notExpected`: The first value to compare. This is the value the test expects not to match `actual`.
- `actual`: The second value to compare. This is the value produced by the code under test.
- `message`: The message to include in the exception when `actual` is equal to `notExpected`. The message is shown in test results.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `notExpected` is equal to `actual`.

```csharp
public static void AreNotEqual<T>(
    T? notExpected,
    T? actual,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified values are unequal and throws an exception if the two values are equal. The equality is computed using the default `EqualityComparer`.

**Type parameters:**

- `T`: The type of values to compare.

**Parameters:**

- `notExpected`: The first value to compare. This is the value the test expects not to match `actual`.
- `actual`: The second value to compare. This is the value produced by the code under test.
- `message`: The message to include in the exception when `actual` is equal to `notExpected`. The message is shown in test results.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `notExpected` is equal to `actual`.

```csharp
public static void AreNotEqual(
    decimal notExpected,
    decimal actual,
    decimal delta,
    ref Assert.AssertNonGenericAreNotEqualInterpolatedStringHandler message,
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified decimals are unequal and throws an exception if they are equal.

**Parameters:**

- `notExpected`: The first decimal to compare. This is the decimal the test expects not to match `actual`.
- `actual`: The second decimal to compare. This is the decimal produced by the code under test.
- `delta`: The required accuracy. An exception will be thrown only if `actual` is different than `notExpected` by at most `delta`.
- `message`: The message to include in the exception when `actual` is equal to `notExpected` or different by less than `delta`. The message is shown in test results.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `notExpected` is equal to `actual`.

```csharp
public static void AreNotEqual(
    decimal notExpected,
    decimal actual,
    decimal delta,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified decimals are unequal and throws an exception if they are equal.

**Parameters:**

- `notExpected`: The first decimal to compare. This is the decimal the test expects not to match `actual`.
- `actual`: The second decimal to compare. This is the decimal produced by the code under test.
- `delta`: The required accuracy. An exception will be thrown only if `actual` is different than `notExpected` by at most `delta`.
- `message`: The message to include in the exception when `actual` is equal to `notExpected` or different by less than `delta`. The message is shown in test results.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `notExpected` is equal to `actual`.

```csharp
public static void AreNotEqual(
    double notExpected,
    double actual,
    double delta,
    ref Assert.AssertNonGenericAreNotEqualInterpolatedStringHandler message,
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified doubles are unequal and throws an exception if they are equal.

**Parameters:**

- `notExpected`: The first double to compare. This is the double the test expects not to match `actual`.
- `actual`: The second double to compare. This is the double produced by the code under test.
- `delta`: The required accuracy. An exception will be thrown only if `actual` is different than `notExpected` by at most `delta`.
- `message`: The message to include in the exception when `actual` is equal to `notExpected` or different by less than `delta`. The message is shown in test results.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `notExpected` is equal to `actual`.

```csharp
public static void AreNotEqual(
    double notExpected,
    double actual,
    double delta,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified doubles are unequal and throws an exception if they are equal.

**Parameters:**

- `notExpected`: The first double to compare. This is the double the test expects not to match `actual`.
- `actual`: The second double to compare. This is the double produced by the code under test.
- `delta`: The required accuracy. An exception will be thrown only if `actual` is different than `notExpected` by at most `delta`.
- `message`: The message to include in the exception when `actual` is equal to `notExpected` or different by less than `delta`. The message is shown in test results.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `notExpected` is equal to `actual`.

```csharp
public static void AreNotEqual(
    float notExpected,
    float actual,
    float delta,
    ref Assert.AssertNonGenericAreNotEqualInterpolatedStringHandler message,
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified floats are unequal and throws an exception if they are equal.

**Parameters:**

- `notExpected`: The first float to compare. This is the float the test expects not to match `actual`.
- `actual`: The second float to compare. This is the float produced by the code under test.
- `delta`: The required accuracy. An exception will be thrown only if `actual` is different than `notExpected` by at most `delta`.
- `message`: The message to include in the exception when `actual` is equal to `notExpected` or different by less than `delta`. The message is shown in test results.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `notExpected` is equal to `actual`.

```csharp
public static void AreNotEqual(
    float notExpected,
    float actual,
    float delta,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified floats are unequal and throws an exception if they are equal.

**Parameters:**

- `notExpected`: The first float to compare. This is the float the test expects not to match `actual`.
- `actual`: The second float to compare. This is the float produced by the code under test.
- `delta`: The required accuracy. An exception will be thrown only if `actual` is different than `notExpected` by at most `delta`.
- `message`: The message to include in the exception when `actual` is equal to `notExpected` or different by less than `delta`. The message is shown in test results.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `notExpected` is equal to `actual`.

```csharp
public static void AreNotEqual(
    long notExpected,
    long actual,
    long delta,
    ref Assert.AssertNonGenericAreNotEqualInterpolatedStringHandler message,
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified longs are unequal and throws an exception if they are equal.

**Parameters:**

- `notExpected`: The first long to compare. This is the long the test expects not to match `actual`.
- `actual`: The second long to compare. This is the long produced by the code under test.
- `delta`: The required accuracy. An exception will be thrown only if `actual` is different than `notExpected` by at most `delta`.
- `message`: The message to include in the exception when `actual` is equal to `notExpected` or different by less than `delta`. The message is shown in test results.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `notExpected` is equal to `actual`.

```csharp
public static void AreNotEqual(
    long notExpected,
    long actual,
    long delta,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified longs are unequal and throws an exception if they are equal.

**Parameters:**

- `notExpected`: The first long to compare. This is the long the test expects not to match `actual`.
- `actual`: The second long to compare. This is the long produced by the code under test.
- `delta`: The required accuracy. An exception will be thrown only if `actual` is different than `notExpected` by at most `delta`.
- `message`: The message to include in the exception when `actual` is equal to `notExpected` or different by less than `delta`. The message is shown in test results.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `notExpected` is equal to `actual`.

```csharp
public static void AreNotEqual(
    string? notExpected,
    string? actual,
    bool ignoreCase,
    ref Assert.AssertNonGenericAreNotEqualInterpolatedStringHandler message,
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified strings are unequal and throws an exception if they are equal. The invariant culture is used for the comparison.

**Parameters:**

- `notExpected`: The first string to compare. This is the string the test expects not to match `actual`.
- `actual`: The second string to compare. This is the string produced by the code under test.
- `ignoreCase`: A Boolean indicating a case-sensitive or insensitive comparison. (true indicates a case-insensitive comparison.)
- `message`: The message to include in the exception when `actual` is equal to `notExpected`. The message is shown in test results.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `notExpected` is equal to `actual`.

```csharp
public static void AreNotEqual(
    string? notExpected,
    string? actual,
    bool ignoreCase,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified strings are unequal and throws an exception if they are equal. The invariant culture is used for the comparison.

**Parameters:**

- `notExpected`: The first string to compare. This is the string the test expects not to match `actual`.
- `actual`: The second string to compare. This is the string produced by the code under test.
- `ignoreCase`: A Boolean indicating a case-sensitive or insensitive comparison. (true indicates a case-insensitive comparison.)
- `message`: The message to include in the exception when `actual` is equal to `notExpected`. The message is shown in test results.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `notExpected` is equal to `actual`.

```csharp
public static void AreNotEqual<T>(
    T? notExpected,
    T? actual,
    IEqualityComparer<T> comparer,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified values are unequal and throws an exception if the two values are equal. The equality is computed using the provided `comparer` parameter.

**Type parameters:**

- `T`: The type of values to compare.

**Parameters:**

- `notExpected`: The first value to compare. This is the value the test expects not to match `actual`.
- `actual`: The second value to compare. This is the value produced by the code under test.
- `comparer`: The `IEqualityComparer` implementation to use when comparing keys, or null to use the default `EqualityComparer`.
- `message`: The message to include in the exception when `actual` is equal to `notExpected`. The message is shown in test results.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `notExpected` is equal to `actual`.

```csharp
public static void AreNotEqual<T>(
    T? notExpected,
    T? actual,
    IEqualityComparer<T?> comparer,
    ref Assert.AssertAreNotEqualInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified values are unequal and throws an exception if the two values are equal. The equality is computed using the default `EqualityComparer`.

**Type parameters:**

- `T`: The type of values to compare.

**Parameters:**

- `notExpected`: The first value to compare. This is the value the test expects not to match `actual`.
- `actual`: The second value to compare. This is the value produced by the code under test.
- `message`: The message to include in the exception when `actual` is equal to `notExpected`. The message is shown in test results.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `notExpected` is equal to `actual`.

```csharp
public static void AreNotEqual(
    string? notExpected,
    string? actual,
    bool ignoreCase,
    CultureInfo culture,
    ref Assert.AssertNonGenericAreNotEqualInterpolatedStringHandler message,
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified strings are unequal and throws an exception if they are equal.

**Parameters:**

- `notExpected`: The first string to compare. This is the string the test expects not to match `actual`.
- `actual`: The second string to compare. This is the string produced by the code under test.
- `ignoreCase`: A Boolean indicating a case-sensitive or insensitive comparison. (true indicates a case-insensitive comparison.)
- `culture`: A CultureInfo object that supplies culture-specific comparison information. If culture is null, the current culture is used.
- `message`: The message to include in the exception when `actual` is equal to `notExpected`. The message is shown in test results.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `notExpected` is equal to `actual`.

```csharp
public static void AreNotEqual(
    string? notExpected,
    string? actual,
    bool ignoreCase,
    CultureInfo culture,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified strings are unequal and throws an exception if they are equal.

**Parameters:**

- `notExpected`: The first string to compare. This is the string the test expects not to match `actual`.
- `actual`: The second string to compare. This is the string produced by the code under test.
- `ignoreCase`: A Boolean indicating a case-sensitive or insensitive comparison. (true indicates a case-insensitive comparison.)
- `culture`: A CultureInfo object that supplies culture-specific comparison information. If culture is null, the current culture is used.
- `message`: The message to include in the exception when `actual` is equal to `notExpected`. The message is shown in test results.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `notExpected` is equal to `actual`.

### AreNotEquivalent

```csharp
public static void AreNotEquivalent<T>(
    Memory<T> notExpected,
    Memory<T> actual,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two memory regions are NOT structurally equivalent.

**Type parameters:**

- `T`: The element type of the memory regions.

**Parameters:**

- `notExpected`: The memory the test expects not to match `actual`.
- `actual`: The memory produced by the code under test.
- `message`: The message to include in the exception when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreNotEquivalent<T>(
    ReadOnlyMemory<T> notExpected,
    ReadOnlyMemory<T> actual,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two memory regions are NOT structurally equivalent.

**Type parameters:**

- `T`: The element type of the memory regions.

**Parameters:**

- `notExpected`: The memory the test expects not to match `actual`.
- `actual`: The memory produced by the code under test.
- `message`: The message to include in the exception when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreNotEquivalent<T>(
    ReadOnlySpan<T> notExpected,
    ReadOnlySpan<T> actual,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two spans are NOT structurally equivalent.

**Type parameters:**

- `T`: The element type of the spans.

**Parameters:**

- `notExpected`: The span the test expects not to match `actual`.
- `actual`: The span produced by the code under test.
- `message`: The message to include in the exception when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreNotEquivalent<T>(
    Span<T> notExpected,
    Span<T> actual,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two spans are NOT structurally equivalent.

**Type parameters:**

- `T`: The element type of the spans.

**Parameters:**

- `notExpected`: The span the test expects not to match `actual`.
- `actual`: The span produced by the code under test.
- `message`: The message to include in the exception when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreNotEquivalent<T>(
    T? notExpected,
    T? actual,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two object graphs are NOT structurally equivalent and throws an exception if they are.

**Type parameters:**

- `T`: The type of values to compare.

**Parameters:**

- `notExpected`: The first value to compare. This is the value the test expects not to match `actual`.
- `actual`: The second value to compare. This is the value produced by the code under test.
- `message`: The message to include in the exception when `actual` is equivalent to `notExpected`. The message is shown in test results.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `notExpected` and `actual` are structurally equivalent, or if the structural comparison cannot be completed.

#### Remarks

See `Assert.AreEquivalent(T0,T0,String,String,String)` and `Assert.AreEquivalent(T0,T0,Boolean,String,String,String)` for the full set of comparison rules.

```csharp
public static void AreNotEquivalent<T>(
    Memory<T> notExpected,
    Memory<T> actual,
    bool strict,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two memory regions are NOT structurally equivalent.

**Type parameters:**

- `T`: The element type of the memory regions.

**Parameters:**

- `notExpected`: The memory the test expects not to match `actual`.
- `actual`: The memory produced by the code under test.
- `strict`: When `true`, the comparison is performed in strict mode.
- `message`: The message to include in the exception when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreNotEquivalent<T>(
    ReadOnlyMemory<T> notExpected,
    ReadOnlyMemory<T> actual,
    bool strict,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two memory regions are NOT structurally equivalent.

**Type parameters:**

- `T`: The element type of the memory regions.

**Parameters:**

- `notExpected`: The memory the test expects not to match `actual`.
- `actual`: The memory produced by the code under test.
- `strict`: When `true`, the comparison is performed in strict mode.
- `message`: The message to include in the exception when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreNotEquivalent<T>(
    ReadOnlySpan<T> notExpected,
    ReadOnlySpan<T> actual,
    bool strict,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two spans are NOT structurally equivalent.

**Type parameters:**

- `T`: The element type of the spans.

**Parameters:**

- `notExpected`: The span the test expects not to match `actual`.
- `actual`: The span produced by the code under test.
- `strict`: When `true`, the comparison is performed in strict mode.
- `message`: The message to include in the exception when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreNotEquivalent<T>(
    Span<T> notExpected,
    Span<T> actual,
    bool strict,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two spans are NOT structurally equivalent.

**Type parameters:**

- `T`: The element type of the spans.

**Parameters:**

- `notExpected`: The span the test expects not to match `actual`.
- `actual`: The span produced by the code under test.
- `strict`: When `true`, the comparison is performed in strict mode.
- `message`: The message to include in the exception when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void AreNotEquivalent<T>(
    T? notExpected,
    T? actual,
    bool strict,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two object graphs are NOT structurally equivalent and throws an exception if they are.

**Type parameters:**

- `T`: The type of values to compare.

**Parameters:**

- `notExpected`: The first value to compare. This is the value the test expects not to match `actual`.
- `actual`: The second value to compare. This is the value produced by the code under test.
- `strict`: When `true`, the equivalence check used to decide whether the assertion fails is performed in strict mode (extra members or dictionary keys on `actual` are considered a difference, so the assertion succeeds in their presence).
- `message`: The message to include in the exception when `actual` is equivalent to `notExpected`. The message is shown in test results.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `notExpected` and `actual` are structurally equivalent, or if the structural comparison cannot be completed.

### AreNotSame

```csharp
public static void AreNotSame<T>(
    T? notExpected,
    T? actual,
    ref Assert.AssertAreNotSameInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified objects refer to different objects and throws an exception if the two inputs refer to the same object.

**Type parameters:**

- `T`: The type of values to compare.

**Parameters:**

- `notExpected`: The first object to compare. This is the value the test expects not to match `actual`.
- `actual`: The second object to compare. This is the value produced by the code under test.
- `message`: The message to include in the exception when `actual` is the same as `notExpected`. The message is shown in test results.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `notExpected` refers to the same object as `actual`.

```csharp
public static void AreNotSame<T>(
    T? notExpected,
    T? actual,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified objects refer to different objects and throws an exception if the two inputs refer to the same object.

**Type parameters:**

- `T`: The type of values to compare.

**Parameters:**

- `notExpected`: The first object to compare. This is the value the test expects not to match `actual`.
- `actual`: The second object to compare. This is the value produced by the code under test.
- `message`: The message to include in the exception when `actual` is the same as `notExpected`. The message is shown in test results.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `notExpected` refers to the same object as `actual`.

### AreNotSequenceEqual

```csharp
public static void AreNotSequenceEqual(
    IEnumerable? notExpected,
    IEnumerable? actual,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two sequences differ in the same order and throws an exception if they do not.

**Parameters:**

- `notExpected`: The sequence not expected to equal `actual`.
- `actual`: The sequence produced by the code under test.
- `message`: The message to include in the exception when the sequences are equal.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreNotSequenceEqual<T>(
    IEnumerable<T?>? notExpected,
    IEnumerable<T?>? actual,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two sequences differ in the same order and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `notExpected`: The sequence not expected to equal `actual`.
- `actual`: The sequence produced by the code under test.
- `message`: The message to include in the exception when the sequences are equal.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreNotSequenceEqual<T>(
    Memory<T> notExpected,
    Memory<T> actual,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two memory regions differ in the same order and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `notExpected`: The memory not expected to equal `actual`.
- `actual`: The memory produced by the code under test.
- `message`: The message to include in the exception when the sequences are equal.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreNotSequenceEqual<T>(
    ReadOnlyMemory<T> notExpected,
    ReadOnlyMemory<T> actual,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two memory regions differ in the same order and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `notExpected`: The memory not expected to equal `actual`.
- `actual`: The memory produced by the code under test.
- `message`: The message to include in the exception when the sequences are equal.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreNotSequenceEqual<T>(
    ReadOnlySpan<T> notExpected,
    ReadOnlySpan<T> actual,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two spans differ in the same order and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `notExpected`: The span not expected to equal `actual`.
- `actual`: The span produced by the code under test.
- `message`: The message to include in the exception when the sequences are equal.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreNotSequenceEqual<T>(
    Span<T> notExpected,
    Span<T> actual,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two spans differ in the same order and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `notExpected`: The span not expected to equal `actual`.
- `actual`: The span produced by the code under test.
- `message`: The message to include in the exception when the sequences are equal.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreNotSequenceEqual<T>(
    T?[]? notExpected,
    IEnumerable<T?>? actual,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether an array and a sequence differ in the same order.

**Type parameters:**

- `T`: The type of the array elements.

**Parameters:**

- `notExpected`: The array not expected to equal `actual`.
- `actual`: The sequence produced by the code under test.
- `message`: The message to include in the exception when the arrays are equal.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreNotSequenceEqual<T>(
    T?[]? notExpected,
    T?[]? actual,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two arrays differ in the same order.

**Type parameters:**

- `T`: The type of the array elements.

**Parameters:**

- `notExpected`: The array not expected to equal `actual`.
- `actual`: The array produced by the code under test.
- `message`: The message to include in the exception when the arrays are equal.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreNotSequenceEqual(
    IEnumerable? notExpected,
    IEnumerable? actual,
    IEqualityComparer? comparer,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two sequences differ in the same order using the specified comparer and throws an exception if they do not.

**Parameters:**

- `notExpected`: The sequence not expected to equal `actual`.
- `actual`: The sequence produced by the code under test.
- `comparer`: The equality comparer to use when comparing elements, or `null` to use the default comparer.
- `message`: The message to include in the exception when the sequences are equal.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreNotSequenceEqual(
    IEnumerable? notExpected,
    IEnumerable? actual,
    SequenceOrder order,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two sequences differ using the specified order semantics and throws an exception if they do not.

**Parameters:**

- `notExpected`: The sequence not expected to equal `actual`.
- `actual`: The sequence produced by the code under test.
- `order`: Specifies whether elements must appear in the same order or in any order.
- `message`: The message to include in the exception when the sequences are equal.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreNotSequenceEqual<T, TNotExpectedCollection, TActualCollection>(
    TNotExpectedCollection? notExpected,
    TActualCollection? actual,
    IEqualityComparer<T?>? comparer,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two collections differ in the same order using the specified equality comparer and throws an exception if they are equal.

**Type parameters:**

- `T`: The type of the collection elements.
- `TNotExpectedCollection`: The concrete type of the not-expected collection.
- `TActualCollection`: The concrete type of the actual collection.

**Parameters:**

- `notExpected`: The collection not expected to equal `actual`.
- `actual`: The collection produced by the code under test.
- `comparer`: The equality comparer to use when comparing elements, or `null` to use the default comparer.
- `message`: The message to include in the exception when the collections are equal.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreNotSequenceEqual<T>(
    IEnumerable<T?>? notExpected,
    IEnumerable<T?>? actual,
    IEqualityComparer<T?>? comparer,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two sequences differ in the same order using the specified comparer and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `notExpected`: The sequence not expected to equal `actual`.
- `actual`: The sequence produced by the code under test.
- `comparer`: The equality comparer to use when comparing elements, or `null` to use the default comparer.
- `message`: The message to include in the exception when the sequences are equal.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreNotSequenceEqual<T>(
    IEnumerable<T?>? notExpected,
    IEnumerable<T?>? actual,
    SequenceOrder order,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two sequences differ using the specified order semantics and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `notExpected`: The sequence not expected to equal `actual`.
- `actual`: The sequence produced by the code under test.
- `order`: Specifies whether elements must appear in the same order or in any order.
- `message`: The message to include in the exception when the sequences are equal.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreNotSequenceEqual<T>(
    Memory<T> notExpected,
    Memory<T> actual,
    IEqualityComparer<T?>? comparer,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two memory regions differ in the same order using the specified comparer and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `notExpected`: The memory not expected to equal `actual`.
- `actual`: The memory produced by the code under test.
- `comparer`: The equality comparer to use when comparing elements, or `null` to use the default comparer.
- `message`: The message to include in the exception when the sequences are equal.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreNotSequenceEqual<T>(
    Memory<T> notExpected,
    Memory<T> actual,
    SequenceOrder order,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two memory regions differ using the specified order semantics and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `notExpected`: The memory not expected to equal `actual`.
- `actual`: The memory produced by the code under test.
- `order`: Specifies whether elements must appear in the same order or in any order.
- `message`: The message to include in the exception when the sequences are equal.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreNotSequenceEqual<T>(
    ReadOnlyMemory<T> notExpected,
    ReadOnlyMemory<T> actual,
    IEqualityComparer<T?>? comparer,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two memory regions differ in the same order using the specified comparer and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `notExpected`: The memory not expected to equal `actual`.
- `actual`: The memory produced by the code under test.
- `comparer`: The equality comparer to use when comparing elements, or `null` to use the default comparer.
- `message`: The message to include in the exception when the sequences are equal.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreNotSequenceEqual<T>(
    ReadOnlyMemory<T> notExpected,
    ReadOnlyMemory<T> actual,
    SequenceOrder order,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two memory regions differ using the specified order semantics and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `notExpected`: The memory not expected to equal `actual`.
- `actual`: The memory produced by the code under test.
- `order`: Specifies whether elements must appear in the same order or in any order.
- `message`: The message to include in the exception when the sequences are equal.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreNotSequenceEqual<T>(
    ReadOnlySpan<T> notExpected,
    ReadOnlySpan<T> actual,
    IEqualityComparer<T?>? comparer,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two spans differ in the same order using the specified comparer and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `notExpected`: The span not expected to equal `actual`.
- `actual`: The span produced by the code under test.
- `comparer`: The equality comparer to use when comparing elements, or `null` to use the default comparer.
- `message`: The message to include in the exception when the sequences are equal.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreNotSequenceEqual<T>(
    ReadOnlySpan<T> notExpected,
    ReadOnlySpan<T> actual,
    SequenceOrder order,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two spans differ using the specified order semantics and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `notExpected`: The span not expected to equal `actual`.
- `actual`: The span produced by the code under test.
- `order`: Specifies whether elements must appear in the same order or in any order.
- `message`: The message to include in the exception when the sequences are equal.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreNotSequenceEqual<T>(
    Span<T> notExpected,
    Span<T> actual,
    IEqualityComparer<T?>? comparer,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two spans differ in the same order using the specified comparer and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `notExpected`: The span not expected to equal `actual`.
- `actual`: The span produced by the code under test.
- `comparer`: The equality comparer to use when comparing elements, or `null` to use the default comparer.
- `message`: The message to include in the exception when the sequences are equal.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreNotSequenceEqual<T>(
    Span<T> notExpected,
    Span<T> actual,
    SequenceOrder order,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two spans differ using the specified order semantics and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `notExpected`: The span not expected to equal `actual`.
- `actual`: The span produced by the code under test.
- `order`: Specifies whether elements must appear in the same order or in any order.
- `message`: The message to include in the exception when the sequences are equal.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreNotSequenceEqual<T>(
    T?[]? notExpected,
    IEnumerable<T?>? actual,
    SequenceOrder order,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether an array and a sequence differ using the specified order semantics.

**Type parameters:**

- `T`: The type of the array elements.

**Parameters:**

- `notExpected`: The array not expected to equal `actual`.
- `actual`: The sequence produced by the code under test.
- `order`: Specifies whether elements must appear in the same order or in any order.
- `message`: The message to include in the exception when the arrays are equal.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreNotSequenceEqual<T>(
    T?[]? notExpected,
    T?[]? actual,
    IEqualityComparer<T?>? comparer,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two arrays differ in the same order using the specified equality comparer.

**Type parameters:**

- `T`: The type of the array elements.

**Parameters:**

- `notExpected`: The array not expected to equal `actual`.
- `actual`: The array produced by the code under test.
- `comparer`: The equality comparer to use when comparing elements, or `null` to use the default comparer.
- `message`: The message to include in the exception when the arrays are equal.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreNotSequenceEqual<T>(
    T?[]? notExpected,
    T?[]? actual,
    SequenceOrder order,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two arrays differ using the specified order semantics.

**Type parameters:**

- `T`: The type of the array elements.

**Parameters:**

- `notExpected`: The array not expected to equal `actual`.
- `actual`: The array produced by the code under test.
- `order`: Specifies whether elements must appear in the same order or in any order.
- `message`: The message to include in the exception when the arrays are equal.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreNotSequenceEqual(
    IEnumerable? notExpected,
    IEnumerable? actual,
    IEqualityComparer? comparer,
    SequenceOrder order,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two sequences differ using the specified comparer and order semantics and throws an exception if they do not.

**Parameters:**

- `notExpected`: The sequence not expected to equal `actual`.
- `actual`: The sequence produced by the code under test.
- `comparer`: The equality comparer to use when comparing elements, or `null` to use the default comparer.
- `order`: Specifies whether elements must appear in the same order or in any order.
- `message`: The message to include in the exception when the sequences are equal.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreNotSequenceEqual<T, TNotExpectedCollection, TActualCollection>(
    TNotExpectedCollection? notExpected,
    TActualCollection? actual,
    IEqualityComparer<T?>? comparer,
    SequenceOrder order,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two collections differ using the specified equality comparer and order semantics and throws an exception if they are equal.

**Type parameters:**

- `T`: The type of the collection elements.
- `TNotExpectedCollection`: The concrete type of the not-expected collection.
- `TActualCollection`: The concrete type of the actual collection.

**Parameters:**

- `notExpected`: The collection not expected to equal `actual`.
- `actual`: The collection produced by the code under test.
- `comparer`: The equality comparer to use when comparing elements, or `null` to use the default comparer.
- `order`: Specifies whether elements must appear in the same order or in any order.
- `message`: The message to include in the exception when the collections are equal.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreNotSequenceEqual<T>(
    IEnumerable<T?>? notExpected,
    IEnumerable<T?>? actual,
    IEqualityComparer<T?>? comparer,
    SequenceOrder order,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two sequences differ using the specified comparer and order semantics and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `notExpected`: The sequence not expected to equal `actual`.
- `actual`: The sequence produced by the code under test.
- `comparer`: The equality comparer to use when comparing elements, or `null` to use the default comparer.
- `order`: Specifies whether elements must appear in the same order or in any order.
- `message`: The message to include in the exception when the sequences are equal.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreNotSequenceEqual<T>(
    Memory<T> notExpected,
    Memory<T> actual,
    IEqualityComparer<T?>? comparer,
    SequenceOrder order,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two memory regions differ using the specified comparer and order semantics and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `notExpected`: The memory not expected to equal `actual`.
- `actual`: The memory produced by the code under test.
- `comparer`: The equality comparer to use when comparing elements, or `null` to use the default comparer.
- `order`: Specifies whether elements must appear in the same order or in any order.
- `message`: The message to include in the exception when the sequences are equal.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreNotSequenceEqual<T>(
    ReadOnlyMemory<T> notExpected,
    ReadOnlyMemory<T> actual,
    IEqualityComparer<T?>? comparer,
    SequenceOrder order,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two memory regions differ using the specified comparer and order semantics and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `notExpected`: The memory not expected to equal `actual`.
- `actual`: The memory produced by the code under test.
- `comparer`: The equality comparer to use when comparing elements, or `null` to use the default comparer.
- `order`: Specifies whether elements must appear in the same order or in any order.
- `message`: The message to include in the exception when the sequences are equal.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreNotSequenceEqual<T>(
    ReadOnlySpan<T> notExpected,
    ReadOnlySpan<T> actual,
    IEqualityComparer<T?>? comparer,
    SequenceOrder order,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two spans differ using the specified comparer and order semantics and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `notExpected`: The span not expected to equal `actual`.
- `actual`: The span produced by the code under test.
- `comparer`: The equality comparer to use when comparing elements, or `null` to use the default comparer.
- `order`: Specifies whether elements must appear in the same order or in any order.
- `message`: The message to include in the exception when the sequences are equal.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreNotSequenceEqual<T>(
    Span<T> notExpected,
    Span<T> actual,
    IEqualityComparer<T?>? comparer,
    SequenceOrder order,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two spans differ using the specified comparer and order semantics and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `notExpected`: The span not expected to equal `actual`.
- `actual`: The span produced by the code under test.
- `comparer`: The equality comparer to use when comparing elements, or `null` to use the default comparer.
- `order`: Specifies whether elements must appear in the same order or in any order.
- `message`: The message to include in the exception when the sequences are equal.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreNotSequenceEqual<T>(
    T?[]? notExpected,
    T?[]? actual,
    IEqualityComparer<T?>? comparer,
    SequenceOrder order,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two arrays differ using the specified equality comparer and order semantics.

**Type parameters:**

- `T`: The type of the array elements.

**Parameters:**

- `notExpected`: The array not expected to equal `actual`.
- `actual`: The array produced by the code under test.
- `comparer`: The equality comparer to use when comparing elements, or `null` to use the default comparer.
- `order`: Specifies whether elements must appear in the same order or in any order.
- `message`: The message to include in the exception when the arrays are equal.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

### AreSame

```csharp
public static void AreSame<T>(
    T? expected,
    T? actual,
    ref Assert.AssertAreSameInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified objects both refer to the same object and throws an exception if the two inputs do not refer to the same object.

**Type parameters:**

- `T`: The type of values to compare.

**Parameters:**

- `expected`: The first object to compare. This is the value the test expects.
- `actual`: The second object to compare. This is the value produced by the code under test.
- `message`: The message to include in the exception when `actual` is not the same as `expected`. The message is shown in test results.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `expected` does not refer to the same object as `actual`.

```csharp
public static void AreSame<T>(
    T? expected,
    T? actual,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether the specified objects both refer to the same object and throws an exception if the two inputs do not refer to the same object.

**Type parameters:**

- `T`: The type of values to compare.

**Parameters:**

- `expected`: The first object to compare. This is the value the test expects.
- `actual`: The second object to compare. This is the value produced by the code under test.
- `message`: The message to include in the exception when `actual` is not the same as `expected`. The message is shown in test results.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `expected` does not refer to the same object as `actual`.

### AreSequenceEqual

```csharp
public static void AreSequenceEqual(
    IEnumerable? expected,
    IEnumerable? actual,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two sequences contain equal elements in the same order and throws an exception if they do not.

**Parameters:**

- `expected`: The sequence expected to be equal to `actual`.
- `actual`: The sequence produced by the code under test.
- `message`: The message to include in the exception when the sequences are not equal.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreSequenceEqual<T>(
    IEnumerable<T?>? expected,
    IEnumerable<T?>? actual,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two sequences contain equal elements in the same order and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `expected`: The sequence expected to be equal to `actual`.
- `actual`: The sequence produced by the code under test.
- `message`: The message to include in the exception when the sequences are not equal.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreSequenceEqual<T>(
    Memory<T> expected,
    Memory<T> actual,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two memory regions contain equal elements in the same order and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `expected`: The memory expected to be equal to `actual`.
- `actual`: The memory produced by the code under test.
- `message`: The message to include in the exception when the sequences are not equal.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreSequenceEqual<T>(
    ReadOnlyMemory<T> expected,
    ReadOnlyMemory<T> actual,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two memory regions contain equal elements in the same order and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `expected`: The memory expected to be equal to `actual`.
- `actual`: The memory produced by the code under test.
- `message`: The message to include in the exception when the sequences are not equal.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreSequenceEqual<T>(
    ReadOnlySpan<T> expected,
    ReadOnlySpan<T> actual,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two spans contain equal elements in the same order and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `expected`: The span expected to be equal to `actual`.
- `actual`: The span produced by the code under test.
- `message`: The message to include in the exception when the sequences are not equal.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreSequenceEqual<T>(
    Span<T> expected,
    Span<T> actual,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two spans contain equal elements in the same order and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `expected`: The span expected to be equal to `actual`.
- `actual`: The span produced by the code under test.
- `message`: The message to include in the exception when the sequences are not equal.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreSequenceEqual<T>(
    T?[]? expected,
    IEnumerable<T?>? actual,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether an array and a sequence contain equal elements in the same order.

**Type parameters:**

- `T`: The type of the array elements.

**Parameters:**

- `expected`: The array expected to be equal to `actual`.
- `actual`: The sequence produced by the code under test.
- `message`: The message to include in the exception when the arrays are not equal.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreSequenceEqual<T>(
    T?[]? expected,
    T?[]? actual,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two arrays contain equal elements in the same order.

**Type parameters:**

- `T`: The type of the array elements.

**Parameters:**

- `expected`: The array expected to be equal to `actual`.
- `actual`: The array produced by the code under test.
- `message`: The message to include in the exception when the arrays are not equal.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreSequenceEqual(
    IEnumerable? expected,
    IEnumerable? actual,
    IEqualityComparer? comparer,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two sequences contain equal elements in the same order using the specified comparer and throws an exception if they do not.

**Parameters:**

- `expected`: The sequence expected to be equal to `actual`.
- `actual`: The sequence produced by the code under test.
- `comparer`: The equality comparer to use when comparing elements, or `null` to use the default comparer.
- `message`: The message to include in the exception when the sequences are not equal.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreSequenceEqual(
    IEnumerable? expected,
    IEnumerable? actual,
    SequenceOrder order,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two sequences contain equal elements using the specified order semantics and throws an exception if they do not.

**Parameters:**

- `expected`: The sequence expected to be equal to `actual`.
- `actual`: The sequence produced by the code under test.
- `order`: Specifies whether elements must appear in the same order or in any order.
- `message`: The message to include in the exception when the sequences are not equal.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreSequenceEqual<T, TExpectedCollection, TActualCollection>(
    TExpectedCollection? expected,
    TActualCollection? actual,
    IEqualityComparer<T?>? comparer,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two collections contain equal elements in the same order using the specified equality comparer and throws an exception if they do not.

**Type parameters:**

- `T`: The type of the collection elements.
- `TExpectedCollection`: The concrete type of the expected collection.
- `TActualCollection`: The concrete type of the actual collection.

**Parameters:**

- `expected`: The collection expected to be equal to `actual`.
- `actual`: The collection produced by the code under test.
- `comparer`: The equality comparer to use when comparing elements, or `null` to use the default comparer.
- `message`: The message to include in the exception when the collections are not equal.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreSequenceEqual<T>(
    IEnumerable<T?>? expected,
    IEnumerable<T?>? actual,
    IEqualityComparer<T?>? comparer,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two sequences contain equal elements in the same order using the specified comparer and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `expected`: The sequence expected to be equal to `actual`.
- `actual`: The sequence produced by the code under test.
- `comparer`: The equality comparer to use when comparing elements, or `null` to use the default comparer.
- `message`: The message to include in the exception when the sequences are not equal.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreSequenceEqual<T>(
    IEnumerable<T?>? expected,
    IEnumerable<T?>? actual,
    SequenceOrder order,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two sequences contain equal elements using the specified order semantics and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `expected`: The sequence expected to be equal to `actual`.
- `actual`: The sequence produced by the code under test.
- `order`: Specifies whether elements must appear in the same order or in any order.
- `message`: The message to include in the exception when the sequences are not equal.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreSequenceEqual<T>(
    Memory<T> expected,
    Memory<T> actual,
    IEqualityComparer<T?>? comparer,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two memory regions contain equal elements in the same order using the specified comparer and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `expected`: The memory expected to be equal to `actual`.
- `actual`: The memory produced by the code under test.
- `comparer`: The equality comparer to use when comparing elements, or `null` to use the default comparer.
- `message`: The message to include in the exception when the sequences are not equal.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreSequenceEqual<T>(
    Memory<T> expected,
    Memory<T> actual,
    SequenceOrder order,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two memory regions contain equal elements using the specified order semantics and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `expected`: The memory expected to be equal to `actual`.
- `actual`: The memory produced by the code under test.
- `order`: Specifies whether elements must appear in the same order or in any order.
- `message`: The message to include in the exception when the sequences are not equal.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreSequenceEqual<T>(
    ReadOnlyMemory<T> expected,
    ReadOnlyMemory<T> actual,
    IEqualityComparer<T?>? comparer,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two memory regions contain equal elements in the same order using the specified comparer and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `expected`: The memory expected to be equal to `actual`.
- `actual`: The memory produced by the code under test.
- `comparer`: The equality comparer to use when comparing elements, or `null` to use the default comparer.
- `message`: The message to include in the exception when the sequences are not equal.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreSequenceEqual<T>(
    ReadOnlyMemory<T> expected,
    ReadOnlyMemory<T> actual,
    SequenceOrder order,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two memory regions contain equal elements using the specified order semantics and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `expected`: The memory expected to be equal to `actual`.
- `actual`: The memory produced by the code under test.
- `order`: Specifies whether elements must appear in the same order or in any order.
- `message`: The message to include in the exception when the sequences are not equal.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreSequenceEqual<T>(
    ReadOnlySpan<T> expected,
    ReadOnlySpan<T> actual,
    IEqualityComparer<T?>? comparer,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two spans contain equal elements in the same order using the specified comparer and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `expected`: The span expected to be equal to `actual`.
- `actual`: The span produced by the code under test.
- `comparer`: The equality comparer to use when comparing elements, or `null` to use the default comparer.
- `message`: The message to include in the exception when the sequences are not equal.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreSequenceEqual<T>(
    ReadOnlySpan<T> expected,
    ReadOnlySpan<T> actual,
    SequenceOrder order,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two spans contain equal elements using the specified order semantics and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `expected`: The span expected to be equal to `actual`.
- `actual`: The span produced by the code under test.
- `order`: Specifies whether elements must appear in the same order or in any order.
- `message`: The message to include in the exception when the sequences are not equal.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreSequenceEqual<T>(
    Span<T> expected,
    Span<T> actual,
    IEqualityComparer<T?>? comparer,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two spans contain equal elements in the same order using the specified comparer and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `expected`: The span expected to be equal to `actual`.
- `actual`: The span produced by the code under test.
- `comparer`: The equality comparer to use when comparing elements, or `null` to use the default comparer.
- `message`: The message to include in the exception when the sequences are not equal.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreSequenceEqual<T>(
    Span<T> expected,
    Span<T> actual,
    SequenceOrder order,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two spans contain equal elements using the specified order semantics and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `expected`: The span expected to be equal to `actual`.
- `actual`: The span produced by the code under test.
- `order`: Specifies whether elements must appear in the same order or in any order.
- `message`: The message to include in the exception when the sequences are not equal.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreSequenceEqual<T>(
    T?[]? expected,
    IEnumerable<T?>? actual,
    SequenceOrder order,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether an array and a sequence contain equal elements using the specified order semantics.

**Type parameters:**

- `T`: The type of the array elements.

**Parameters:**

- `expected`: The array expected to be equal to `actual`.
- `actual`: The sequence produced by the code under test.
- `order`: Specifies whether elements must appear in the same order or in any order.
- `message`: The message to include in the exception when the arrays are not equal.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreSequenceEqual<T>(
    T?[]? expected,
    T?[]? actual,
    IEqualityComparer<T?>? comparer,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two arrays contain equal elements in the same order using the specified equality comparer.

**Type parameters:**

- `T`: The type of the array elements.

**Parameters:**

- `expected`: The array expected to be equal to `actual`.
- `actual`: The array produced by the code under test.
- `comparer`: The equality comparer to use when comparing elements, or `null` to use the default comparer.
- `message`: The message to include in the exception when the arrays are not equal.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreSequenceEqual<T>(
    T?[]? expected,
    T?[]? actual,
    SequenceOrder order,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two arrays contain equal elements using the specified order semantics.

**Type parameters:**

- `T`: The type of the array elements.

**Parameters:**

- `expected`: The array expected to be equal to `actual`.
- `actual`: The array produced by the code under test.
- `order`: Specifies whether elements must appear in the same order or in any order.
- `message`: The message to include in the exception when the arrays are not equal.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreSequenceEqual(
    IEnumerable? expected,
    IEnumerable? actual,
    IEqualityComparer? comparer,
    SequenceOrder order,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two sequences contain equal elements using the specified comparer and order semantics and throws an exception if they do not.

**Parameters:**

- `expected`: The sequence expected to be equal to `actual`.
- `actual`: The sequence produced by the code under test.
- `comparer`: The equality comparer to use when comparing elements, or `null` to use the default comparer.
- `order`: Specifies whether elements must appear in the same order or in any order.
- `message`: The message to include in the exception when the sequences are not equal.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreSequenceEqual<T, TExpectedCollection, TActualCollection>(
    TExpectedCollection? expected,
    TActualCollection? actual,
    IEqualityComparer<T?>? comparer,
    SequenceOrder order,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two collections contain equal elements using the specified equality comparer and order semantics and throws an exception if they do not.

**Type parameters:**

- `T`: The type of the collection elements.
- `TExpectedCollection`: The concrete type of the expected collection.
- `TActualCollection`: The concrete type of the actual collection.

**Parameters:**

- `expected`: The collection expected to be equal to `actual`.
- `actual`: The collection produced by the code under test.
- `comparer`: The equality comparer to use when comparing elements, or `null` to use the default comparer.
- `order`: Specifies whether elements must appear in the same order or in any order.
- `message`: The message to include in the exception when the collections are not equal.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreSequenceEqual<T>(
    IEnumerable<T?>? expected,
    IEnumerable<T?>? actual,
    IEqualityComparer<T?>? comparer,
    SequenceOrder order,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two sequences contain equal elements using the specified comparer and order semantics and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `expected`: The sequence expected to be equal to `actual`.
- `actual`: The sequence produced by the code under test.
- `comparer`: The equality comparer to use when comparing elements, or `null` to use the default comparer.
- `order`: Specifies whether elements must appear in the same order or in any order.
- `message`: The message to include in the exception when the sequences are not equal.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreSequenceEqual<T>(
    Memory<T> expected,
    Memory<T> actual,
    IEqualityComparer<T?>? comparer,
    SequenceOrder order,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two memory regions contain equal elements using the specified comparer and order semantics and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `expected`: The memory expected to be equal to `actual`.
- `actual`: The memory produced by the code under test.
- `comparer`: The equality comparer to use when comparing elements, or `null` to use the default comparer.
- `order`: Specifies whether elements must appear in the same order or in any order.
- `message`: The message to include in the exception when the sequences are not equal.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreSequenceEqual<T>(
    ReadOnlyMemory<T> expected,
    ReadOnlyMemory<T> actual,
    IEqualityComparer<T?>? comparer,
    SequenceOrder order,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two memory regions contain equal elements using the specified comparer and order semantics and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `expected`: The memory expected to be equal to `actual`.
- `actual`: The memory produced by the code under test.
- `comparer`: The equality comparer to use when comparing elements, or `null` to use the default comparer.
- `order`: Specifies whether elements must appear in the same order or in any order.
- `message`: The message to include in the exception when the sequences are not equal.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreSequenceEqual<T>(
    ReadOnlySpan<T> expected,
    ReadOnlySpan<T> actual,
    IEqualityComparer<T?>? comparer,
    SequenceOrder order,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two spans contain equal elements using the specified comparer and order semantics and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `expected`: The span expected to be equal to `actual`.
- `actual`: The span produced by the code under test.
- `comparer`: The equality comparer to use when comparing elements, or `null` to use the default comparer.
- `order`: Specifies whether elements must appear in the same order or in any order.
- `message`: The message to include in the exception when the sequences are not equal.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreSequenceEqual<T>(
    Span<T> expected,
    Span<T> actual,
    IEqualityComparer<T?>? comparer,
    SequenceOrder order,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two spans contain equal elements using the specified comparer and order semantics and throws an exception if they do not.

**Type parameters:**

- `T`: The type of sequence elements.

**Parameters:**

- `expected`: The span expected to be equal to `actual`.
- `actual`: The span produced by the code under test.
- `comparer`: The equality comparer to use when comparing elements, or `null` to use the default comparer.
- `order`: Specifies whether elements must appear in the same order or in any order.
- `message`: The message to include in the exception when the sequences are not equal.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

```csharp
public static void AreSequenceEqual<T>(
    T?[]? expected,
    T?[]? actual,
    IEqualityComparer<T?>? comparer,
    SequenceOrder order,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("actual")] string actualExpression = "")
```

Tests whether two arrays contain equal elements using the specified equality comparer and order semantics.

**Type parameters:**

- `T`: The type of the array elements.

**Parameters:**

- `expected`: The array expected to be equal to `actual`.
- `actual`: The array produced by the code under test.
- `comparer`: The equality comparer to use when comparing elements, or `null` to use the default comparer.
- `order`: Specifies whether elements must appear in the same order or in any order.
- `message`: The message to include in the exception when the arrays are not equal.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `actualExpression`: The syntactic expression of actual as given by the compiler via caller argument expression.

### Contains

```csharp
public static void Contains(
    Func<object, bool> predicate,
    IEnumerable collection,
    string? message = "",
    [CallerArgumentExpression("predicate")] string predicateExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified collection contains the given element.

**Parameters:**

- `predicate`: A function to test each element for a condition.
- `collection`: The collection.
- `message`: The message to display when the assertion fails.
- `predicateExpression`: The syntactic expression of predicate as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void Contains(
    object? expected,
    IEnumerable collection,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified collection contains the given element.

**Parameters:**

- `expected`: The expected item.
- `collection`: The collection.
- `message`: The message to display when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void Contains(
    string substring,
    string value,
    string? message = "",
    [CallerArgumentExpression("substring")] string substringExpression = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified string contains the specified substring and throws an exception if the substring does not occur within the test string.

**Parameters:**

- `substring`: The string expected to occur within `value`.
- `value`: The string that is expected to contain `substring`.
- `message`: The message to include in the exception when `substring` is not in `value`. The message is shown in test results.
- `substringExpression`: The syntactic expression of substring as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: `value` is null, or `substring` is null, or `value` does not contain `substring`.

```csharp
public static void Contains<T, TCollection>(
    Func<T, bool> predicate,
    TCollection collection,
    string? message = "",
    [CallerArgumentExpression("predicate")] string predicateExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified collection contains an element that matches the given predicate.

**Type parameters:**

- `T`: The type of the collection items.
- `TCollection`: The concrete type of the collection.

**Parameters:**

- `predicate`: A function to test each element for a condition.
- `collection`: The collection.
- `message`: The message to display when the assertion fails.
- `predicateExpression`: The syntactic expression of predicate as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void Contains<T, TCollection>(
    T? expected,
    TCollection collection,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified collection contains the given element.

**Type parameters:**

- `T`: The type of the collection items.
- `TCollection`: The concrete type of the collection.

**Parameters:**

- `expected`: The expected item.
- `collection`: The collection.
- `message`: The message to display when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

#### Remarks

The collection may contain null elements even when `expected` is not null.

```csharp
public static void Contains<T>(
    Func<T, bool> predicate,
    IEnumerable<T?> collection,
    string? message = "",
    [CallerArgumentExpression("predicate")] string predicateExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified collection contains the given element.

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `predicate`: A function to test each element for a condition.
- `collection`: The collection.
- `message`: The message to display when the assertion fails.
- `predicateExpression`: The syntactic expression of predicate as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void Contains<T>(
    Func<T, bool> predicate,
    Memory<T> collection,
    string? message = "",
    [CallerArgumentExpression("predicate")] string predicateExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified memory contains an element matching the given predicate.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `predicate`: A function to test each element for a condition.
- `collection`: The memory.
- `message`: The message to display when the assertion fails.
- `predicateExpression`: The syntactic expression of predicate as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void Contains<T>(
    Func<T, bool> predicate,
    ReadOnlyMemory<T> collection,
    string? message = "",
    [CallerArgumentExpression("predicate")] string predicateExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified memory contains an element matching the given predicate.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `predicate`: A function to test each element for a condition.
- `collection`: The memory.
- `message`: The message to display when the assertion fails.
- `predicateExpression`: The syntactic expression of predicate as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void Contains<T>(
    Func<T, bool> predicate,
    ReadOnlySpan<T> collection,
    string? message = "",
    [CallerArgumentExpression("predicate")] string predicateExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified span contains an element matching the given predicate.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `predicate`: A function to test each element for a condition.
- `collection`: The span.
- `message`: The message to display when the assertion fails.
- `predicateExpression`: The syntactic expression of predicate as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void Contains<T>(
    Func<T, bool> predicate,
    Span<T> collection,
    string? message = "",
    [CallerArgumentExpression("predicate")] string predicateExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified span contains an element matching the given predicate.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `predicate`: A function to test each element for a condition.
- `collection`: The span.
- `message`: The message to display when the assertion fails.
- `predicateExpression`: The syntactic expression of predicate as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void Contains<T>(
    Func<T, bool> predicate,
    T?[] collection,
    string? message = "",
    [CallerArgumentExpression("predicate")] string predicateExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified array contains an element that matches the given predicate.

**Type parameters:**

- `T`: The type of the array items.

**Parameters:**

- `predicate`: A function to test each element for a condition.
- `collection`: The array.
- `message`: The message to display when the assertion fails.
- `predicateExpression`: The syntactic expression of predicate as given by the compiler via caller argument expression.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression.

```csharp
public static void Contains<T>(
    T? expected,
    IEnumerable<T?> collection,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified collection contains the given element.

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `expected`: The expected item.
- `collection`: The collection.
- `message`: The message to display when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void Contains<T>(
    T? expected,
    Memory<T> collection,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified memory contains the given element.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `expected`: The expected item.
- `collection`: The memory.
- `message`: The message to display when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void Contains<T>(
    T? expected,
    ReadOnlyMemory<T> collection,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified memory contains the given element.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `expected`: The expected item.
- `collection`: The memory.
- `message`: The message to display when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void Contains<T>(
    T? expected,
    ReadOnlySpan<T> collection,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified span contains the given element.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `expected`: The expected item.
- `collection`: The span.
- `message`: The message to display when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void Contains<T>(
    T? expected,
    Span<T> collection,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified span contains the given element.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `expected`: The expected item.
- `collection`: The span.
- `message`: The message to display when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void Contains<T>(
    T? expected,
    T?[] collection,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified array contains the given element.

**Type parameters:**

- `T`: The type of the array items.

**Parameters:**

- `expected`: The expected item.
- `collection`: The array.
- `message`: The message to display when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression.

```csharp
public static void Contains(
    object? expected,
    IEnumerable collection,
    IEqualityComparer comparer,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified collection contains the given element.

**Parameters:**

- `expected`: The expected item.
- `collection`: The collection.
- `comparer`: An equality comparer to compare values.
- `message`: The message to display when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void Contains(
    string substring,
    string value,
    StringComparison comparisonType,
    string? message = "",
    [CallerArgumentExpression("substring")] string substringExpression = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified string contains the specified substring and throws an exception if the substring does not occur within the test string.

**Parameters:**

- `substring`: The string expected to occur within `value`.
- `value`: The string that is expected to contain `substring`.
- `comparisonType`: The comparison method to compare strings `comparisonType`.
- `message`: The message to include in the exception when `substring` is not in `value`. The message is shown in test results.
- `substringExpression`: The syntactic expression of substring as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: `value` is null, or `substring` is null, or `value` does not contain `substring`.

```csharp
public static void Contains<T, TCollection>(
    T? expected,
    TCollection collection,
    IEqualityComparer<T?> comparer,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified collection contains the given element.

**Type parameters:**

- `T`: The type of the collection items.
- `TCollection`: The concrete type of the collection.

**Parameters:**

- `expected`: The expected item.
- `collection`: The collection.
- `comparer`: An equality comparer to compare values.
- `message`: The message to display when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

#### Remarks

The collection may contain null elements even when `expected` is not null.

```csharp
public static void Contains<T>(
    T? expected,
    IEnumerable<T?> collection,
    IEqualityComparer<T?> comparer,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified collection contains the given element.

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `expected`: The expected item.
- `collection`: The collection.
- `comparer`: An equality comparer to compare values.
- `message`: The message to display when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void Contains<T>(
    T? expected,
    Memory<T> collection,
    IEqualityComparer<T?> comparer,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified memory contains the given element.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `expected`: The expected item.
- `collection`: The memory.
- `comparer`: An equality comparer to compare values.
- `message`: The message to display when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void Contains<T>(
    T? expected,
    ReadOnlyMemory<T> collection,
    IEqualityComparer<T?> comparer,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified memory contains the given element.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `expected`: The expected item.
- `collection`: The memory.
- `comparer`: An equality comparer to compare values.
- `message`: The message to display when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void Contains<T>(
    T? expected,
    ReadOnlySpan<T> collection,
    IEqualityComparer<T?> comparer,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified span contains the given element.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `expected`: The expected item.
- `collection`: The span.
- `comparer`: An equality comparer to compare values.
- `message`: The message to display when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void Contains<T>(
    T? expected,
    Span<T> collection,
    IEqualityComparer<T?> comparer,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified span contains the given element.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `expected`: The expected item.
- `collection`: The span.
- `comparer`: An equality comparer to compare values.
- `message`: The message to display when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void Contains<T>(
    T? expected,
    T?[] collection,
    IEqualityComparer<T?> comparer,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified array contains the given element using the specified equality comparer.

**Type parameters:**

- `T`: The type of the array items.

**Parameters:**

- `expected`: The expected item.
- `collection`: The array.
- `comparer`: An equality comparer to compare values.
- `message`: The message to display when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression.

### ContainsAll

```csharp
public static void ContainsAll(
    [NotNull] IEnumerable expected,
    [NotNull] IEnumerable collection,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether `collection` contains every element of `expected` (with multiplicity) and throws an exception if any element in `expected` occurs more times than in `collection`.

**Parameters:**

- `expected`: The collection of items expected to all be present in `collection`.
- `collection`: The collection expected to contain every item of `expected`.
- `message`: The message to include in the exception when an element in `expected` is not found (with sufficient multiplicity) in `collection`. The message is shown in test results.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `expected` contains at least one element that occurs more times than in `collection`.

#### Remarks

Element multiplicity is significant: `[1]` does not contain all of `[1, 1]`.

```csharp
public static void ContainsAll<T>(
    Memory<T> expected,
    Memory<T> collection,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether `collection` contains every element of `expected` (with multiplicity).

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `expected`: The memory of items expected to all be present in `collection`.
- `collection`: The memory expected to contain every item of `expected`.
- `message`: The message to include in the exception when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void ContainsAll<T>(
    ReadOnlyMemory<T> expected,
    ReadOnlyMemory<T> collection,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether `collection` contains every element of `expected` (with multiplicity).

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `expected`: The memory of items expected to all be present in `collection`.
- `collection`: The memory expected to contain every item of `expected`.
- `message`: The message to include in the exception when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void ContainsAll<T>(
    ReadOnlySpan<T> expected,
    ReadOnlySpan<T> collection,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether `collection` contains every element of `expected` (with multiplicity).

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `expected`: The span of items expected to all be present in `collection`.
- `collection`: The span expected to contain every item of `expected`.
- `message`: The message to include in the exception when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void ContainsAll<T>(
    Span<T> expected,
    Span<T> collection,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether `collection` contains every element of `expected` (with multiplicity).

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `expected`: The span of items expected to all be present in `collection`.
- `collection`: The span expected to contain every item of `expected`.
- `message`: The message to include in the exception when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void ContainsAll<T>(
    [NotNull] IEnumerable<T?> expected,
    [NotNull] IEnumerable<T?> collection,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether `collection` contains every element of `expected` (with multiplicity) and throws an exception if any element in `expected` occurs more times than in `collection`.

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `expected`: The collection of items expected to all be present in `collection`.
- `collection`: The collection expected to contain every item of `expected`.
- `message`: The message to include in the exception when an element in `expected` is not found (with sufficient multiplicity) in `collection`. The message is shown in test results.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `expected` contains at least one element that occurs more times than in `collection`.

#### Remarks

Element multiplicity is significant: `[1]` does not contain all of `[1, 1]`.

```csharp
public static void ContainsAll<T>(
    [NotNull] T?[] expected,
    [NotNull] IEnumerable<T?> collection,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether `collection` contains every element of the specified `expected` array.

**Type parameters:**

- `T`: The type of the array items.

**Parameters:**

- `expected`: The array of items expected to all be present in `collection`.
- `collection`: The collection expected to contain every item of `expected`.
- `message`: The message to include in the exception when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression.

**Exceptions:**

- `AssertFailedException`: Thrown if an expected element does not occur enough times in `collection`.

#### Remarks

Element multiplicity is significant: `[1]` does not contain all of `[1, 1]`.

```csharp
public static void ContainsAll<T>(
    [NotNull] T?[] expected,
    [NotNull] T?[] collection,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified array contains every element of `expected`.

**Type parameters:**

- `T`: The type of the array items.

**Parameters:**

- `expected`: The array of items expected to all be present in `collection`.
- `collection`: The array expected to contain every item of `expected`.
- `message`: The message to include in the exception when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression.

**Exceptions:**

- `AssertFailedException`: Thrown if an expected element does not occur enough times in `collection`.

#### Remarks

Element multiplicity is significant: `[1]` does not contain all of `[1, 1]`.

```csharp
public static void ContainsAll(
    [NotNull] IEnumerable expected,
    [NotNull] IEnumerable collection,
    [NotNull] IEqualityComparer comparer,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether `collection` contains every element of `expected` (with multiplicity) and throws an exception if any element in `expected` occurs more times than in `collection`.

**Parameters:**

- `expected`: The collection of items expected to all be present in `collection`.
- `collection`: The collection expected to contain every item of `expected`.
- `comparer`: The equality comparer to use when comparing elements.
- `message`: The message to include in the exception when an element in `expected` is not found (with sufficient multiplicity) in `collection`. The message is shown in test results.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `expected` contains at least one element that occurs more times than in `collection`.

#### Remarks

Element multiplicity is significant: `[1]` does not contain all of `[1, 1]`.

```csharp
public static void ContainsAll<T, TExpectedCollection, TCollection>(
    [NotNull] TExpectedCollection expected,
    [NotNull] TCollection collection,
    [NotNull] IEqualityComparer<T?> comparer,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified collection contains every element of `expected` using the specified equality comparer.

**Type parameters:**

- `T`: The type of the collection items.
- `TExpectedCollection`: The concrete type of the expected collection.
- `TCollection`: The concrete type of the collection.

**Parameters:**

- `expected`: The collection of items expected to all be present in `collection`.
- `collection`: The collection expected to contain every item of `expected`.
- `comparer`: The equality comparer to use when comparing elements.
- `message`: The message to include in the exception when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression.

**Exceptions:**

- `AssertFailedException`: Thrown if `expected` contains an element that does not occur enough times in `collection`.

#### Remarks

Element multiplicity is significant: `[1]` does not contain all of `[1, 1]`.

```csharp
public static void ContainsAll<T>(
    Memory<T> expected,
    Memory<T> collection,
    [NotNull] IEqualityComparer<T?> comparer,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether `collection` contains every element of `expected` (with multiplicity).

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `expected`: The memory of items expected to all be present in `collection`.
- `collection`: The memory expected to contain every item of `expected`.
- `comparer`: The equality comparer to use when comparing elements.
- `message`: The message to include in the exception when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void ContainsAll<T>(
    ReadOnlyMemory<T> expected,
    ReadOnlyMemory<T> collection,
    [NotNull] IEqualityComparer<T?> comparer,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether `collection` contains every element of `expected` (with multiplicity).

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `expected`: The memory of items expected to all be present in `collection`.
- `collection`: The memory expected to contain every item of `expected`.
- `comparer`: The equality comparer to use when comparing elements.
- `message`: The message to include in the exception when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void ContainsAll<T>(
    ReadOnlySpan<T> expected,
    ReadOnlySpan<T> collection,
    [NotNull] IEqualityComparer<T?> comparer,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether `collection` contains every element of `expected` (with multiplicity).

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `expected`: The span of items expected to all be present in `collection`.
- `collection`: The span expected to contain every item of `expected`.
- `comparer`: The equality comparer to use when comparing elements.
- `message`: The message to include in the exception when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void ContainsAll<T>(
    Span<T> expected,
    Span<T> collection,
    [NotNull] IEqualityComparer<T?> comparer,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether `collection` contains every element of `expected` (with multiplicity).

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `expected`: The span of items expected to all be present in `collection`.
- `collection`: The span expected to contain every item of `expected`.
- `comparer`: The equality comparer to use when comparing elements.
- `message`: The message to include in the exception when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void ContainsAll<T>(
    [NotNull] IEnumerable<T?> expected,
    [NotNull] IEnumerable<T?> collection,
    [NotNull] IEqualityComparer<T?> comparer,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether `collection` contains every element of `expected` (with multiplicity) and throws an exception if any element in `expected` occurs more times than in `collection`.

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `expected`: The collection of items expected to all be present in `collection`.
- `collection`: The collection expected to contain every item of `expected`.
- `comparer`: The equality comparer to use when comparing elements.
- `message`: The message to include in the exception when an element in `expected` is not found (with sufficient multiplicity) in `collection`. The message is shown in test results.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `expected` contains at least one element that occurs more times than in `collection`.

#### Remarks

Element multiplicity is significant: `[1]` does not contain all of `[1, 1]`.

```csharp
public static void ContainsAll<T>(
    [NotNull] T?[] expected,
    [NotNull] T?[] collection,
    [NotNull] IEqualityComparer<T?> comparer,
    string? message = "",
    [CallerArgumentExpression("expected")] string expectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified array contains every element of `expected` using the specified equality comparer.

**Type parameters:**

- `T`: The type of the array items.

**Parameters:**

- `expected`: The array of items expected to all be present in `collection`.
- `collection`: The array expected to contain every item of `expected`.
- `comparer`: The equality comparer to use when comparing elements.
- `message`: The message to include in the exception when the assertion fails.
- `expectedExpression`: The syntactic expression of expected as given by the compiler via caller argument expression.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression.

**Exceptions:**

- `AssertFailedException`: Thrown if an expected element does not occur enough times in `collection`.

#### Remarks

Element multiplicity is significant: `[1]` does not contain all of `[1, 1]`.

### ContainsSingle

```csharp
public static T? ContainsSingle<T>(
    IEnumerable<T?> collection,
    ref Assert.AssertSingleInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified collection contains exactly one element.

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `collection`: The collection.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The item.

```csharp
public static T? ContainsSingle<T>(
    IEnumerable<T?> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified collection contains exactly one element.

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `collection`: The collection.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The item.

```csharp
public static T? ContainsSingle<T>(
    Memory<T> collection,
    ref Assert.AssertSingleInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified memory contains exactly one element.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `collection`: The memory.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The item.

```csharp
public static T? ContainsSingle<T>(
    Memory<T> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified memory contains exactly one element.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `collection`: The memory.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The item.

```csharp
public static T? ContainsSingle<T>(
    ReadOnlyMemory<T> collection,
    ref Assert.AssertSingleInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified memory contains exactly one element.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `collection`: The memory.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The item.

```csharp
public static T? ContainsSingle<T>(
    ReadOnlyMemory<T> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified memory contains exactly one element.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `collection`: The memory.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The item.

```csharp
public static T? ContainsSingle<T>(
    ReadOnlySpan<T> collection,
    ref Assert.AssertSingleInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified span contains exactly one element.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `collection`: The span.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The item.

```csharp
public static T? ContainsSingle<T>(
    ReadOnlySpan<T> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified span contains exactly one element.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `collection`: The span.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The item.

```csharp
public static T? ContainsSingle<T>(
    Span<T> collection,
    ref Assert.AssertSingleInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified span contains exactly one element.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `collection`: The span.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The item.

```csharp
public static T? ContainsSingle<T>(
    Span<T> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified span contains exactly one element.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `collection`: The span.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The item.

```csharp
public static T? ContainsSingle<T>(
    T?[] collection,
    ref Assert.AssertSingleInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified array contains exactly one element.

**Type parameters:**

- `T`: The type of the array items.

**Parameters:**

- `collection`: The array.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression.

**Returns:** The item.

```csharp
public static T? ContainsSingle<T>(
    T?[] collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified array contains exactly one element.

**Type parameters:**

- `T`: The type of the array items.

**Parameters:**

- `collection`: The array.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression.

**Returns:** The item.

```csharp
public static object? ContainsSingle(
    IEnumerable collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified collection contains exactly one element.

**Parameters:**

- `collection`: The collection.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The item.

```csharp
public static T? ContainsSingle<T, TCollection>(
    Func<T, bool> predicate,
    TCollection collection,
    string? message = "",
    [CallerArgumentExpression("predicate")] string predicateExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified collection contains exactly one element that matches the given predicate.

**Type parameters:**

- `T`: The type of the collection items.
- `TCollection`: The concrete type of the collection.

**Parameters:**

- `predicate`: A function to test each element for a condition.
- `collection`: The collection.
- `message`: The message to display when the assertion fails.
- `predicateExpression`: The syntactic expression of predicate as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The item that matches the predicate.

```csharp
public static T? ContainsSingle<T>(
    Func<T, bool> predicate,
    IEnumerable<T?> collection,
    string? message = "",
    [CallerArgumentExpression("predicate")] string predicateExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified collection contains exactly one element that matches the given predicate.

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `predicate`: A function to test each element for a condition.
- `collection`: The collection.
- `message`: The message to display when the assertion fails.
- `predicateExpression`: The syntactic expression of predicate as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The item that matches the predicate.

```csharp
public static T? ContainsSingle<T>(
    Func<T, bool> predicate,
    Memory<T> collection,
    string? message = "",
    [CallerArgumentExpression("predicate")] string predicateExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified memory contains exactly one element that matches the given predicate.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `predicate`: A function to test each element for a condition.
- `collection`: The memory.
- `message`: The message to display when the assertion fails.
- `predicateExpression`: The syntactic expression of predicate as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The item that matches the predicate.

```csharp
public static T? ContainsSingle<T>(
    Func<T, bool> predicate,
    ReadOnlyMemory<T> collection,
    string? message = "",
    [CallerArgumentExpression("predicate")] string predicateExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified memory contains exactly one element that matches the given predicate.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `predicate`: A function to test each element for a condition.
- `collection`: The memory.
- `message`: The message to display when the assertion fails.
- `predicateExpression`: The syntactic expression of predicate as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The item that matches the predicate.

```csharp
public static T? ContainsSingle<T>(
    Func<T, bool> predicate,
    ReadOnlySpan<T> collection,
    string? message = "",
    [CallerArgumentExpression("predicate")] string predicateExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified span contains exactly one element that matches the given predicate.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `predicate`: A function to test each element for a condition.
- `collection`: The span.
- `message`: The message to display when the assertion fails.
- `predicateExpression`: The syntactic expression of predicate as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The item that matches the predicate.

```csharp
public static T? ContainsSingle<T>(
    Func<T, bool> predicate,
    Span<T> collection,
    string? message = "",
    [CallerArgumentExpression("predicate")] string predicateExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified span contains exactly one element that matches the given predicate.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `predicate`: A function to test each element for a condition.
- `collection`: The span.
- `message`: The message to display when the assertion fails.
- `predicateExpression`: The syntactic expression of predicate as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The item that matches the predicate.

```csharp
public static T? ContainsSingle<T>(
    Func<T, bool> predicate,
    T?[] collection,
    string? message = "",
    [CallerArgumentExpression("predicate")] string predicateExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified array contains exactly one element that matches the given predicate.

**Type parameters:**

- `T`: The type of the array items.

**Parameters:**

- `predicate`: A function to test each element for a condition.
- `collection`: The array.
- `message`: The message to display when the assertion fails.
- `predicateExpression`: The syntactic expression of predicate as given by the compiler via caller argument expression.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression.

**Returns:** The item that matches the predicate.

```csharp
public static object? ContainsSingle(
    Func<object, bool> predicate,
    IEnumerable collection,
    string? message = "",
    [CallerArgumentExpression("predicate")] string predicateExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified collection contains exactly one element that matches the given predicate.

**Parameters:**

- `predicate`: A function to test each element for a condition.
- `collection`: The collection.
- `message`: The message to display when the assertion fails.
- `predicateExpression`: The syntactic expression of predicate as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The item that matches the predicate.

### DoesNotContain

```csharp
public static void DoesNotContain(
    Func<object, bool> predicate,
    IEnumerable collection,
    string? message = "",
    [CallerArgumentExpression("predicate")] string predicateExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified collection does not contain the specified item.

**Parameters:**

- `predicate`: A function to test each element for a condition.
- `collection`: The collection.
- `message`: The message to display when the assertion fails.
- `predicateExpression`: The syntactic expression of predicate as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void DoesNotContain(
    object? notExpected,
    IEnumerable collection,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified collection does not contain the specified item.

**Parameters:**

- `notExpected`: The unexpected item.
- `collection`: The collection.
- `message`: The message to display when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void DoesNotContain(
    string substring,
    string value,
    string? message = "",
    [CallerArgumentExpression("substring")] string substringExpression = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified string does not contain the specified substring and throws an exception if the substring occurs within the test string.

**Parameters:**

- `substring`: The string expected to not occur within `value`.
- `value`: The string that is expected to not contain `substring`.
- `message`: The message to include in the exception when `substring` is in `value`. The message is shown in test results.
- `substringExpression`: The syntactic expression of substring as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: `value` is null, or `substring` is null, or `value` contains `substring`.

```csharp
public static void DoesNotContain<T, TCollection>(
    Func<T, bool> predicate,
    TCollection collection,
    string? message = "",
    [CallerArgumentExpression("predicate")] string predicateExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified collection contains no element that matches the given predicate.

**Type parameters:**

- `T`: The type of the collection items.
- `TCollection`: The concrete type of the collection.

**Parameters:**

- `predicate`: A function to test each element for a condition.
- `collection`: The collection.
- `message`: The message to display when the assertion fails.
- `predicateExpression`: The syntactic expression of predicate as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void DoesNotContain<T, TCollection>(
    T? notExpected,
    TCollection collection,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified collection does not contain the specified item.

**Type parameters:**

- `T`: The type of the collection items.
- `TCollection`: The concrete type of the collection.

**Parameters:**

- `notExpected`: The unexpected item.
- `collection`: The collection.
- `message`: The message to display when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

#### Remarks

The collection may contain null elements even when `notExpected` is not null.

```csharp
public static void DoesNotContain<T>(
    Func<T, bool> predicate,
    IEnumerable<T?> collection,
    string? message = "",
    [CallerArgumentExpression("predicate")] string predicateExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified collection does not contain the specified item.

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `predicate`: A function to test each element for a condition.
- `collection`: The collection.
- `message`: The message to display when the assertion fails.
- `predicateExpression`: The syntactic expression of predicate as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void DoesNotContain<T>(
    Func<T, bool> predicate,
    Memory<T> collection,
    string? message = "",
    [CallerArgumentExpression("predicate")] string predicateExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified memory does not contain an element matching the given predicate.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `predicate`: A function to test each element for a condition.
- `collection`: The memory.
- `message`: The message to display when the assertion fails.
- `predicateExpression`: The syntactic expression of predicate as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void DoesNotContain<T>(
    Func<T, bool> predicate,
    ReadOnlyMemory<T> collection,
    string? message = "",
    [CallerArgumentExpression("predicate")] string predicateExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified memory does not contain an element matching the given predicate.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `predicate`: A function to test each element for a condition.
- `collection`: The memory.
- `message`: The message to display when the assertion fails.
- `predicateExpression`: The syntactic expression of predicate as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void DoesNotContain<T>(
    Func<T, bool> predicate,
    ReadOnlySpan<T> collection,
    string? message = "",
    [CallerArgumentExpression("predicate")] string predicateExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified span does not contain an element matching the given predicate.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `predicate`: A function to test each element for a condition.
- `collection`: The span.
- `message`: The message to display when the assertion fails.
- `predicateExpression`: The syntactic expression of predicate as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void DoesNotContain<T>(
    Func<T, bool> predicate,
    Span<T> collection,
    string? message = "",
    [CallerArgumentExpression("predicate")] string predicateExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified span does not contain an element matching the given predicate.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `predicate`: A function to test each element for a condition.
- `collection`: The span.
- `message`: The message to display when the assertion fails.
- `predicateExpression`: The syntactic expression of predicate as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void DoesNotContain<T>(
    Func<T, bool> predicate,
    T?[] collection,
    string? message = "",
    [CallerArgumentExpression("predicate")] string predicateExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified array contains no element that matches the given predicate.

**Type parameters:**

- `T`: The type of the array items.

**Parameters:**

- `predicate`: A function to test each element for a condition.
- `collection`: The array.
- `message`: The message to display when the assertion fails.
- `predicateExpression`: The syntactic expression of predicate as given by the compiler via caller argument expression.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression.

```csharp
public static void DoesNotContain<T>(
    T? notExpected,
    IEnumerable<T?> collection,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified collection does not contain the specified item.

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `notExpected`: The unexpected item.
- `collection`: The collection.
- `message`: The message to display when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void DoesNotContain<T>(
    T? notExpected,
    Memory<T> collection,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified memory does not contain the specified item.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `notExpected`: The unexpected item.
- `collection`: The memory.
- `message`: The message to display when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void DoesNotContain<T>(
    T? notExpected,
    ReadOnlyMemory<T> collection,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified memory does not contain the specified item.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `notExpected`: The unexpected item.
- `collection`: The memory.
- `message`: The message to display when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void DoesNotContain<T>(
    T? notExpected,
    ReadOnlySpan<T> collection,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified span does not contain the specified item.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `notExpected`: The unexpected item.
- `collection`: The span.
- `message`: The message to display when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void DoesNotContain<T>(
    T? notExpected,
    Span<T> collection,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified span does not contain the specified item.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `notExpected`: The unexpected item.
- `collection`: The span.
- `message`: The message to display when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void DoesNotContain<T>(
    T? notExpected,
    T?[] collection,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified array does not contain the specified item.

**Type parameters:**

- `T`: The type of the array items.

**Parameters:**

- `notExpected`: The unexpected item.
- `collection`: The array.
- `message`: The message to display when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression.

```csharp
public static void DoesNotContain(
    object? notExpected,
    IEnumerable collection,
    IEqualityComparer comparer,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified collection does not contain the specified item.

**Parameters:**

- `notExpected`: The unexpected item.
- `collection`: The collection.
- `comparer`: An equality comparer to compare values.
- `message`: The message to display when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void DoesNotContain(
    string substring,
    string value,
    StringComparison comparisonType,
    string? message = "",
    [CallerArgumentExpression("substring")] string substringExpression = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified string does not contain the specified substring and throws an exception if the substring occurs within the test string.

**Parameters:**

- `substring`: The string expected to not occur within `value`.
- `value`: The string that is expected to not contain `substring`.
- `comparisonType`: The comparison method to compare strings `comparisonType`.
- `message`: The message to include in the exception when `substring` is in `value`. The message is shown in test results.
- `substringExpression`: The syntactic expression of substring as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: `value` is null, or `substring` is null, or `value` contains `substring`.

```csharp
public static void DoesNotContain<T, TCollection>(
    T? notExpected,
    TCollection collection,
    IEqualityComparer<T?> comparer,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified collection does not contain the specified item.

**Type parameters:**

- `T`: The type of the collection items.
- `TCollection`: The concrete type of the collection.

**Parameters:**

- `notExpected`: The unexpected item.
- `collection`: The collection.
- `comparer`: An equality comparer to compare values.
- `message`: The message to display when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

#### Remarks

The collection may contain null elements even when `notExpected` is not null.

```csharp
public static void DoesNotContain<T>(
    T? notExpected,
    IEnumerable<T?> collection,
    IEqualityComparer<T?> comparer,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified collection does not contain the specified item.

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `notExpected`: The unexpected item.
- `collection`: The collection.
- `comparer`: An equality comparer to compare values.
- `message`: The message to display when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void DoesNotContain<T>(
    T? notExpected,
    Memory<T> collection,
    IEqualityComparer<T?> comparer,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified memory does not contain the specified item.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `notExpected`: The unexpected item.
- `collection`: The memory.
- `comparer`: An equality comparer to compare values.
- `message`: The message to display when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void DoesNotContain<T>(
    T? notExpected,
    ReadOnlyMemory<T> collection,
    IEqualityComparer<T?> comparer,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified memory does not contain the specified item.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `notExpected`: The unexpected item.
- `collection`: The memory.
- `comparer`: An equality comparer to compare values.
- `message`: The message to display when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void DoesNotContain<T>(
    T? notExpected,
    ReadOnlySpan<T> collection,
    IEqualityComparer<T?> comparer,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified span does not contain the specified item.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `notExpected`: The unexpected item.
- `collection`: The span.
- `comparer`: An equality comparer to compare values.
- `message`: The message to display when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void DoesNotContain<T>(
    T? notExpected,
    Span<T> collection,
    IEqualityComparer<T?> comparer,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified span does not contain the specified item.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `notExpected`: The unexpected item.
- `collection`: The span.
- `comparer`: An equality comparer to compare values.
- `message`: The message to display when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void DoesNotContain<T>(
    T? notExpected,
    T?[] collection,
    IEqualityComparer<T?> comparer,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified array does not contain the specified item using the specified equality comparer.

**Type parameters:**

- `T`: The type of the array items.

**Parameters:**

- `notExpected`: The unexpected item.
- `collection`: The array.
- `comparer`: An equality comparer to compare values.
- `message`: The message to display when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression.

### DoesNotContainAll

```csharp
public static void DoesNotContainAll(
    [NotNull] IEnumerable notExpected,
    [NotNull] IEnumerable collection,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether `collection` does not contain every element of `notExpected` (with multiplicity) and throws an exception if every element in `notExpected` occurs at least as many times in `collection`.

**Parameters:**

- `notExpected`: The collection of items the test expects not to all be present in `collection`.
- `collection`: The collection expected not to contain every item of `notExpected`.
- `message`: The message to include in the exception when every element in `notExpected` is also found (with sufficient multiplicity) in `collection`. The message is shown in test results.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if every element of `notExpected` occurs at least as many times in `collection`.

#### Remarks

Element multiplicity is significant: `[1]` is considered not to contain all of `[1, 1]` (so this assertion would pass for those inputs).

```csharp
public static void DoesNotContainAll<T>(
    Memory<T> notExpected,
    Memory<T> collection,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether `collection` does not contain every element of `notExpected` (with multiplicity).

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `notExpected`: The memory of items the test expects not to all be present in `collection`.
- `collection`: The memory expected not to contain every item of `notExpected`.
- `message`: The message to include in the exception when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void DoesNotContainAll<T>(
    ReadOnlyMemory<T> notExpected,
    ReadOnlyMemory<T> collection,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether `collection` does not contain every element of `notExpected` (with multiplicity).

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `notExpected`: The memory of items the test expects not to all be present in `collection`.
- `collection`: The memory expected not to contain every item of `notExpected`.
- `message`: The message to include in the exception when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void DoesNotContainAll<T>(
    ReadOnlySpan<T> notExpected,
    ReadOnlySpan<T> collection,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether `collection` does not contain every element of `notExpected` (with multiplicity).

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `notExpected`: The span of items the test expects not to all be present in `collection`.
- `collection`: The span expected not to contain every item of `notExpected`.
- `message`: The message to include in the exception when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void DoesNotContainAll<T>(
    Span<T> notExpected,
    Span<T> collection,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether `collection` does not contain every element of `notExpected` (with multiplicity).

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `notExpected`: The span of items the test expects not to all be present in `collection`.
- `collection`: The span expected not to contain every item of `notExpected`.
- `message`: The message to include in the exception when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void DoesNotContainAll<T>(
    [NotNull] IEnumerable<T?> notExpected,
    [NotNull] IEnumerable<T?> collection,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether `collection` does not contain every element of `notExpected` (with multiplicity) and throws an exception if every element in `notExpected` occurs at least as many times in `collection`.

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `notExpected`: The collection of items the test expects not to all be present in `collection`.
- `collection`: The collection expected not to contain every item of `notExpected`.
- `message`: The message to include in the exception when every element in `notExpected` is also found (with sufficient multiplicity) in `collection`. The message is shown in test results.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if every element of `notExpected` occurs at least as many times in `collection`.

#### Remarks

Element multiplicity is significant: `[1]` is considered not to contain all of `[1, 1]` (so this assertion would pass for those inputs).

```csharp
public static void DoesNotContainAll<T>(
    [NotNull] T?[] notExpected,
    [NotNull] IEnumerable<T?> collection,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether `collection` does not contain every element of the specified `notExpected` array.

**Type parameters:**

- `T`: The type of the array items.

**Parameters:**

- `notExpected`: The array of items that must not all be present in `collection`.
- `collection`: The collection that must not contain every item of `notExpected`.
- `message`: The message to include in the exception when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression.

**Exceptions:**

- `AssertFailedException`: Thrown if every unexpected element occurs enough times in `collection`.

#### Remarks

Element multiplicity is significant: `[1]` does not contain all of `[1, 1]`.

```csharp
public static void DoesNotContainAll<T>(
    [NotNull] T?[] notExpected,
    [NotNull] T?[] collection,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified array does not contain every element of `notExpected`.

**Type parameters:**

- `T`: The type of the array items.

**Parameters:**

- `notExpected`: The array of items that must not all be present in `collection`.
- `collection`: The array that must not contain every item of `notExpected`.
- `message`: The message to include in the exception when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression.

**Exceptions:**

- `AssertFailedException`: Thrown if every unexpected element occurs enough times in `collection`.

#### Remarks

Element multiplicity is significant: `[1]` does not contain all of `[1, 1]`.

```csharp
public static void DoesNotContainAll(
    [NotNull] IEnumerable notExpected,
    [NotNull] IEnumerable collection,
    [NotNull] IEqualityComparer comparer,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether `collection` does not contain every element of `notExpected` (with multiplicity) and throws an exception if every element in `notExpected` occurs at least as many times in `collection`.

**Parameters:**

- `notExpected`: The collection of items the test expects not to all be present in `collection`.
- `collection`: The collection expected not to contain every item of `notExpected`.
- `comparer`: The equality comparer to use when comparing elements.
- `message`: The message to include in the exception when every element in `notExpected` is also found (with sufficient multiplicity) in `collection`. The message is shown in test results.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if every element of `notExpected` occurs at least as many times in `collection`.

#### Remarks

Element multiplicity is significant: `[1]` is considered not to contain all of `[1, 1]` (so this assertion would pass for those inputs).

```csharp
public static void DoesNotContainAll<T, TNotExpectedCollection, TCollection>(
    [NotNull] TNotExpectedCollection notExpected,
    [NotNull] TCollection collection,
    [NotNull] IEqualityComparer<T?> comparer,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified collection does not contain every element of `notExpected` using the specified equality comparer.

**Type parameters:**

- `T`: The type of the collection items.
- `TNotExpectedCollection`: The concrete type of the not-expected collection.
- `TCollection`: The concrete type of the collection.

**Parameters:**

- `notExpected`: The collection of items that must not all be present in `collection`.
- `collection`: The collection that must not contain every item of `notExpected`.
- `comparer`: The equality comparer to use when comparing elements.
- `message`: The message to include in the exception when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression.

**Exceptions:**

- `AssertFailedException`: Thrown if every element in `notExpected` occurs enough times in `collection`.

#### Remarks

Element multiplicity is significant: `[1]` does not contain all of `[1, 1]`.

```csharp
public static void DoesNotContainAll<T>(
    Memory<T> notExpected,
    Memory<T> collection,
    [NotNull] IEqualityComparer<T?> comparer,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether `collection` does not contain every element of `notExpected` (with multiplicity).

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `notExpected`: The memory of items the test expects not to all be present in `collection`.
- `collection`: The memory expected not to contain every item of `notExpected`.
- `comparer`: The equality comparer to use when comparing elements.
- `message`: The message to include in the exception when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void DoesNotContainAll<T>(
    ReadOnlyMemory<T> notExpected,
    ReadOnlyMemory<T> collection,
    [NotNull] IEqualityComparer<T?> comparer,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether `collection` does not contain every element of `notExpected` (with multiplicity).

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `notExpected`: The memory of items the test expects not to all be present in `collection`.
- `collection`: The memory expected not to contain every item of `notExpected`.
- `comparer`: The equality comparer to use when comparing elements.
- `message`: The message to include in the exception when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void DoesNotContainAll<T>(
    ReadOnlySpan<T> notExpected,
    ReadOnlySpan<T> collection,
    [NotNull] IEqualityComparer<T?> comparer,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether `collection` does not contain every element of `notExpected` (with multiplicity).

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `notExpected`: The span of items the test expects not to all be present in `collection`.
- `collection`: The span expected not to contain every item of `notExpected`.
- `comparer`: The equality comparer to use when comparing elements.
- `message`: The message to include in the exception when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void DoesNotContainAll<T>(
    Span<T> notExpected,
    Span<T> collection,
    [NotNull] IEqualityComparer<T?> comparer,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether `collection` does not contain every element of `notExpected` (with multiplicity).

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `notExpected`: The span of items the test expects not to all be present in `collection`.
- `collection`: The span expected not to contain every item of `notExpected`.
- `comparer`: The equality comparer to use when comparing elements.
- `message`: The message to include in the exception when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void DoesNotContainAll<T>(
    [NotNull] IEnumerable<T?> notExpected,
    [NotNull] IEnumerable<T?> collection,
    [NotNull] IEqualityComparer<T?> comparer,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether `collection` does not contain every element of `notExpected` (with multiplicity) and throws an exception if every element in `notExpected` occurs at least as many times in `collection`.

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `notExpected`: The collection of items the test expects not to all be present in `collection`.
- `collection`: The collection expected not to contain every item of `notExpected`.
- `comparer`: The equality comparer to use when comparing elements.
- `message`: The message to include in the exception when every element in `notExpected` is also found (with sufficient multiplicity) in `collection`. The message is shown in test results.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if every element of `notExpected` occurs at least as many times in `collection`.

#### Remarks

Element multiplicity is significant: `[1]` is considered not to contain all of `[1, 1]` (so this assertion would pass for those inputs).

```csharp
public static void DoesNotContainAll<T>(
    [NotNull] T?[] notExpected,
    [NotNull] T?[] collection,
    [NotNull] IEqualityComparer<T?> comparer,
    string? message = "",
    [CallerArgumentExpression("notExpected")] string notExpectedExpression = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the specified array does not contain every element of `notExpected` using the specified equality comparer.

**Type parameters:**

- `T`: The type of the array items.

**Parameters:**

- `notExpected`: The array of items that must not all be present in `collection`.
- `collection`: The array that must not contain every item of `notExpected`.
- `comparer`: The equality comparer to use when comparing elements.
- `message`: The message to include in the exception when the assertion fails.
- `notExpectedExpression`: The syntactic expression of notExpected as given by the compiler via caller argument expression.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression.

**Exceptions:**

- `AssertFailedException`: Thrown if every unexpected element occurs enough times in `collection`.

#### Remarks

Element multiplicity is significant: `[1]` does not contain all of `[1, 1]`.

### DoesNotEndWith

```csharp
public static void DoesNotEndWith(
    [NotNull] string notExpectedSuffix,
    [NotNull] string value,
    string? message = "",
    [CallerArgumentExpression("notExpectedSuffix")] string notExpectedSuffixExpression = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified string does not end with the specified unexpected suffix and throws an exception if the test string ends with the suffix.

**Parameters:**

- `notExpectedSuffix`: The string expected not to be a suffix of `value`.
- `value`: The string that is expected to not end with `notExpectedSuffix`.
- `message`: The message to include in the exception when `value` ends with `notExpectedSuffix`. The message is shown in test results.
- `notExpectedSuffixExpression`: The syntactic expression of notExpectedSuffix as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: `value` is null, or `notExpectedSuffix` is null, or `value` ends with `notExpectedSuffix`.

```csharp
public static void DoesNotEndWith(
    [NotNull] string notExpectedSuffix,
    [NotNull] string value,
    StringComparison comparisonType,
    string? message = "",
    [CallerArgumentExpression("notExpectedSuffix")] string notExpectedSuffixExpression = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified string does not end with the specified unexpected suffix and throws an exception if the test string does ends with the suffix.

**Parameters:**

- `notExpectedSuffix`: The string expected not to be a suffix of `value`.
- `value`: The string that is expected to not end with `notExpectedSuffix`.
- `comparisonType`: The comparison method to compare strings `comparisonType`.
- `message`: The message to include in the exception when `value` ends with `notExpectedSuffix`. The message is shown in test results.
- `notExpectedSuffixExpression`: The syntactic expression of notExpectedSuffix as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: `value` is null, or `notExpectedSuffix` is null, or `value` ends with `notExpectedSuffix`.

### DoesNotMatchRegex

```csharp
public static void DoesNotMatchRegex(
    [NotNull] Regex pattern,
    [NotNull] string value,
    string? message = "",
    [CallerArgumentExpression("pattern")] string patternExpression = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified string does not match a regular expression and throws an exception if the string MatchesRegex the expression.

**Parameters:**

- `pattern`: The regular expression that `value` is expected to not match.
- `value`: The string that is expected not to match `pattern`.
- `message`: The message to include in the exception when `value` MatchesRegex `pattern`. The message is shown in test results.
- `patternExpression`: The syntactic expression of pattern as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: `value` is null, or `pattern` is null, or `value` MatchesRegex `pattern`.

```csharp
public static void DoesNotMatchRegex(
    [NotNull] string pattern,
    [NotNull] string value,
    string? message = "",
    [CallerArgumentExpression("pattern")] string patternExpression = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified string does not match a regular expression and throws an exception if the string MatchesRegex the expression.

**Parameters:**

- `pattern`: The regular expression that `value` is expected to not match.
- `value`: The string that is expected not to match `pattern`.
- `message`: The message to include in the exception when `value` MatchesRegex `pattern`. The message is shown in test results.
- `patternExpression`: The syntactic expression of pattern as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: `value` is null, or `pattern` is null, or `value` MatchesRegex `pattern`.

### DoesNotStartWith

```csharp
public static void DoesNotStartWith(
    [NotNull] string notExpectedPrefix,
    [NotNull] string value,
    string? message = "",
    [CallerArgumentExpression("notExpectedPrefix")] string notExpectedPrefixExpression = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified string does not begin with the specified unexpected prefix and throws an exception if the test string does start with the prefix.

**Parameters:**

- `notExpectedPrefix`: The string not expected to be a prefix of `value`.
- `value`: The string that is not expected to begin with `notExpectedPrefix`.
- `message`: The message to include in the exception when `value` begins with `notExpectedPrefix`. The message is shown in test results.
- `notExpectedPrefixExpression`: The syntactic expression of notExpectedPrefix as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: `value` is null, or `notExpectedPrefix` is null, or `value` does not start with `notExpectedPrefix`.

```csharp
public static void DoesNotStartWith(
    [NotNull] string notExpectedPrefix,
    [NotNull] string value,
    StringComparison comparisonType,
    string? message = "",
    [CallerArgumentExpression("notExpectedPrefix")] string notExpectedPrefixExpression = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified string does not begin with the specified unexpected prefix and throws an exception if the test string does start with the prefix.

**Parameters:**

- `notExpectedPrefix`: The string not expected to be a prefix of `value`.
- `value`: The string that is not expected to begin with `notExpectedPrefix`.
- `comparisonType`: The comparison method to compare strings `comparisonType`.
- `message`: The message to include in the exception when `value` begins with `notExpectedPrefix`. The message is shown in test results.
- `notExpectedPrefixExpression`: The syntactic expression of notExpectedPrefix as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: `value` is null, or `notExpectedPrefix` is null, or `value` does not start with `notExpectedPrefix`.

### EndsWith

```csharp
public static void EndsWith(
    [NotNull] string expectedSuffix,
    [NotNull] string value,
    string? message = "",
    [CallerArgumentExpression("expectedSuffix")] string expectedSuffixExpression = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified string ends with the specified suffix and throws an exception if the test string does not end with the suffix.

**Parameters:**

- `expectedSuffix`: The string expected to be a suffix of `value`.
- `value`: The string that is expected to end with `expectedSuffix`.
- `message`: The message to include in the exception when `value` does not end with `expectedSuffix`. The message is shown in test results.
- `expectedSuffixExpression`: The syntactic expression of expectedSuffix as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: `value` is null, or `expectedSuffix` is null, or `value` does not end with `expectedSuffix`.

```csharp
public static void EndsWith(
    [NotNull] string expectedSuffix,
    [NotNull] string value,
    StringComparison comparisonType,
    string? message = "",
    [CallerArgumentExpression("expectedSuffix")] string expectedSuffixExpression = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified string ends with the specified suffix and throws an exception if the test string does not end with the suffix.

**Parameters:**

- `expectedSuffix`: The string expected to be a suffix of `value`.
- `value`: The string that is expected to end with `expectedSuffix`.
- `comparisonType`: The comparison method to compare strings `comparisonType`.
- `message`: The message to include in the exception when `value` does not end with `expectedSuffix`. The message is shown in test results.
- `expectedSuffixExpression`: The syntactic expression of expectedSuffix as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: `value` is null, or `expectedSuffix` is null, or `value` does not end with `expectedSuffix`.

### Fail

```csharp
[DoesNotReturn]
public static void Fail(string message = "")
```

Throws an AssertFailedException.

**Parameters:**

- `message`: The message to include in the exception. The message is shown in test results.

**Exceptions:**

- `AssertFailedException`: Always thrown.

### HasCount

```csharp
public static void HasCount(
    int expected,
    IEnumerable collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the collection has the expected count/length.

**Parameters:**

- `expected`: The expected count.
- `collection`: The collection.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void HasCount<T>(
    int expected,
    IEnumerable<T?> collection,
    ref Assert.AssertCountInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the collection has the expected count/length.

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `expected`: The expected count.
- `collection`: The collection.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void HasCount<T>(
    int expected,
    IEnumerable<T?> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the collection has the expected count/length.

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `expected`: The expected count.
- `collection`: The collection.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void HasCount<T>(
    int expected,
    Memory<T> collection,
    ref Assert.AssertCountInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the memory has the expected count/length.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `expected`: The expected count.
- `collection`: The memory.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void HasCount<T>(
    int expected,
    Memory<T> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the memory has the expected count/length.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `expected`: The expected count.
- `collection`: The memory.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void HasCount<T>(
    int expected,
    ReadOnlyMemory<T> collection,
    ref Assert.AssertCountInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the memory has the expected count/length.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `expected`: The expected count.
- `collection`: The memory.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void HasCount<T>(
    int expected,
    ReadOnlyMemory<T> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the memory has the expected count/length.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `expected`: The expected count.
- `collection`: The memory.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void HasCount<T>(
    int expected,
    ReadOnlySpan<T> collection,
    ref Assert.AssertCountInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the span has the expected count/length.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `expected`: The expected count.
- `collection`: The span.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void HasCount<T>(
    int expected,
    ReadOnlySpan<T> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the span has the expected count/length.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `expected`: The expected count.
- `collection`: The span.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void HasCount<T>(
    int expected,
    Span<T> collection,
    ref Assert.AssertCountInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the span has the expected count/length.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `expected`: The expected count.
- `collection`: The span.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void HasCount<T>(
    int expected,
    Span<T> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the span has the expected count/length.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `expected`: The expected count.
- `collection`: The span.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void HasCount<T>(
    int expected,
    T?[] collection,
    ref Assert.AssertCountInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the array has the expected count/length.

**Type parameters:**

- `T`: The type of the array items.

**Parameters:**

- `expected`: The expected count.
- `collection`: The array.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void HasCount<T>(
    int expected,
    T?[] collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests whether the array has the expected count/length.

**Type parameters:**

- `T`: The type of the array items.

**Parameters:**

- `expected`: The expected count.
- `collection`: The array.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

### Inconclusive

```csharp
[DoesNotReturn]
public static void Inconclusive(string message = "")
```

Throws an AssertInconclusiveException.

**Parameters:**

- `message`: The message to include in the exception. The message is shown in test results.

**Exceptions:**

- `AssertInconclusiveException`: Always thrown.

### IsEmpty

```csharp
public static void IsEmpty(
    IEnumerable collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests that the collection is empty.

**Parameters:**

- `collection`: The collection.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void IsEmpty<T>(
    IEnumerable<T?> collection,
    ref Assert.AssertCountInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests that the collection is empty.

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `collection`: The collection.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void IsEmpty<T>(
    IEnumerable<T?> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests that the collection is empty.

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `collection`: The collection.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void IsEmpty<T>(
    Memory<T> collection,
    ref Assert.AssertCountInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests that the memory is empty.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `collection`: The memory.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void IsEmpty<T>(
    Memory<T> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests that the memory is empty.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `collection`: The memory.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void IsEmpty<T>(
    ReadOnlyMemory<T> collection,
    ref Assert.AssertCountInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests that the memory is empty.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `collection`: The memory.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void IsEmpty<T>(
    ReadOnlyMemory<T> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests that the memory is empty.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `collection`: The memory.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void IsEmpty<T>(
    ReadOnlySpan<T> collection,
    ref Assert.AssertCountInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests that the span is empty.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `collection`: The span.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void IsEmpty<T>(
    ReadOnlySpan<T> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests that the span is empty.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `collection`: The span.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void IsEmpty<T>(
    Span<T> collection,
    ref Assert.AssertCountInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests that the span is empty.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `collection`: The span.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void IsEmpty<T>(
    Span<T> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests that the span is empty.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `collection`: The span.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void IsEmpty<T>(
    T?[] collection,
    ref Assert.AssertCountInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests that the array is empty.

**Type parameters:**

- `T`: The type of the array items.

**Parameters:**

- `collection`: The array.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void IsEmpty<T>(
    T?[] collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests that the array is empty.

**Type parameters:**

- `T`: The type of the array items.

**Parameters:**

- `collection`: The array.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

### IsExactInstanceOfType

```csharp
public static T IsExactInstanceOfType<T>(
    [NotNull] object value,
    string? message = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified object is exactly an instance of the generic type and throws an exception if the generic type does not match exactly.

**Type parameters:**

- `T`: The expected exact type of `value`.

```csharp
public static T? IsExactInstanceOfType<T>(
    [NotNull] object value,
    ref Assert.AssertGenericIsExactInstanceOfTypeInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified object is exactly an instance of the generic type and throws an exception if the generic type does not match exactly.

**Type parameters:**

- `T`: The expected exact type of `value`.

```csharp
public static void IsExactInstanceOfType(
    [NotNull] object value,
    [NotNull] Type expectedType,
    ref Assert.AssertIsExactInstanceOfTypeInterpolatedStringHandler message,
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified object is exactly an instance of the expected type and throws an exception if the expected type does not match exactly.

**Parameters:**

- `value`: The object the test expects to be of the specified type.
- `expectedType`: The expected exact type of `value`.
- `message`: The message to include in the exception when `value` is not exactly an instance of `expectedType`. The message is shown in test results.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `value` is null or `expectedType` is not exactly the type of `value`.

```csharp
public static void IsExactInstanceOfType(
    [NotNull] object value,
    [NotNull] Type expectedType,
    string? message = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified object is exactly an instance of the expected type and throws an exception if the expected type does not match exactly.

**Parameters:**

- `value`: The object the test expects to be of the specified type.
- `expectedType`: The expected exact type of `value`.
- `message`: The message to include in the exception when `value` is not exactly an instance of `expectedType`. The message is shown in test results.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `value` is null or `expectedType` is not exactly the type of `value`.

### IsFalse

```csharp
public static void IsFalse(
    [DoesNotReturnIf(true)] bool? condition,
    ref Assert.AssertIsFalseInterpolatedStringHandler message,
    [CallerArgumentExpression("condition")] string conditionExpression = "")
```

Tests whether the specified condition is false and throws an exception if the condition is true.

**Parameters:**

- `condition`: The condition the test expects to be false.
- `message`: The message to include in the exception when `condition` is true. The message is shown in test results.
- `conditionExpression`: The syntactic expression of condition as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `condition` is true.

```csharp
public static void IsFalse(
    [DoesNotReturnIf(true)] bool? condition,
    string? message = "",
    [CallerArgumentExpression("condition")] string conditionExpression = "")
```

Tests whether the specified condition is false and throws an exception if the condition is true.

**Parameters:**

- `condition`: The condition the test expects to be false.
- `message`: The message to include in the exception when `condition` is true. The message is shown in test results.
- `conditionExpression`: The syntactic expression of condition as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `condition` is true.

### IsGreaterThan

```csharp
public static void IsGreaterThan<T>(
    T lowerBound,
    T value,
    string? message = "",
    [CallerArgumentExpression("lowerBound")] string lowerBoundExpression = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the value is greater than the lower bound and throws an exception if it is not.

**Type parameters:**

- `T`: The type of values to compare.

**Parameters:**

- `lowerBound`: The lower bound value that the value should exceed.
- `value`: The value to compare. This is the value produced by the code under test.
- `message`: The message to include in the exception when `value` is not greater than `lowerBound`. The message is shown in test results.
- `lowerBoundExpression`: The syntactic expression of lowerBound as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `value` is not greater than `lowerBound`.

### IsGreaterThanOrEqualTo

```csharp
public static void IsGreaterThanOrEqualTo<T>(
    T lowerBound,
    T value,
    string? message = "",
    [CallerArgumentExpression("lowerBound")] string lowerBoundExpression = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the value is greater than or equal to the lower bound and throws an exception if it is not.

**Type parameters:**

- `T`: The type of values to compare.

**Parameters:**

- `lowerBound`: The lower bound value that the value should meet or exceed.
- `value`: The value to compare. This is the value produced by the code under test.
- `message`: The message to include in the exception when `value` is not greater than or equal to `lowerBound`. The message is shown in test results.
- `lowerBoundExpression`: The syntactic expression of lowerBound as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `value` is not greater than or equal to `lowerBound`.

### IsInRange

```csharp
public static void IsInRange<T>(
    T minValue,
    T maxValue,
    T value,
    string? message = "",
    [CallerArgumentExpression("minValue")] string minValueExpression = "",
    [CallerArgumentExpression("maxValue")] string maxValueExpression = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified value is within the expected range (inclusive). The range includes both the minimum and maximum values.

**Type parameters:**

- `T`: The type of the values to compare.

**Parameters:**

- `minValue`: The minimum value of the expected range (inclusive).
- `maxValue`: The maximum value of the expected range (inclusive).
- `value`: The value to test.
- `message`: The message format to display when the assertion fails.
- `minValueExpression`: The syntactic expression of minValue as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `maxValueExpression`: The syntactic expression of maxValue as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

### IsInstanceOfType

```csharp
public static T IsInstanceOfType<T>(
    [NotNull] object value,
    string? message = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified object is an instance of the generic type and throws an exception if the generic type is not in the inheritance hierarchy of the object.

**Type parameters:**

- `T`: The expected type of `value`.

```csharp
public static T? IsInstanceOfType<T>(
    [NotNull] object value,
    ref Assert.AssertGenericIsInstanceOfTypeInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified object is an instance of the generic type and throws an exception if the generic type is not in the inheritance hierarchy of the object.

**Type parameters:**

- `T`: The expected type of `value`.

```csharp
public static void IsInstanceOfType(
    [NotNull] object value,
    [NotNull] Type expectedType,
    ref Assert.AssertIsInstanceOfTypeInterpolatedStringHandler message,
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified object is an instance of the expected type and throws an exception if the expected type is not in the inheritance hierarchy of the object.

**Parameters:**

- `value`: The object the test expects to be of the specified type.
- `expectedType`: The expected type of `value`.
- `message`: The message to include in the exception when `value` is not an instance of `expectedType`. The message is shown in test results.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `value` is null or `expectedType` is not in the inheritance hierarchy of `value`.

```csharp
public static void IsInstanceOfType(
    [NotNull] object value,
    [NotNull] Type expectedType,
    string? message = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified object is an instance of the expected type and throws an exception if the expected type is not in the inheritance hierarchy of the object.

**Parameters:**

- `value`: The object the test expects to be of the specified type.
- `expectedType`: The expected type of `value`.
- `message`: The message to include in the exception when `value` is not an instance of `expectedType`. The message is shown in test results.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `value` is null or `expectedType` is not in the inheritance hierarchy of `value`.

### IsLessThan

```csharp
public static void IsLessThan<T>(
    T upperBound,
    T value,
    string? message = "",
    [CallerArgumentExpression("upperBound")] string upperBoundExpression = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the value is less than the upper bound and throws an exception if it is not.

**Type parameters:**

- `T`: The type of values to compare.

**Parameters:**

- `upperBound`: The upper bound value that the value should be less than.
- `value`: The value to compare. This is the value produced by the code under test.
- `message`: The message to include in the exception when `value` is not less than `upperBound`. The message is shown in test results.
- `upperBoundExpression`: The syntactic expression of upperBound as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `value` is not less than `upperBound`.

### IsLessThanOrEqualTo

```csharp
public static void IsLessThanOrEqualTo<T>(
    T upperBound,
    T value,
    string? message = "",
    [CallerArgumentExpression("upperBound")] string upperBoundExpression = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the value is less than or equal to the upper bound and throws an exception if it is not.

**Type parameters:**

- `T`: The type of values to compare.

**Parameters:**

- `upperBound`: The upper bound value that the value should not exceed.
- `value`: The value to compare. This is the value produced by the code under test.
- `message`: The message to include in the exception when `value` is not less than or equal to `upperBound`. The message is shown in test results.
- `upperBoundExpression`: The syntactic expression of upperBound as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `value` is not less than or equal to `upperBound`.

### IsNegative

```csharp
public static void IsNegative<T>(
    T value,
    string? message = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified value is negative and throws an exception if it is not.

**Type parameters:**

- `T`: The type of value to test.

**Parameters:**

- `value`: The value to test.
- `message`: The message to include in the exception when `value` is not negative. The message is shown in test results.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `value` is not negative.

### IsNotEmpty

```csharp
public static void IsNotEmpty(
    IEnumerable collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests that the collection is not empty.

**Parameters:**

- `collection`: The collection.
- `message`: The message format to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void IsNotEmpty<T>(
    IEnumerable<T?> collection,
    ref Assert.AssertIsNotEmptyInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests that the collection is not empty.

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `collection`: The collection.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void IsNotEmpty<T>(
    IEnumerable<T?> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests that the collection is not empty.

**Type parameters:**

- `T`: The type of the collection items.

**Parameters:**

- `collection`: The collection.
- `message`: The message format to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void IsNotEmpty<T>(
    Memory<T> collection,
    ref Assert.AssertIsNotEmptyInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests that the memory is not empty.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `collection`: The memory.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void IsNotEmpty<T>(
    Memory<T> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests that the memory is not empty.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `collection`: The memory.
- `message`: The message format to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void IsNotEmpty<T>(
    ReadOnlyMemory<T> collection,
    ref Assert.AssertIsNotEmptyInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests that the memory is not empty.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `collection`: The memory.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void IsNotEmpty<T>(
    ReadOnlyMemory<T> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests that the memory is not empty.

**Type parameters:**

- `T`: The type of the memory items.

**Parameters:**

- `collection`: The memory.
- `message`: The message format to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void IsNotEmpty<T>(
    ReadOnlySpan<T> collection,
    ref Assert.AssertIsNotEmptyInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests that the span is not empty.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `collection`: The span.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void IsNotEmpty<T>(
    ReadOnlySpan<T> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests that the span is not empty.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `collection`: The span.
- `message`: The message format to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void IsNotEmpty<T>(
    Span<T> collection,
    ref Assert.AssertIsNotEmptyInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests that the span is not empty.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `collection`: The span.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void IsNotEmpty<T>(
    Span<T> collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests that the span is not empty.

**Type parameters:**

- `T`: The type of the span items.

**Parameters:**

- `collection`: The span.
- `message`: The message format to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void IsNotEmpty<T>(
    T?[] collection,
    ref Assert.AssertIsNotEmptyInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests that the array is not empty.

**Type parameters:**

- `T`: The type of the array items.

**Parameters:**

- `collection`: The array.
- `message`: The message to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

```csharp
public static void IsNotEmpty<T>(
    T?[] collection,
    string? message = "",
    [CallerArgumentExpression("collection")] string collectionExpression = "")
```

Tests that the array is not empty.

**Type parameters:**

- `T`: The type of the array items.

**Parameters:**

- `collection`: The array.
- `message`: The message format to display when the assertion fails.
- `collectionExpression`: The syntactic expression of collection as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

### IsNotExactInstanceOfType

```csharp
public static void IsNotExactInstanceOfType<T>(
    object? value,
    ref Assert.AssertGenericIsNotExactInstanceOfTypeInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified object is not exactly an instance of the wrong generic type and throws an exception if the specified type matches exactly.

**Type parameters:**

- `T`: The exact type that `value` should not be.

```csharp
public static void IsNotExactInstanceOfType<T>(
    object? value,
    string? message = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified object is not exactly an instance of the wrong generic type and throws an exception if the specified type matches exactly.

**Type parameters:**

- `T`: The exact type that `value` should not be.

```csharp
public static void IsNotExactInstanceOfType(
    object? value,
    [NotNull] Type wrongType,
    ref Assert.AssertIsNotExactInstanceOfTypeInterpolatedStringHandler message,
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified object is not exactly an instance of the wrong type and throws an exception if the specified type matches exactly.

**Parameters:**

- `value`: The object the test expects not to be exactly of the specified type.
- `wrongType`: The exact type that `value` should not be.
- `message`: The message to include in the exception when `value` is exactly an instance of `wrongType`. The message is shown in test results.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `value` is not null and `wrongType` is exactly the type of `value`.

```csharp
public static void IsNotExactInstanceOfType(
    object? value,
    [NotNull] Type wrongType,
    string? message = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified object is not exactly an instance of the wrong type and throws an exception if the specified type matches exactly.

**Parameters:**

- `value`: The object the test expects not to be exactly of the specified type.
- `wrongType`: The exact type that `value` should not be.
- `message`: The message to include in the exception when `value` is exactly an instance of `wrongType`. The message is shown in test results.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `value` is not null and `wrongType` is exactly the type of `value`.

### IsNotInstanceOfType

```csharp
public static void IsNotInstanceOfType<T>(
    object? value,
    Assert.AssertGenericIsNotInstanceOfTypeInterpolatedStringHandler<T> message,
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified object is not an instance of the wrong generic type and throws an exception if the specified type is in the inheritance hierarchy of the object.

**Type parameters:**

- `T`: The type that `value` should not be.

```csharp
public static void IsNotInstanceOfType<T>(
    object? value,
    string? message = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified object is not an instance of the wrong generic type and throws an exception if the specified type is in the inheritance hierarchy of the object.

**Type parameters:**

- `T`: The type that `value` should not be.

```csharp
public static void IsNotInstanceOfType(
    object? value,
    [NotNull] Type wrongType,
    ref Assert.AssertIsNotInstanceOfTypeInterpolatedStringHandler message,
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified object is not an instance of the wrong type and throws an exception if the specified type is in the inheritance hierarchy of the object.

**Parameters:**

- `value`: The object the test expects not to be of the specified type.
- `wrongType`: The type that `value` should not be.
- `message`: The message to include in the exception when `value` is an instance of `wrongType`. The message is shown in test results.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `value` is not null and `wrongType` is in the inheritance hierarchy of `value`.

```csharp
public static void IsNotInstanceOfType(
    object? value,
    [NotNull] Type wrongType,
    string? message = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified object is not an instance of the wrong type and throws an exception if the specified type is in the inheritance hierarchy of the object.

**Parameters:**

- `value`: The object the test expects not to be of the specified type.
- `wrongType`: The type that `value` should not be.
- `message`: The message to include in the exception when `value` is an instance of `wrongType`. The message is shown in test results.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `value` is not null and `wrongType` is in the inheritance hierarchy of `value`.

### IsNotNull

```csharp
public static void IsNotNull(
    [NotNull] object value,
    ref Assert.AssertIsNotNullInterpolatedStringHandler message,
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified object is null and throws an exception if it is not.

**Parameters:**

- `value`: The object the test expects to be null.
- `message`: The message to include in the exception when `value` is not null. The message is shown in test results.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `value` is not null.

```csharp
public static void IsNotNull(
    [NotNull] object value,
    string? message = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified object is non-null and throws an exception if it is null.

**Parameters:**

- `value`: The object the test expects not to be null.
- `message`: The message to include in the exception when `value` is null. The message is shown in test results.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `value` is null.

### IsNull

```csharp
public static void IsNull(
    object? value,
    ref Assert.AssertIsNullInterpolatedStringHandler message,
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified object is null and throws an exception if it is not.

**Parameters:**

- `value`: The object the test expects to be null.
- `message`: The message to include in the exception when `value` is not null. The message is shown in test results.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `value` is not null.

```csharp
public static void IsNull(
    object? value,
    string? message = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified object is null and throws an exception if it is not.

**Parameters:**

- `value`: The object the test expects to be null.
- `message`: The message to include in the exception when `value` is not null. The message is shown in test results.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `value` is not null.

### IsPositive

```csharp
public static void IsPositive<T>(
    T value,
    string? message = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified value is positive and throws an exception if it is not.

**Type parameters:**

- `T`: The type of value to test.

**Parameters:**

- `value`: The value to test.
- `message`: The message to include in the exception when `value` is not positive. The message is shown in test results.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `value` is not positive.

### IsTrue

```csharp
public static void IsTrue(
    [DoesNotReturnIf(false)] bool? condition,
    ref Assert.AssertIsTrueInterpolatedStringHandler message,
    [CallerArgumentExpression("condition")] string conditionExpression = "")
```

Tests whether the specified condition is true and throws an exception if the condition is false.

**Parameters:**

- `condition`: The condition the test expects to be true.
- `message`: The message to include in the exception when `condition` is false. The message is shown in test results.
- `conditionExpression`: The syntactic expression of condition as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `condition` is false.

```csharp
public static void IsTrue(
    [DoesNotReturnIf(false)] bool? condition,
    string? message = "",
    [CallerArgumentExpression("condition")] string conditionExpression = "")
```

Tests whether the specified condition is true and throws an exception if the condition is false.

**Parameters:**

- `condition`: The condition the test expects to be true.
- `message`: The message to include in the exception when `condition` is false. The message is shown in test results.
- `conditionExpression`: The syntactic expression of condition as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: Thrown if `condition` is false.

### MatchesRegex

```csharp
public static void MatchesRegex(
    [NotNull] Regex pattern,
    [NotNull] string value,
    string? message = "",
    [CallerArgumentExpression("pattern")] string patternExpression = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified string MatchesRegex a regular expression and throws an exception if the string does not match the expression.

**Parameters:**

- `pattern`: The regular expression that `value` is expected to match.
- `value`: The string that is expected to match `pattern`.
- `message`: The message to include in the exception when `value` does not match `pattern`. The message is shown in test results.
- `patternExpression`: The syntactic expression of pattern as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: `value` is null, or `pattern` is null, or `value` does not match `pattern`.

```csharp
public static void MatchesRegex(
    [NotNull] string pattern,
    [NotNull] string value,
    string? message = "",
    [CallerArgumentExpression("pattern")] string patternExpression = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified string MatchesRegex a regular expression and throws an exception if the string does not match the expression.

**Parameters:**

- `pattern`: The regular expression that `value` is expected to match.
- `value`: The string that is expected to match `pattern`.
- `message`: The message to include in the exception when `value` does not match `pattern`. The message is shown in test results.
- `patternExpression`: The syntactic expression of pattern as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: `value` is null, or `pattern` is null, or `value` does not match `pattern`.

### Scope

```csharp
[Experimental("MSTESTEXP", UrlFormat = "https://aka.ms/mstest/diagnostics#{0}")]
public static IDisposable Scope()
```

Creates a new assertion scope that collects assertion failures instead of throwing them immediately. When the returned scope is disposed, all collected failures are thrown as a single `AssertFailedException`.

**Returns:** An `IDisposable` representing the assertion scope.

#### Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

#### Example

```csharp
using (Assert.Scope())
{
    Assert.AreEqual(1, 2);  // collected, not thrown
    Assert.IsTrue(false);   // collected, not thrown
}
// AssertFailedException is thrown here with all collected failures.
```

### StartsWith

```csharp
public static void StartsWith(
    [NotNull] string expectedPrefix,
    [NotNull] string value,
    string? message = "",
    [CallerArgumentExpression("expectedPrefix")] string expectedPrefixExpression = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified string begins with the specified prefix and throws an exception if the test string does not start with the prefix.

**Parameters:**

- `expectedPrefix`: The string expected to be a prefix of `value`.
- `value`: The string that is expected to begin with `expectedPrefix`.
- `message`: The message to include in the exception when `value` does not begin with `expectedPrefix`. The message is shown in test results.
- `expectedPrefixExpression`: The syntactic expression of expectedPrefix as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: `value` is null, or `expectedPrefix` is null, or `value` does not start with `expectedPrefix`.

```csharp
public static void StartsWith(
    [NotNull] string expectedPrefix,
    [NotNull] string value,
    StringComparison comparisonType,
    string? message = "",
    [CallerArgumentExpression("expectedPrefix")] string expectedPrefixExpression = "",
    [CallerArgumentExpression("value")] string valueExpression = "")
```

Tests whether the specified string begins with the specified prefix and throws an exception if the test string does not start with the prefix.

**Parameters:**

- `expectedPrefix`: The string expected to be a prefix of `value`.
- `value`: The string that is expected to begin with `expectedPrefix`.
- `comparisonType`: The comparison method to compare strings `comparisonType`.
- `message`: The message to include in the exception when `value` does not begin with `expectedPrefix`. The message is shown in test results.
- `expectedPrefixExpression`: The syntactic expression of expectedPrefix as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.
- `valueExpression`: The syntactic expression of value as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Exceptions:**

- `AssertFailedException`: `value` is null, or `expectedPrefix` is null, or `value` does not start with `expectedPrefix`.

### Throws

```csharp
public static TException Throws<TException>(
    Action action,
    Func<Exception?, string> messageBuilder,
    [CallerArgumentExpression("action")] string actionExpression = "")
```

Asserts that the delegate `action` throws an exception of type `TException` (or derived type) and throws `AssertFailedException` if code does not throw exception or throws exception of type other than `TException`.

**Type parameters:**

- `TException`: The type of exception expected to be thrown.

**Parameters:**

- `action`: Delegate to code to be tested and which is expected to throw exception.
- `messageBuilder`: A func that takes the thrown Exception (or null if the action didn't throw any exception) to construct the message to include in the exception when `action` does not throw exception of type `TException`.
- `actionExpression`: The syntactic expression of action as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The exception that was thrown.

**Exceptions:**

- `AssertFailedException`: Thrown if `action` does not throw exception of type `TException`.

```csharp
public static TException Throws<TException>(
    Action action,
    ref Assert.AssertNonStrictThrowsInterpolatedStringHandler<TException> message,
    [CallerArgumentExpression("action")] string actionExpression = "")
```

Asserts that the delegate `action` throws an exception of type `TException` (or derived type) and throws `AssertFailedException` if code does not throw exception or throws exception of type other than `TException`.

**Type parameters:**

- `TException`: The type of exception expected to be thrown.

**Parameters:**

- `action`: Delegate to code to be tested and which is expected to throw exception.
- `message`: The message to include in the exception when `action` does not throw exception of type `TException`.
- `actionExpression`: The syntactic expression of action as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The exception that was thrown.

**Exceptions:**

- `AssertFailedException`: Thrown if `action` does not throw exception of type `TException`.

```csharp
public static TException Throws<TException>(
    Action action,
    string? message = "",
    [CallerArgumentExpression("action")] string actionExpression = "")
```

Asserts that the delegate `action` throws an exception of type `TException` (or derived type) and throws `AssertFailedException` if code does not throw exception or throws exception of type other than `TException`.

**Type parameters:**

- `TException`: The type of exception expected to be thrown.

**Parameters:**

- `action`: Delegate to code to be tested and which is expected to throw exception.
- `message`: The message to include in the exception when `action` does not throw exception of type `TException`.
- `actionExpression`: The syntactic expression of action as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The exception that was thrown.

**Exceptions:**

- `AssertFailedException`: Thrown if `action` does not throw exception of type `TException`.

```csharp
public static TException Throws<TException>(
    Func<object?> action,
    Func<Exception?, string> messageBuilder,
    [CallerArgumentExpression("action")] string actionExpression = "")
```

Asserts that the delegate `action` throws an exception of type `TException` (or derived type) and throws `AssertFailedException` if code does not throw exception or throws exception of type other than `TException`.

**Type parameters:**

- `TException`: The type of exception expected to be thrown.

**Parameters:**

- `action`: Delegate to code to be tested and which is expected to throw exception.
- `messageBuilder`: A func that takes the thrown Exception (or null if the action didn't throw any exception) to construct the message to include in the exception when `action` does not throw exception of type `TException`.
- `actionExpression`: The syntactic expression of action as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The exception that was thrown.

**Exceptions:**

- `AssertFailedException`: Thrown if `action` does not throw exception of type `TException`.

```csharp
public static TException Throws<TException>(
    Func<object?> action,
    ref Assert.AssertNonStrictThrowsInterpolatedStringHandler<TException> message,
    [CallerArgumentExpression("action")] string actionExpression = "")
```

Asserts that the delegate `action` throws an exception of type `TException` (or derived type) and throws `AssertFailedException` if code does not throw exception or throws exception of type other than `TException`.

**Type parameters:**

- `TException`: The type of exception expected to be thrown.

**Parameters:**

- `action`: Delegate to code to be tested and which is expected to throw exception.
- `message`: The message to include in the exception when `action` does not throw exception of type `TException`.
- `actionExpression`: The syntactic expression of action as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The exception that was thrown.

**Exceptions:**

- `AssertFailedException`: Thrown if `action` does not throw exception of type `TException`.

```csharp
public static TException Throws<TException>(
    Func<object?> action,
    string? message = "",
    [CallerArgumentExpression("action")] string actionExpression = "")
```

Asserts that the delegate `action` throws an exception of type `TException` (or derived type) and throws `AssertFailedException` if code does not throw exception or throws exception of type other than `TException`.

**Type parameters:**

- `TException`: The type of exception expected to be thrown.

**Parameters:**

- `action`: Delegate to code to be tested and which is expected to throw exception.
- `message`: The message to include in the exception when `action` does not throw exception of type `TException`.
- `actionExpression`: The syntactic expression of action as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The exception that was thrown.

**Exceptions:**

- `AssertFailedException`: Thrown if `action` does not throw exception of type `TException`.

### ThrowsAsync

```csharp
public static Task<TException> ThrowsAsync<TException>(
    Func<Task> action,
    Func<Exception?, string> messageBuilder,
    [CallerArgumentExpression("action")] string actionExpression = "")
```

Asserts that the delegate `action` throws an exception of type `TException` (or derived type) and throws `AssertFailedException` if code does not throw exception or throws exception of type other than `TException`.

**Type parameters:**

- `TException`: The type of exception expected to be thrown.

**Parameters:**

- `action`: Delegate to code to be tested and which is expected to throw exception.
- `messageBuilder`: A func that takes the thrown Exception (or null if the action didn't throw any exception) to construct the message to include in the exception when `action` does not throw exception of type `TException`.
- `actionExpression`: The syntactic expression of action as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The exception that was thrown.

**Exceptions:**

- `AssertFailedException`: Thrown if `action` does not throw exception of type `TException`.

```csharp
public static Task<TException> ThrowsAsync<TException>(
    Func<Task> action,
    ref Assert.AssertNonStrictThrowsAsyncInterpolatedStringHandler<TException> message,
    [CallerArgumentExpression("action")] string actionExpression = "")
```

Asserts that the delegate `action` throws an exception of type `TException` (or derived type) and throws `AssertFailedException` if code does not throw exception or throws exception of type other than `TException`.

**Type parameters:**

- `TException`: The type of exception expected to be thrown.

**Parameters:**

- `action`: Delegate to code to be tested and which is expected to throw exception.
- `message`: The message to include in the exception when `action` does not throw exception of type `TException`.
- `actionExpression`: The syntactic expression of action as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The exception that was thrown.

**Exceptions:**

- `AssertFailedException`: Thrown if `action` does not throw exception of type `TException`.

```csharp
public static Task<TException> ThrowsAsync<TException>(
    Func<Task> action,
    string? message = "",
    [CallerArgumentExpression("action")] string actionExpression = "")
```

Asserts that the delegate `action` throws an exception of type `TException` (or derived type) and throws `AssertFailedException` if code does not throw exception or throws exception of type other than `TException`.

**Type parameters:**

- `TException`: The type of exception expected to be thrown.

**Parameters:**

- `action`: Delegate to code to be tested and which is expected to throw exception.
- `message`: The message to include in the exception when `action` does not throw exception of type `TException`.
- `actionExpression`: The syntactic expression of action as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The exception that was thrown.

**Exceptions:**

- `AssertFailedException`: Thrown if `action` does not throw exception of type `TException`.

### ThrowsExactly

```csharp
public static TException ThrowsExactly<TException>(
    Action action,
    Func<Exception?, string> messageBuilder,
    [CallerArgumentExpression("action")] string actionExpression = "")
```

Asserts that the delegate `action` throws an exception of type `TException` (and not of derived type) and throws `AssertFailedException` if code does not throw exception or throws exception of type other than `TException`.

**Type parameters:**

- `TException`: The type of exception expected to be thrown.

**Parameters:**

- `action`: Delegate to code to be tested and which is expected to throw exception.
- `messageBuilder`: A func that takes the thrown Exception (or null if the action didn't throw any exception) to construct the message to include in the exception when `action` does not throw exception of type `TException`.
- `actionExpression`: The syntactic expression of action as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The exception that was thrown.

**Exceptions:**

- `AssertFailedException`: Thrown if `action` does not throw exception of type `TException`.

```csharp
public static TException ThrowsExactly<TException>(
    Action action,
    ref Assert.AssertThrowsExactlyInterpolatedStringHandler<TException> message,
    [CallerArgumentExpression("action")] string actionExpression = "")
```

Asserts that the delegate `action` throws an exception of type `TException` (and not of derived type) and throws `AssertFailedException` if code does not throw exception or throws exception of type other than `TException`.

**Type parameters:**

- `TException`: The type of exception expected to be thrown.

**Parameters:**

- `action`: Delegate to code to be tested and which is expected to throw exception.
- `message`: The message to include in the exception when `action` does not throw exception of type `TException`.
- `actionExpression`: The syntactic expression of action as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The exception that was thrown.

**Exceptions:**

- `AssertFailedException`: Thrown if `action` does not throw exception of type `TException`.

```csharp
public static TException ThrowsExactly<TException>(
    Action action,
    string? message = "",
    [CallerArgumentExpression("action")] string actionExpression = "")
```

Asserts that the delegate `action` throws an exception of type `TException` (and not of derived type) and throws `AssertFailedException` if code does not throw exception or throws exception of type other than `TException`.

**Type parameters:**

- `TException`: The type of exception expected to be thrown.

**Parameters:**

- `action`: Delegate to code to be tested and which is expected to throw exception.
- `message`: The message to include in the exception when `action` does not throw exception of type `TException`.
- `actionExpression`: The syntactic expression of action as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The exception that was thrown.

**Exceptions:**

- `AssertFailedException`: Thrown if `action` does not throw exception of type `TException`.

```csharp
public static TException ThrowsExactly<TException>(
    Func<object?> action,
    Func<Exception?, string> messageBuilder,
    [CallerArgumentExpression("action")] string actionExpression = "")
```

Asserts that the delegate `action` throws an exception of type `TException` (and not of derived type) and throws `AssertFailedException` if code does not throw exception or throws exception of type other than `TException`.

**Type parameters:**

- `TException`: The type of exception expected to be thrown.

**Parameters:**

- `action`: Delegate to code to be tested and which is expected to throw exception.
- `messageBuilder`: A func that takes the thrown Exception (or null if the action didn't throw any exception) to construct the message to include in the exception when `action` does not throw exception of type `TException`.
- `actionExpression`: The syntactic expression of action as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The exception that was thrown.

**Exceptions:**

- `AssertFailedException`: Thrown if `action` does not throw exception of type `TException`.

```csharp
public static TException ThrowsExactly<TException>(
    Func<object?> action,
    ref Assert.AssertThrowsExactlyInterpolatedStringHandler<TException> message,
    [CallerArgumentExpression("action")] string actionExpression = "")
```

Asserts that the delegate `action` throws an exception of type `TException` (and not of derived type) and throws `AssertFailedException` if code does not throw exception or throws exception of type other than `TException`.

**Type parameters:**

- `TException`: The type of exception expected to be thrown.

**Parameters:**

- `action`: Delegate to code to be tested and which is expected to throw exception.
- `message`: The message to include in the exception when `action` does not throw exception of type `TException`.
- `actionExpression`: The syntactic expression of action as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The exception that was thrown.

**Exceptions:**

- `AssertFailedException`: Thrown if `action` does not throw exception of type `TException`.

```csharp
public static TException ThrowsExactly<TException>(
    Func<object?> action,
    string? message = "",
    [CallerArgumentExpression("action")] string actionExpression = "")
```

Asserts that the delegate `action` throws an exception of type `TException` (and not of derived type) and throws `AssertFailedException` if code does not throw exception or throws exception of type other than `TException`.

**Type parameters:**

- `TException`: The type of exception expected to be thrown.

**Parameters:**

- `action`: Delegate to code to be tested and which is expected to throw exception.
- `message`: The message to include in the exception when `action` does not throw exception of type `TException`.
- `actionExpression`: The syntactic expression of action as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The exception that was thrown.

**Exceptions:**

- `AssertFailedException`: Thrown if `action` does not throw exception of type `TException`.

### ThrowsExactlyAsync

```csharp
public static Task<TException> ThrowsExactlyAsync<TException>(
    Func<Task> action,
    Func<Exception?, string> messageBuilder,
    [CallerArgumentExpression("action")] string actionExpression = "")
```

Asserts that the delegate `action` throws an exception of type `TException` (and not of derived type) and throws `AssertFailedException` if code does not throw exception or throws exception of type other than `TException`.

**Type parameters:**

- `TException`: The type of exception expected to be thrown.

**Parameters:**

- `action`: Delegate to code to be tested and which is expected to throw exception.
- `messageBuilder`: A func that takes the thrown Exception (or null if the action didn't throw any exception) to construct the message to include in the exception when `action` does not throw exception of type `TException`.
- `actionExpression`: The syntactic expression of action as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The exception that was thrown.

**Exceptions:**

- `AssertFailedException`: Thrown if `action` does not throw exception of type `TException`.

```csharp
public static Task<TException> ThrowsExactlyAsync<TException>(
    Func<Task> action,
    ref Assert.AssertThrowsExactlyAsyncInterpolatedStringHandler<TException> message,
    [CallerArgumentExpression("action")] string actionExpression = "")
```

Asserts that the delegate `action` throws an exception of type `TException` (and not of derived type) and throws `AssertFailedException` if code does not throw exception or throws exception of type other than `TException`.

**Type parameters:**

- `TException`: The type of exception expected to be thrown.

**Parameters:**

- `action`: Delegate to code to be tested and which is expected to throw exception.
- `message`: The message to include in the exception when `action` does not throw exception of type `TException`.
- `actionExpression`: The syntactic expression of action as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The exception that was thrown.

**Exceptions:**

- `AssertFailedException`: Thrown if `action` does not throw exception of type `TException`.

```csharp
public static Task<TException> ThrowsExactlyAsync<TException>(
    Func<Task> action,
    string? message = "",
    [CallerArgumentExpression("action")] string actionExpression = "")
```

Asserts that the delegate `action` throws an exception of type `TException` (and not of derived type) and throws `AssertFailedException` if code does not throw exception or throws exception of type other than `TException`.

**Type parameters:**

- `TException`: The type of exception expected to be thrown.

**Parameters:**

- `action`: Delegate to code to be tested and which is expected to throw exception.
- `message`: The message to include in the exception when `action` does not throw exception of type `TException`.
- `actionExpression`: The syntactic expression of action as given by the compiler via caller argument expression. Users shouldn't pass a value for this parameter.

**Returns:** The exception that was thrown.

**Exceptions:**

- `AssertFailedException`: Thrown if `action` does not throw exception of type `TException`.
