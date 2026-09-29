# MSTEST0059: Do not use both Parallelize and DoNotParallelize attributes

| Property                            | Value                                              |
|-------------------------------------|----------------------------------------------------|
| **Rule ID**                         | MSTEST0059                                         |
| **Title**                           | Do not use both Parallelize and DoNotParallelize attributes |
| **Category**                        | Usage                                              |
| **Fix is breaking or non-breaking** | Non-breaking                                       |
| **Enabled by default**              | Yes                                                |
| **Default severity**                | Warning                                            |
| **Introduced in version**           | 4.1.0                                              |
| **Is there a code fix**             | No                                                 |

## Cause

An assembly contains both [`ParallelizeAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/ParallelizeAttribute.md) and [`DoNotParallelizeAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/DoNotParallelizeAttribute.md) attributes.

## Rule description

The [`ParallelizeAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/ParallelizeAttribute.md) and [`DoNotParallelizeAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/DoNotParallelizeAttribute.md) attributes are mutually exclusive at the assembly level. When both attributes are applied to the same assembly, tests run sequentially. This conflicting configuration indicates unclear intent and should be resolved by choosing one parallelization strategy for your test assembly.

```csharp
using Microsoft.VisualStudio.TestTools.UnitTesting;

[assembly: Parallelize(Workers = 0, Scope = ExecutionScope.MethodLevel)] // Violation
[assembly: DoNotParallelize]
```

## How to fix violations

Remove one of the conflicting attributes based on your intended parallelization strategy.

If you want parallel execution:

```csharp
using Microsoft.VisualStudio.TestTools.UnitTesting;

[assembly: Parallelize(Workers = 0, Scope = ExecutionScope.MethodLevel)]
```

If you want sequential execution:

```csharp
using Microsoft.VisualStudio.TestTools.UnitTesting;

[assembly: DoNotParallelize]
```

If you want to enable parallelization at the assembly level but disable it for specific classes or methods, apply `Parallelize` at the assembly level and `DoNotParallelize` at the class or method level:

```csharp
using Microsoft.VisualStudio.TestTools.UnitTesting;

[assembly: Parallelize(Workers = 0, Scope = ExecutionScope.MethodLevel)]

[DoNotParallelize]
[TestClass]
public class SequentialTests
{
    [TestMethod]
    public void Test1() { }
}

[TestClass]
public class ParallelTests
{
    [TestMethod]
    public void Test2() { }
    
    [DoNotParallelize]
    [TestMethod]
    public void Test3() { }
}
```

## When to suppress warnings

Do not suppress warnings from this rule. Having both attributes creates ambiguous test configuration that should be resolved.

## Suppress a warning

If you just want to suppress a single violation, add preprocessor directives to your source file to disable and then re-enable the rule.

```csharp
#pragma warning disable MSTEST0059
// The code that's violating the rule is on this line.
#pragma warning restore MSTEST0059
```

To disable the rule for a file, folder, or project, set its severity to `none` in the [configuration file](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/configuration-files).

```ini
[*.{cs,vb}]
dotnet_diagnostic.MSTEST0059.severity = none
```

For more information, see [How to suppress code analysis warnings](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/suppress-warnings).
