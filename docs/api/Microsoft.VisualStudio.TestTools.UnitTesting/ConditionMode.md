# ConditionMode enum

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

An enumeration used with `ConditionBaseAttribute` to control whether the condition is reversed.

```csharp
public enum ConditionMode
```

## Fields

| Name | Value | Description |
| --- | --- | --- |
| `Include` | `0` | Runs only when the condition is met (the default). |
| `Exclude` | `1` | Ignores the test when the condition is met (i.e, reverse the condition). |
