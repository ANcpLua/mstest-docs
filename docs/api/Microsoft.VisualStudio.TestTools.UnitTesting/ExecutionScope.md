# ExecutionScope enum

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

Parallel execution mode.

```csharp
public enum ExecutionScope
```

## Fields

| Name | Value | Description |
| --- | --- | --- |
| `ClassLevel` | `0` | Each thread of execution will be handed a TestClass worth of tests to execute. Within the TestClass, the test methods will execute serially. |
| `MethodLevel` | `1` | Each thread of execution will be handed TestMethods to execute. |
