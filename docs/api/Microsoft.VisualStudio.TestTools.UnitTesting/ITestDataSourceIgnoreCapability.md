# ITestDataSourceIgnoreCapability interface

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

Specifies the capability of a test data source to be ignored and define the ignore reason.

```csharp
public interface ITestDataSourceIgnoreCapability
```

## Properties

### IgnoreMessage

```csharp
string? IgnoreMessage { get; set; }
```

Gets or sets a reason to ignore the test data source. Setting the property to non-null value will ignore the test data source.
