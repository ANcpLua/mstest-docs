# TestApplicationBuilderExtensions class

- Namespace: `Microsoft.Testing.Platform.Helpers`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

A collection of extension methods for `ITestApplicationBuilder`.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public static class TestApplicationBuilderExtensions
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Methods

### AddMaximumFailedTestsService

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public static void AddMaximumFailedTestsService(this ITestApplicationBuilder builder, IExtension extension)
```

Registers the command-line options provider for '--maximum-failed-tests'.

**Parameters:**

- `builder`: The test application builder.
- `extension`: The extension owner of the maximum failed tests service.

#### Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

### AddTestExecutionFilterProvider

```csharp
public static void AddTestExecutionFilterProvider(
    this ITestApplicationBuilder builder,
    Func<IServiceProvider, ITestExecutionFilterProvider> providerFactory)
```

Registers a provider that can contribute an additional test execution filter constraint.

**Parameters:**

- `builder`: The test application builder.
- `providerFactory`: The factory method for creating the provider.

### AddTreeNodeFilterService

```csharp
public static void AddTreeNodeFilterService(this ITestApplicationBuilder testApplicationBuilder, IExtension extension)
```

Registers the command-line options provider for '--treenode-filter'.

**Parameters:**

- `testApplicationBuilder`: The test application builder.
- `extension`: The extension owner of the tree node filter service.
