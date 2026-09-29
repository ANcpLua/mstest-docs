# CollectionAssert class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

A collection of helper classes to test various conditions associated with collections within unit tests. If the condition being tested is not met, an exception is thrown.

```csharp
public sealed class CollectionAssert
```

## Properties

### That

```csharp
public static CollectionAssert That { get; }
```

Gets the singleton instance of the CollectionAssert functionality.

#### Remarks

Users can use this to plug-in custom assertions through C# extension methods. For instance, the signature of a custom assertion provider could be `public static void AreEqualUnordered(this CollectionAssert customAssert, ICollection expected, ICollection actual)` and the call-site would be `CollectionAssert.That.AreEqualUnordered(list1, list2);`.

For new custom assertions, prefer extending `Assert.That` instead, because `CollectionAssert` is likely to be deprecated in a future release. For more information, see [Extension hooks on StringAssert and CollectionAssert](https://learn.microsoft.com/dotnet/core/testing/unit-testing-mstest-writing-tests-assertions#extension-hooks-on-stringassert-and-collectionassert).

#### Example

The following example defines a custom `AreEqualUnordered` assertion as an extension method on `CollectionAssert` and invokes it through `CollectionAssert.That`:

```csharp
using System.Collections.Generic;
using System.Linq;
using Microsoft.VisualStudio.TestTools.UnitTesting;
            
public static class CustomCollectionAssertExtensions
{
    public static void AreEqualUnordered<T>(this CollectionAssert collectionAssert, IEnumerable<T> expected, IEnumerable<T> actual)
    {
        if (!expected.OrderBy(x => x).SequenceEqual(actual.OrderBy(x => x)))
        {
            throw new AssertFailedException("CollectionAssert.That.AreEqualUnordered failed. Collections do not contain the same elements.");
        }
    }
}
            
[TestClass]
public class SetTests
{
    [TestMethod]
    public void Items_MatchRegardlessOfOrder()
    {
        CollectionAssert.That.AreEqualUnordered(new[] { 1, 2, 3 }, new[] { 3, 1, 2 });
    }
}
```

## Methods

### AllItemsAreInstancesOfType

```csharp
public static void AllItemsAreInstancesOfType([NotNull] ICollection collection, [NotNull] Type expectedType)
```

Tests whether all elements in the specified collection are instances of the expected type and throws an exception if the expected type is not in the inheritance hierarchy of one or more of the elements.

**Parameters:**

- `collection`: The collection containing elements the test expects to be of the specified type.
- `expectedType`: The expected type of each element of `collection`.

**Exceptions:**

- `AssertFailedException`: `collection` is null or, `expectedType` is null, or some elements of `collection` do not inherit/implement `expectedType`.

```csharp
public static void AllItemsAreInstancesOfType(
    [NotNull] ICollection collection,
    [NotNull] Type expectedType,
    string? message)
```

Tests whether all elements in the specified collection are instances of the expected type and throws an exception if the expected type is not in the inheritance hierarchy of one or more of the elements.

**Parameters:**

- `collection`: The collection containing elements the test expects to be of the specified type.
- `expectedType`: The expected type of each element of `collection`.
- `message`: The message to include in the exception when an element in `collection` is not an instance of `expectedType`. The message is shown in test results.

**Exceptions:**

- `AssertFailedException`: `collection` is null or, `expectedType` is null, or some elements of `collection` do not inherit/implement `expectedType`.

### AllItemsAreNotNull

```csharp
public static void AllItemsAreNotNull([NotNull] ICollection collection)
```

Tests whether all items in the specified collection are non-null and throws an exception if any element is null.

**Parameters:**

- `collection`: The collection in which to search for null elements.

**Exceptions:**

- `AssertFailedException`: `collection` is null, or `collection` contains a null element.

```csharp
public static void AllItemsAreNotNull([NotNull] ICollection collection, string? message)
```

Tests whether all items in the specified collection are non-null and throws an exception if any element is null.

**Parameters:**

- `collection`: The collection in which to search for null elements.
- `message`: The message to include in the exception when `collection` contains a null element. The message is shown in test results.

**Exceptions:**

- `AssertFailedException`: `collection` is null, or `collection` contains a null element.

### AllItemsAreUnique

```csharp
public static void AllItemsAreUnique([NotNull] ICollection collection)
```

Tests whether all items in the specified collection are unique or not and throws if any two elements in the collection are equal.

**Parameters:**

- `collection`: The collection in which to search for duplicate elements.

**Exceptions:**

- `AssertFailedException`: `collection` is null, or `collection` contains at least one duplicate element.

```csharp
public static void AllItemsAreUnique([NotNull] ICollection collection, string? message)
```

Tests whether all items in the specified collection are unique or not and throws if any two elements in the collection are equal.

**Parameters:**

- `collection`: The collection in which to search for duplicate elements.
- `message`: The message to include in the exception when `collection` contains at least one duplicate element. The message is shown in test results.

**Exceptions:**

- `AssertFailedException`: `collection` is null, or `collection` contains at least one duplicate element.

### AreEqual

```csharp
public static void AreEqual(ICollection? expected, ICollection? actual)
```

Tests whether the specified collections are equal and throws an exception if the two collections are not equal. Equality is defined as having the same elements in the same order and quantity. Whether two elements are the same is checked using `Object.Equals(Object,Object)` method. Different references to the same value are considered equal.

**Parameters:**

- `expected`: The first collection to compare. This is the collection the tests expects.
- `actual`: The second collection to compare. This is the collection produced by the code under test.

**Exceptions:**

- `AssertFailedException`: Thrown if `expected` is not equal to `actual`.

```csharp
public static void AreEqual(
    ICollection? expected,
    ICollection? actual,
    [NotNull] IComparer comparer)
```

Tests whether the specified collections are equal and throws an exception if the two collections are not equal. Equality is defined as having the same elements in the same order and quantity. Different references to the same value are considered equal.

**Parameters:**

- `expected`: The first collection to compare. This is the collection the tests expects.
- `actual`: The second collection to compare. This is the collection produced by the code under test.
- `comparer`: The compare implementation to use when comparing elements of the collection.

**Exceptions:**

- `AssertFailedException`: Thrown if `expected` is not equal to `actual`.

```csharp
public static void AreEqual(
    ICollection? expected,
    ICollection? actual,
    string? message)
```

Tests whether the specified collections are equal and throws an exception if the two collections are not equal. Equality is defined as having the same elements in the same order and quantity. Whether two elements are the same is checked using `Object.Equals(Object,Object)` method. Different references to the same value are considered equal.

**Parameters:**

- `expected`: The first collection to compare. This is the collection the tests expects.
- `actual`: The second collection to compare. This is the collection produced by the code under test.
- `message`: The message to include in the exception when `actual` is not equal to `expected`. The message is shown in test results.

**Exceptions:**

- `AssertFailedException`: Thrown if `expected` is not equal to `actual`.

```csharp
public static void AreEqual(
    ICollection? expected,
    ICollection? actual,
    [NotNull] IComparer comparer,
    string? message)
```

Tests whether the specified collections are equal and throws an exception if the two collections are not equal. Equality is defined as having the same elements in the same order and quantity. Different references to the same value are considered equal.

**Parameters:**

- `expected`: The first collection to compare. This is the collection the tests expects.
- `actual`: The second collection to compare. This is the collection produced by the code under test.
- `comparer`: The compare implementation to use when comparing elements of the collection.
- `message`: The message to include in the exception when `actual` is not equal to `expected`. The message is shown in test results.

**Exceptions:**

- `AssertFailedException`: Thrown if `expected` is not equal to `actual`.

### AreEquivalent

```csharp
public static void AreEquivalent(ICollection? expected, ICollection? actual)
```

Tests whether two collections contain the same elements and throws an exception if either collection contains an element not in the other collection.

**Parameters:**

- `expected`: The first collection to compare. This contains the elements the test expects.
- `actual`: The second collection to compare. This is the collection produced by the code under test.

**Exceptions:**

- `AssertFailedException`: `expected` and `actual` nullabilities don't match, or if any element was found in one of the collections but not the other.

```csharp
public static void AreEquivalent(
    ICollection? expected,
    ICollection? actual,
    string? message)
```

Tests whether two collections contain the same elements and throws an exception if either collection contains an element not in the other collection.

**Parameters:**

- `expected`: The first collection to compare. This contains the elements the test expects.
- `actual`: The second collection to compare. This is the collection produced by the code under test.
- `message`: The message to include in the exception when an element was found in one of the collections but not the other. The message is shown in test results.

**Exceptions:**

- `AssertFailedException`: `expected` and `actual` nullabilities don't match, or if any element was found in one of the collections but not the other.

```csharp
public static void AreEquivalent<T>(
    IEnumerable<T?>? expected,
    IEnumerable<T?>? actual,
    [NotNull] IEqualityComparer<T?> comparer)
```

Tests whether two collections contain the same elements and throws an exception if either collection contains an element not in the other collection.

**Type parameters:**

- `T`: The type of values to compare.

**Parameters:**

- `expected`: The first collection to compare. This contains the elements the test expects.
- `actual`: The second collection to compare. This is the collection produced by the code under test.
- `comparer`: The compare implementation to use when comparing elements of the collection.

**Exceptions:**

- `AssertFailedException`: `expected` and `actual` nullabilities don't match, or if any element was found in one of the collections but not the other.

```csharp
public static void AreEquivalent<T>(
    IEnumerable<T?>? expected,
    IEnumerable<T?>? actual,
    [NotNull] IEqualityComparer<T?> comparer,
    string? message)
```

Tests whether two collections contain the same elements and throws an exception if either collection contains an element not in the other collection.

**Type parameters:**

- `T`: The type of values to compare.

**Parameters:**

- `expected`: The first collection to compare. This contains the elements the test expects.
- `actual`: The second collection to compare. This is the collection produced by the code under test.
- `comparer`: The compare implementation to use when comparing elements of the collection.
- `message`: The message to include in the exception when an element was found in one of the collections but not the other. The message is shown in test results.

**Exceptions:**

- `AssertFailedException`: `expected` and `actual` nullabilities don't match, or if any element was found in one of the collections but not the other.

### AreNotEqual

```csharp
public static void AreNotEqual(ICollection? notExpected, ICollection? actual)
```

Tests whether the specified collections are unequal and throws an exception if the two collections are equal. Equality is defined as having the same elements in the same order and quantity. Whether two elements are the same is checked using `Object.Equals(Object,Object)` method. Different references to the same value are considered equal.

**Parameters:**

- `notExpected`: The first collection to compare. This is the collection the tests expects not to match `actual`.
- `actual`: The second collection to compare. This is the collection produced by the code under test.

**Exceptions:**

- `AssertFailedException`: Thrown if `notExpected` is equal to `actual`.

```csharp
public static void AreNotEqual(
    ICollection? notExpected,
    ICollection? actual,
    [NotNull] IComparer comparer)
```

Tests whether the specified collections are unequal and throws an exception if the two collections are equal. Equality is defined as having the same elements in the same order and quantity. Different references to the same value are considered equal.

**Parameters:**

- `notExpected`: The first collection to compare. This is the collection the tests expects not to match `actual`.
- `actual`: The second collection to compare. This is the collection produced by the code under test.
- `comparer`: The compare implementation to use when comparing elements of the collection.

**Exceptions:**

- `AssertFailedException`: Thrown if `notExpected` is equal to `actual`.

```csharp
public static void AreNotEqual(
    ICollection? notExpected,
    ICollection? actual,
    string? message)
```

Tests whether the specified collections are unequal and throws an exception if the two collections are equal. Equality is defined as having the same elements in the same order and quantity. Whether two elements are the same is checked using `Object.Equals(Object,Object)` method. Different references to the same value are considered equal.

**Parameters:**

- `notExpected`: The first collection to compare. This is the collection the tests expects not to match `actual`.
- `actual`: The second collection to compare. This is the collection produced by the code under test.
- `message`: The message to include in the exception when `actual` is equal to `notExpected`. The message is shown in test results.

**Exceptions:**

- `AssertFailedException`: Thrown if `notExpected` is equal to `actual`.

```csharp
public static void AreNotEqual(
    ICollection? notExpected,
    ICollection? actual,
    [NotNull] IComparer comparer,
    string? message)
```

Tests whether the specified collections are unequal and throws an exception if the two collections are equal. Equality is defined as having the same elements in the same order and quantity. Different references to the same value are considered equal.

**Parameters:**

- `notExpected`: The first collection to compare. This is the collection the tests expects not to match `actual`.
- `actual`: The second collection to compare. This is the collection produced by the code under test.
- `comparer`: The compare implementation to use when comparing elements of the collection.
- `message`: The message to include in the exception when `actual` is equal to `notExpected`. The message is shown in test results.

**Exceptions:**

- `AssertFailedException`: Thrown if `notExpected` is equal to `actual`.

### AreNotEquivalent

```csharp
public static void AreNotEquivalent(ICollection? notExpected, ICollection? actual)
```

Tests whether two collections contain the different elements and throws an exception if the two collections contain identical elements without regard to order.

**Parameters:**

- `notExpected`: The first collection to compare. This contains the elements the test expects to be different than the actual collection.
- `actual`: The second collection to compare. This is the collection produced by the code under test.

**Exceptions:**

- `AssertFailedException`: `notExpected` and `actual` nullabilities don't match, or if collections contain the same elements, including the same number of duplicate occurrences of each element.

```csharp
public static void AreNotEquivalent(
    ICollection? notExpected,
    ICollection? actual,
    string? message)
```

Tests whether two collections contain the different elements and throws an exception if the two collections contain identical elements without regard to order.

**Parameters:**

- `notExpected`: The first collection to compare. This contains the elements the test expects to be different than the actual collection.
- `actual`: The second collection to compare. This is the collection produced by the code under test.
- `message`: The message to include in the exception when `actual` contains the same elements as `notExpected`. The message is shown in test results.

**Exceptions:**

- `AssertFailedException`: `notExpected` and `actual` nullabilities don't match, or if collections contain the same elements, including the same number of duplicate occurrences of each element.

```csharp
public static void AreNotEquivalent<T>(
    IEnumerable<T?>? notExpected,
    IEnumerable<T?>? actual,
    [NotNull] IEqualityComparer<T?> comparer)
```

Tests whether two collections contain the different elements and throws an exception if the two collections contain identical elements without regard to order.

**Type parameters:**

- `T`: The type of values to compare.

**Parameters:**

- `notExpected`: The first collection to compare. This contains the elements the test expects to be different than the actual collection.
- `actual`: The second collection to compare. This is the collection produced by the code under test.
- `comparer`: The compare implementation to use when comparing elements of the collection.

**Exceptions:**

- `AssertFailedException`: `notExpected` and `actual` nullabilities don't match, or if collections contain the same elements, including the same number of duplicate occurrences of each element.

```csharp
public static void AreNotEquivalent<T>(
    IEnumerable<T?>? notExpected,
    IEnumerable<T?>? actual,
    [NotNull] IEqualityComparer<T?> comparer,
    string? message)
```

Tests whether two collections contain the different elements and throws an exception if the two collections contain identical elements without regard to order.

**Type parameters:**

- `T`: The type of values to compare.

**Parameters:**

- `notExpected`: The first collection to compare. This contains the elements the test expects to be different than the actual collection.
- `actual`: The second collection to compare. This is the collection produced by the code under test.
- `comparer`: The compare implementation to use when comparing elements of the collection.
- `message`: The message to include in the exception when `actual` contains the same elements as `notExpected`. The message is shown in test results.

**Exceptions:**

- `AssertFailedException`: `notExpected` and `actual` nullabilities don't match, or if collections contain the same elements, including the same number of duplicate occurrences of each element.

### Contains

```csharp
public static void Contains([NotNull] ICollection collection, object? element)
```

Tests whether the specified collection contains the specified element and throws an exception if the element is not in the collection.

**Parameters:**

- `collection`: The collection in which to search for the element.
- `element`: The element that is expected to be in the collection.

**Exceptions:**

- `AssertFailedException`: `collection` is null, or `collection` does not contain element `element`.

```csharp
public static void Contains(
    [NotNull] ICollection collection,
    object? element,
    string? message)
```

Tests whether the specified collection contains the specified element and throws an exception if the element is not in the collection.

**Parameters:**

- `collection`: The collection in which to search for the element.
- `element`: The element that is expected to be in the collection.
- `message`: The message to include in the exception when `element` is not in `collection`. The message is shown in test results.

**Exceptions:**

- `AssertFailedException`: `collection` is null, or `collection` does not contain element `element`.

### DoesNotContain

```csharp
public static void DoesNotContain([NotNull] ICollection collection, object? element)
```

Tests whether the specified collection does not contain the specified element and throws an exception if the element is in the collection.

**Parameters:**

- `collection`: The collection in which to search for the element.
- `element`: The element that is expected not to be in the collection.

**Exceptions:**

- `AssertFailedException`: `collection` is null, or `collection` contains element `element`.

```csharp
public static void DoesNotContain(
    [NotNull] ICollection collection,
    object? element,
    string? message)
```

Tests whether the specified collection does not contain the specified element and throws an exception if the element is in the collection.

**Parameters:**

- `collection`: The collection in which to search for the element.
- `element`: The element that is expected not to be in the collection.
- `message`: The message to include in the exception when `element` is in `collection`. The message is shown in test results.

**Exceptions:**

- `AssertFailedException`: `collection` is null, or `collection` contains element `element`.

### Equals

```csharp
[Obsolete("CollectionAssert.Equals should not be used for Assertions. Please use CollectionAssert.AreEqual & overloads instead.", true, DiagnosticId = "MSTEST0104", UrlFormat = "https://aka.ms/mstest/diagnostics#{0}")]
[DoesNotReturn]
public static bool Equals(object? objA, object? objB)
```

Static equals overloads are used for comparing instances of two types for equality. This method should **not** be used for comparison of two instances for equality. Please use CollectionAssert.AreEqual and associated overloads in your unit tests.

**Parameters:**

- `objA`: Object A.
- `objB`: Object B.

**Returns:** Never returns.

### IsNotSubsetOf

```csharp
public static void IsNotSubsetOf([NotNull] ICollection subset, [NotNull] ICollection superset)
```

Tests whether one collection is not a subset of another collection and throws an exception if all elements in the subset are also in the superset.

**Parameters:**

- `subset`: The collection expected not to be a subset of `superset`.
- `superset`: The collection expected not to be a superset of `subset`.

**Exceptions:**

- `AssertFailedException`: `subset` is null, or `superset` is null, or all elements of `subset` are contained in `superset`.

```csharp
public static void IsNotSubsetOf(
    [NotNull] ICollection subset,
    [NotNull] ICollection superset,
    string? message)
```

Tests whether one collection is not a subset of another collection and throws an exception if all elements in the subset are also in the superset.

**Parameters:**

- `subset`: The collection expected not to be a subset of `superset`.
- `superset`: The collection expected not to be a superset of `subset`.
- `message`: The message to include in the exception when every element in `subset` is also found in `superset`. The message is shown in test results.

**Exceptions:**

- `AssertFailedException`: `subset` is null, or `superset` is null, or all elements of `subset` are contained in `superset`.

### IsSubsetOf

```csharp
public static void IsSubsetOf([NotNull] ICollection subset, [NotNull] ICollection superset)
```

Tests whether one collection is a subset of another collection and throws an exception if any element in the subset is not also in the superset.

**Parameters:**

- `subset`: The collection expected to be a subset of `superset`.
- `superset`: The collection expected to be a superset of `subset`.

**Exceptions:**

- `AssertFailedException`: `subset` is null, or `superset` is null, or `subset` contains at least one element not contained in `superset`.

```csharp
public static void IsSubsetOf(
    [NotNull] ICollection subset,
    [NotNull] ICollection superset,
    string? message)
```

Tests whether one collection is a subset of another collection and throws an exception if any element in the subset is not also in the superset.

**Parameters:**

- `subset`: The collection expected to be a subset of `superset`.
- `superset`: The collection expected to be a superset of `subset`.
- `message`: The message to include in the exception when an element in `subset` is not found in `superset`. The message is shown in test results.

**Exceptions:**

- `AssertFailedException`: `subset` is null, or `superset` is null, or `subset` contains at least one element not contained in `superset`.

### ReferenceEquals

```csharp
[Obsolete("CollectionAssert.ReferenceEquals should not be used for Assertions. Please use CollectionAssert methods or Assert.AreSame & overloads instead.", true, DiagnosticId = "MSTEST0105", UrlFormat = "https://aka.ms/mstest/diagnostics#{0}")]
[DoesNotReturn]
public static bool ReferenceEquals(object? objA, object? objB)
```

Static ReferenceEquals overloads are used for comparing instances of two types for reference equality. This method should **not** be used for comparison of two instances for reference equality. Please use CollectionAssert methods or Assert.AreSame and associated overloads in your unit tests.

**Parameters:**

- `objA`: Object A.
- `objB`: Object B.

**Returns:** Never returns.
