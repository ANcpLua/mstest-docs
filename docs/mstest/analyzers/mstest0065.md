# MSTEST0065: Avoid `Assert.AreEqual` on collection types

| Property                            | Value                                              |
|-------------------------------------|----------------------------------------------------|
| **Rule ID**                         | MSTEST0065                                         |
| **Title**                           | Avoid `Assert.AreEqual` on collection types        |
| **Category**                        | Usage                                              |
| **Fix is breaking or non-breaking** | Non-breaking                                       |
| **Enabled by default**              | Yes                                                |
| **Default severity**                | Warning                                            |
| **Introduced in version**           | 4.3.0                                              |
| **Is there a code fix**             | No                                                 |

> [!NOTE]
> This rule is available starting with MSTest 4.3.
>
> Starting with MSTest 4.3.3, the rule doesn't report collection types that declare their own equality behavior.

## Cause

A call to [`Assert.AreEqual`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/Assert.md) or [`Assert.AreNotEqual`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/Assert.md) is made on a value whose static type implements [`IEnumerable<T>`](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.ienumerable-1) (other than [`String`](https://learn.microsoft.com/en-us/dotnet/api/system.string)).

## Rule description

[`AreEqual`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/Assert.md) and [`AreNotEqual`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/Assert.md) use [`EqualityComparer<T>.Default`](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.equalitycomparer-1.default). For most collection types — for example arrays, [`List<T>`](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1), or any user-defined type implementing [`IEnumerable<T>`](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.ienumerable-1) — this falls back to reference equality (or to whatever equality the type defines for itself), and not to element-wise comparison. As a result, the assertion almost never asserts what the test author intended.

```csharp
[TestClass]
public class TestClass
{
    [TestMethod]
    public void Test()
    {
        var expected = new[] { 1, 2, 3 };
        var actual = new[] { 1, 2, 3 };

        // Violation: this compares references, not contents, and fails.
        Assert.AreEqual(expected, actual);
    }
}
```

## How to fix violations

Choose the assertion that matches your intent:

- Use `Assert.AreSequenceEqual` for ordered element-wise comparison.
- Use `Assert.AreSequenceEqual(expected, actual, SequenceOrder.InAnyOrder)` for unordered element-wise comparison.
- Use `Assert.AreEquivalent` for deep structural comparison.

```csharp
[TestClass]
public class TestClass
{
    [TestMethod]
    public void Test()
    {
        var expected = new[] { 1, 2, 3 };
        var actual = new[] { 1, 2, 3 };

        Assert.AreSequenceEqual(expected, actual);
    }
}
```

## When to suppress warnings

Suppress this warning only if the type defines its own `Equals`/`GetHashCode` to compare contents and you intentionally rely on that.

## Suppress a warning

If you just want to suppress a single violation, add preprocessor directives to your source file to disable and then re-enable the rule.

```csharp
#pragma warning disable MSTEST0065
// The code that's violating the rule is on this line.
#pragma warning restore MSTEST0065
```

To disable the rule for a file, folder, or project, set its severity to `none` in the [configuration file](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/configuration-files).

```ini
[*.{cs,vb}]
dotnet_diagnostic.MSTEST0065.severity = none
```

For more information, see [How to suppress code analysis warnings](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/suppress-warnings).
