# StringAssert class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

The string assert.

```csharp
public sealed class StringAssert
```

## Properties

### That

```csharp
public static StringAssert That { get; }
```

Gets the singleton instance of the StringAssert functionality.

#### Remarks

Users can use this to plug-in custom assertions through C# extension methods. For instance, the signature of a custom assertion provider could be `public static void ContainsWords(this StringAssert customAssert, string value, ICollection substrings)` and the call-site would be `StringAssert.That.ContainsWords(value, substrings);`.

For new custom assertions, prefer extending `Assert.That` instead, because `StringAssert` is likely to be deprecated in a future release. For more information, see [Extension hooks on StringAssert and CollectionAssert](https://learn.microsoft.com/dotnet/core/testing/unit-testing-mstest-writing-tests-assertions#extension-hooks-on-stringassert-and-collectionassert).

#### Example

The following example defines a custom `ContainsWords` assertion as an extension method on `StringAssert` and invokes it through `StringAssert.That`:

```csharp
using System.Collections.Generic;
using Microsoft.VisualStudio.TestTools.UnitTesting;
            
public static class CustomStringAssertExtensions
{
    public static void ContainsWords(this StringAssert stringAssert, string value, IEnumerable<string> words)
    {
        foreach (string word in words)
        {
            if (value == null || !value.Contains(word))
            {
                throw new AssertFailedException($"StringAssert.That.ContainsWords failed. Word <{word}> not found in <{value}>.");
            }
        }
    }
}
            
[TestClass]
public class MessageTests
{
    [TestMethod]
    public void Greeting_ContainsExpectedWords()
    {
        StringAssert.That.ContainsWords("Hello, world!", new[] { "Hello", "world" });
    }
}
```

## Methods

### Contains

```csharp
public static void Contains([NotNull] string value, [NotNull] string substring)
```

Tests whether the specified string contains the specified substring and throws an exception if the substring does not occur within the test string.

**Parameters:**

- `value`: The string that is expected to contain `substring`.
- `substring`: The string expected to occur within `value`.

**Exceptions:**

- `AssertFailedException`: `value` is null, or `substring` is null, or `value` does not contain `substring`.

```csharp
public static void Contains(
    [NotNull] string value,
    [NotNull] string substring,
    StringComparison comparisonType)
```

Tests whether the specified string contains the specified substring and throws an exception if the substring does not occur within the test string.

**Parameters:**

- `value`: The string that is expected to contain `substring`.
- `substring`: The string expected to occur within `value`.
- `comparisonType`: The comparison method to compare strings `comparisonType`.

**Exceptions:**

- `AssertFailedException`: `value` is null, or `substring` is null, or `value` does not contain `substring`.

```csharp
public static void Contains(
    [NotNull] string value,
    [NotNull] string substring,
    string? message)
```

Tests whether the specified string contains the specified substring and throws an exception if the substring does not occur within the test string.

**Parameters:**

- `value`: The string that is expected to contain `substring`.
- `substring`: The string expected to occur within `value`.
- `message`: The message to include in the exception when `substring` is not in `value`. The message is shown in test results.

**Exceptions:**

- `AssertFailedException`: `value` is null, or `substring` is null, or `value` does not contain `substring`.

```csharp
public static void Contains(
    [NotNull] string value,
    [NotNull] string substring,
    StringComparison comparisonType,
    string? message)
```

Tests whether the specified string contains the specified substring and throws an exception if the substring does not occur within the test string.

**Parameters:**

- `value`: The string that is expected to contain `substring`.
- `substring`: The string expected to occur within `value`.
- `comparisonType`: The comparison method to compare strings `comparisonType`.
- `message`: The message to include in the exception when `substring` is not in `value`. The message is shown in test results.

**Exceptions:**

- `AssertFailedException`: `value` is null, or `substring` is null, or `value` does not contain `substring`.

### DoesNotMatch

```csharp
public static void DoesNotMatch([NotNull] string value, [NotNull] Regex pattern)
```

Tests whether the specified string does not match a regular expression and throws an exception if the string matches the expression.

**Parameters:**

- `value`: The string that is expected not to match `pattern`.
- `pattern`: The regular expression that `value` is expected to not match.

**Exceptions:**

- `AssertFailedException`: `value` is null, or `pattern` is null, or `value` matches `pattern`.

```csharp
public static void DoesNotMatch(
    [NotNull] string value,
    [NotNull] Regex pattern,
    string? message)
```

Tests whether the specified string does not match a regular expression and throws an exception if the string matches the expression.

**Parameters:**

- `value`: The string that is expected not to match `pattern`.
- `pattern`: The regular expression that `value` is expected to not match.
- `message`: The message to include in the exception when `value` matches `pattern`. The message is shown in test results.

**Exceptions:**

- `AssertFailedException`: `value` is null, or `pattern` is null, or `value` matches `pattern`.

### EndsWith

```csharp
public static void EndsWith([NotNull] string value, [NotNull] string substring)
```

Tests whether the specified string ends with the specified substring and throws an exception if the test string does not end with the substring.

**Parameters:**

- `value`: The string that is expected to end with `substring`.
- `substring`: The string expected to be a suffix of `value`.

**Exceptions:**

- `AssertFailedException`: `value` is null, or `substring` is null, or `value` does not end with `substring`.

```csharp
public static void EndsWith(
    [NotNull] string value,
    [NotNull] string substring,
    StringComparison comparisonType)
```

Tests whether the specified string ends with the specified substring and throws an exception if the test string does not end with the substring.

**Parameters:**

- `value`: The string that is expected to end with `substring`.
- `substring`: The string expected to be a suffix of `value`.
- `comparisonType`: The comparison method to compare strings `comparisonType`.

**Exceptions:**

- `AssertFailedException`: `value` is null, or `substring` is null, or `value` does not end with `substring`.

```csharp
public static void EndsWith(
    [NotNull] string value,
    [NotNull] string substring,
    string? message)
```

Tests whether the specified string ends with the specified substring and throws an exception if the test string does not end with the substring.

**Parameters:**

- `value`: The string that is expected to end with `substring`.
- `substring`: The string expected to be a suffix of `value`.
- `message`: The message to include in the exception when `value` does not end with `substring`. The message is shown in test results.

**Exceptions:**

- `AssertFailedException`: `value` is null, or `substring` is null, or `value` does not end with `substring`.

```csharp
public static void EndsWith(
    [NotNull] string value,
    [NotNull] string substring,
    StringComparison comparisonType,
    string? message)
```

Tests whether the specified string ends with the specified substring and throws an exception if the test string does not end with the substring.

**Parameters:**

- `value`: The string that is expected to end with `substring`.
- `substring`: The string expected to be a suffix of `value`.
- `comparisonType`: The comparison method to compare strings `comparisonType`.
- `message`: The message to include in the exception when `value` does not end with `substring`. The message is shown in test results.

**Exceptions:**

- `AssertFailedException`: `value` is null, or `substring` is null, or `value` does not end with `substring`.

### Equals

```csharp
[Obsolete("StringAssert.Equals should not be used for Assertions. Please use StringAssert methods or Assert.AreEqual & overloads instead.", true, DiagnosticId = "MSTEST0102", UrlFormat = "https://aka.ms/mstest/diagnostics#{0}")]
[DoesNotReturn]
public static bool Equals(object? objA, object? objB)
```

Static equals overloads are used for comparing instances of two types for equality. This method should **not** be used for comparison of two instances for equality. Please use StringAssert methods or Assert.AreEqual and associated overloads in your unit tests.

**Parameters:**

- `objA`: Object A.
- `objB`: Object B.

**Returns:** Never returns.

### Matches

```csharp
public static void Matches([NotNull] string value, [NotNull] Regex pattern)
```

Tests whether the specified string matches a regular expression and throws an exception if the string does not match the expression.

**Parameters:**

- `value`: The string that is expected to match `pattern`.
- `pattern`: The regular expression that `value` is expected to match.

**Exceptions:**

- `AssertFailedException`: `value` is null, or `pattern` is null, or `value` does not match `pattern`.

```csharp
public static void Matches(
    [NotNull] string value,
    [NotNull] Regex pattern,
    string? message)
```

Tests whether the specified string matches a regular expression and throws an exception if the string does not match the expression.

**Parameters:**

- `value`: The string that is expected to match `pattern`.
- `pattern`: The regular expression that `value` is expected to match.
- `message`: The message to include in the exception when `value` does not match `pattern`. The message is shown in test results.

**Exceptions:**

- `AssertFailedException`: `value` is null, or `pattern` is null, or `value` does not match `pattern`.

### ReferenceEquals

```csharp
[Obsolete("StringAssert.ReferenceEquals should not be used for Assertions. Please use StringAssert methods or Assert.AreSame & overloads instead.", true, DiagnosticId = "MSTEST0103", UrlFormat = "https://aka.ms/mstest/diagnostics#{0}")]
[DoesNotReturn]
public static bool ReferenceEquals(object? objA, object? objB)
```

Static ReferenceEquals overloads are used for comparing instances of two types for reference equality. This method should **not** be used for comparison of two instances for reference equality. Please use StringAssert methods or Assert.AreSame and associated overloads in your unit tests.

**Parameters:**

- `objA`: Object A.
- `objB`: Object B.

**Returns:** Never returns.

### StartsWith

```csharp
public static void StartsWith([NotNull] string value, [NotNull] string substring)
```

Tests whether the specified string begins with the specified substring and throws an exception if the test string does not start with the substring.

**Parameters:**

- `value`: The string that is expected to begin with `substring`.
- `substring`: The string expected to be a prefix of `value`.

**Exceptions:**

- `AssertFailedException`: `value` is null, or `substring` is null, or `value` does not start with `substring`.

```csharp
public static void StartsWith(
    [NotNull] string value,
    [NotNull] string substring,
    StringComparison comparisonType)
```

Tests whether the specified string begins with the specified substring and throws an exception if the test string does not start with the substring.

**Parameters:**

- `value`: The string that is expected to begin with `substring`.
- `substring`: The string expected to be a prefix of `value`.
- `comparisonType`: The comparison method to compare strings `comparisonType`.

**Exceptions:**

- `AssertFailedException`: `value` is null, or `substring` is null, or `value` does not start with `substring`.

```csharp
public static void StartsWith(
    [NotNull] string value,
    [NotNull] string substring,
    string? message)
```

Tests whether the specified string begins with the specified substring and throws an exception if the test string does not start with the substring.

**Parameters:**

- `value`: The string that is expected to begin with `substring`.
- `substring`: The string expected to be a prefix of `value`.
- `message`: The message to include in the exception when `value` does not begin with `substring`. The message is shown in test results.

**Exceptions:**

- `AssertFailedException`: `value` is null, or `substring` is null, or `value` does not start with `substring`.

```csharp
public static void StartsWith(
    [NotNull] string value,
    [NotNull] string substring,
    StringComparison comparisonType,
    string? message)
```

Tests whether the specified string begins with the specified substring and throws an exception if the test string does not start with the substring.

**Parameters:**

- `value`: The string that is expected to begin with `substring`.
- `substring`: The string expected to be a prefix of `value`.
- `comparisonType`: The comparison method to compare strings `comparisonType`.
- `message`: The message to include in the exception when `value` does not begin with `substring`. The message is shown in test results.

**Exceptions:**

- `AssertFailedException`: `value` is null, or `substring` is null, or `value` does not start with `substring`.
