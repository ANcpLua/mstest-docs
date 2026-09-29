# MSTEST0068: Use Assert instead of CollectionAssert

| Property                            | Value                                              |
|-------------------------------------|----------------------------------------------------|
| **Rule ID**                         | MSTEST0068                                         |
| **Title**                           | Use `Assert` instead of `CollectionAssert`         |
| **Category**                        | Usage                                              |
| **Fix is breaking or non-breaking** | Non-breaking                                       |
| **Enabled by default**              | Yes                                                |
| **Default severity**                | Info                                               |
| **Introduced in version**           | 4.3.0                                              |
| **Is there a code fix**             | Yes                                                |

> [!NOTE]
> This rule is available starting with MSTest 4.3.

## Cause

A test method uses [`CollectionAssert`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/CollectionAssert.md) methods instead of equivalent [`Assert`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/Assert.md) methods.

## Rule description

Most [`CollectionAssert`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/CollectionAssert.md) methods have equivalent counterparts in [`Assert`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/Assert.md) that provide the same functionality. Prefer the [`Assert`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/Assert.md) methods for consistency, better readability, improved discoverability, and alignment with behavior across all test frameworks.

The following [`CollectionAssert`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/CollectionAssert.md) methods have equivalent [`Assert`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/Assert.md) methods:

- `CollectionAssert.AreEqual(a, b)` → `Assert.AreSequenceEqual(a, b)`
- `CollectionAssert.AreNotEqual(a, b)` → `Assert.AreNotSequenceEqual(a, b)`
- `CollectionAssert.AreEquivalent(a, b)` → `Assert.AreSequenceEqual(a, b, SequenceOrder.InAnyOrder)`
- `CollectionAssert.AreNotEquivalent(a, b)` → `Assert.AreNotSequenceEqual(a, b, SequenceOrder.InAnyOrder)`
- `CollectionAssert.AllItemsAreNotNull(a)` → `Assert.AreAllNotNull(a)`
- `CollectionAssert.AllItemsAreUnique(a)` → `Assert.AreAllDistinct(a)`
- `CollectionAssert.AllItemsAreInstancesOfType(collection, typeof(T))` → `Assert.AreAllOfType<T>(collection)`
- `CollectionAssert.Contains(collection, value)` → `Assert.Contains(value, collection)`
- `CollectionAssert.DoesNotContain(collection, value)` → `Assert.DoesNotContain(value, collection)`

> [!WARNING]
> When migrating from [`CollectionAssert`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/CollectionAssert.md) to [`Assert`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/Assert.md), be careful about the change in parameter order for `Contains`, `DoesNotContain`, and `AllItemsAreInstancesOfType`. In [`Assert`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/Assert.md), the expected value is always the first parameter.

Overloads of `AreEqual`/`AreNotEqual` that take an [`IComparer`](https://learn.microsoft.com/en-us/dotnet/api/system.collections.icomparer) are skipped because `Assert.AreSequenceEqual` expects an [`IEqualityComparer<T>`](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.iequalitycomparer-1) (different semantics). Overloads of `AreEquivalent`/`AreNotEquivalent` that take an [`IEqualityComparer<T>`](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.iequalitycomparer-1) are also skipped. `IsSubsetOf`/`IsNotSubsetOf` have no direct [`Assert`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/Assert.md) equivalent today and are not handled.

## How to fix violations

Use the provided code fixer to automatically replace [`CollectionAssert`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/CollectionAssert.md) method calls with their equivalent [`Assert`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/Assert.md) methods. You can also manually replace the method calls if needed.

## When to suppress warnings

Don't suppress warnings from this rule. The [`Assert`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/Assert.md) methods provide the same functionality with better consistency.

## Suppress a warning

If you just want to suppress a single violation, add preprocessor directives to your source file to disable and then re-enable the rule.

```csharp
#pragma warning disable MSTEST0068
// The code that's violating the rule is on this line.
#pragma warning restore MSTEST0068
```

To disable the rule for a file, folder, or project, set its severity to `none` in the [configuration file](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/configuration-files).

```ini
[*.{cs,vb}]
dotnet_diagnostic.MSTEST0068.severity = none
```

For more information, see [How to suppress code analysis warnings](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/suppress-warnings).
