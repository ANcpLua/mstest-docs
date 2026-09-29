# SequenceOrder enum

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

Specifies whether sequence elements must appear in the same order, or in any order, when comparing collections with `Assert.AreSequenceEqual(IEnumerable<T0>,IEnumerable<T0>,SequenceOrder,String,String,String)`.

```csharp
public enum SequenceOrder
```

## Fields

| Name | Value | Description |
| --- | --- | --- |
| `InOrder` | `0` | Elements must appear in the same order in both sequences (LINQ `Enumerable.SequenceEqual(IEnumerable<T0>,IEnumerable<T0>)` semantics). |
| `InAnyOrder` | `1` | Elements may appear in any order, but each element must appear the same number of times in both sequences (multiset equality). |
