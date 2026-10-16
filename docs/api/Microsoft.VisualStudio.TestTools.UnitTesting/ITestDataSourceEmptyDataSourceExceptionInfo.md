# ITestDataSourceEmptyDataSourceExceptionInfo interface

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

Optional capability for a custom `ITestDataSource` to provide richer information when the data source returns no rows. When a data source implements this interface, MSTest uses the returned member and type names to build a more actionable exception message instead of the generic `GetData returned empty collection` message.

```csharp
[Experimental("MSTESTEXP", UrlFormat = "https://aka.ms/mstest/diagnostics#{0}")]
public interface ITestDataSourceEmptyDataSourceExceptionInfo
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Methods

### GetPropertyOrMethodContainerTypeNameForEmptyDataSourceException

```csharp
string? GetPropertyOrMethodContainerTypeNameForEmptyDataSourceException(MethodInfo testMethodInfo)
```

Returns the type name on which the method/property accessed by this data source exists.

**Parameters:**

- `testMethodInfo`: The test method that the data source is attached to.

**Returns:** The name of the type that declares the member that produced the (empty) data, or `null` if unknown.

### GetPropertyOrMethodNameForEmptyDataSourceException

```csharp
string? GetPropertyOrMethodNameForEmptyDataSourceException()
```

Returns the method/property name accessed by this data source. For example, for `DynamicDataAttribute`, that will be the attribute argument.

**Returns:** The name of the member that produced the (empty) data, or `null` if unknown.
