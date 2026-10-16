# MSTEST0086: Remove redundant test method attribute

| Property | Value |
|---|---|
| **Rule ID** | MSTEST0086 |
| **Title** | Remove redundant test method attribute |
| **Category** | Usage |
| **Fix is breaking or non-breaking** | Non-breaking |
| **Enabled by default** | Yes |
| **Default severity** | Info |
| **Introduced in version** | 4.5.0 |
| **Is there a code fix** | Yes, for C# only |

## Cause

A test method declares an MSTest attribute whose effective behavior is already supplied by its containing test class or a base test class.

## Rule description

Duplicate attributes make the effective test policy harder to understand and maintain. The rule reports method-level conditions, retry settings, isolation settings, metadata, deployment items, or dependencies only when the class-level configuration already provides equivalent or more restrictive behavior.

The rule covers `OSCondition`, `ArchitectureCondition`, `CICondition`, `DoNotParallelize`, `ResourceLock`, `Retry`, `Ignore`, `TestCategory`, `TestProperty`, `DeploymentItem`, and `DependsOn`.

For `OSCondition`, `ArchitectureCondition`, `CICondition`, `Retry`, `Ignore`, and `DependsOn`, the rule reports redundant attributes only on methods declared in sealed test classes. These class-level attributes aren't inherited, so removing a method-level attribute from an unsealed class could change how an inherited test runs in a derived class.

For `DoNotParallelize`, `ResourceLock`, `TestCategory`, `TestProperty`, and `DeploymentItem`, the rule also considers attributes on base classes. The rule doesn't report `MemberCondition`, `ExecutableCondition`, or custom attributes.

```csharp
[TestClass, DoNotParallelize]
public class Tests
{
    [TestMethod, DoNotParallelize] // Violation
    public void Test() { }
}
```

## How to fix violations

Remove the redundant method-level attribute. Keep an attribute on the method when it changes or narrows the class-level behavior.

```csharp
[TestClass, DoNotParallelize]
public class Tests
{
    [TestMethod] public void Test() { }
}
```

A C# code fix removes the redundant attribute. Visual Basic reports the diagnostic but doesn't provide an automatic fix.

## When to suppress warnings

Suppress the rule when the duplicate attribute intentionally documents a local policy and that documentation value outweighs the maintenance cost.

## Suppress a warning

```csharp
#pragma warning disable MSTEST0086
// The code that's violating the rule is on this line.
#pragma warning restore MSTEST0086
```

To disable the rule for a file, folder, or project, set its severity to `none` in the [configuration file](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/configuration-files).

```ini
[*.{cs,vb}]
dotnet_diagnostic.MSTEST0086.severity = none
```

For more information, see [How to suppress code analysis warnings](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/suppress-warnings).

## See also

- [Write tests with MSTest](../writing-tests/overview.md)
- [Test execution and control](../writing-tests/controlling-execution.md)
