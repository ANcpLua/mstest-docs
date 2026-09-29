# OperatingSystems enum

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

An enum that is used with `OSConditionAttribute` to control which operating systems a test method or test class supports or doesn't support.

```csharp
[Flags]
public enum OperatingSystems
```

## Fields

| Name | Value | Description |
| --- | --- | --- |
| `Linux` | `1` | Represents the Linux operating system. |
| `OSX` | `2` | Representing the MacOS operating system. |
| `Windows` | `4` | Represents the Windows operating system. |
| `FreeBSD` | `8` | Represents the FreeBSD operating system. |
