# MSTEST0047: Unused TestContext parameter suppressor

| Property                            | Value                                                     |
|-------------------------------------|-----------------------------------------------------------|
| **Rule ID**                         | MSTEST0047                                                |
| **Title**                           | Suppress IDE0060 for the TestContext parameter            |
| **Category**                        | Suppressor                                                |
| **Introduced in version**           | 3.10.0                                                    |

## Suppressor description

Suppress the [IDE0060: Remove unused parameter](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/style-rules/ide0060) diagnostic for the [`TestContext`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md) parameter of fixture methods.

MSTest lets you receive the `TestContext` as a parameter of fixture methods that are marked with [`AssemblyInitializeAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/AssemblyInitializeAttribute.md), [`ClassInitializeAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/ClassInitializeAttribute.md), [`GlobalTestInitializeAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/GlobalTestInitializeAttribute.md), or [`GlobalTestCleanupAttribute`](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/GlobalTestCleanupAttribute.md). Because the parameter is required by MSTest even when your method body doesn't use it, IDE0060 would otherwise incorrectly flag it as unused.

## When to disable suppressor

.NET suppressors cannot be disabled.
