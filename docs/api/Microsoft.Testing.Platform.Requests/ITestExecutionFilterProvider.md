# ITestExecutionFilterProvider interface

- Namespace: `Microsoft.Testing.Platform.Requests`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

Provides an additional constraint for a test execution request.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public interface ITestExecutionFilterProvider : IExtension
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Methods

### GetFilterAsync

```csharp
Task<ITestExecutionFilter?> GetFilterAsync(TestExecutionFilterContext context, CancellationToken cancellationToken)
```

Gets the filter constraint for the current request.

**Parameters:**

- `context`: The test execution filter context.
- `cancellationToken`: The cancellation token for the request.

**Returns:** A task whose result is the filter constraint, or `null` when the provider does not constrain the current request.

#### Remarks

Provider constraints are not currently applied to JSON-RPC server requests. Return `null` when `TestExecutionFilterContext.Origin` is `TestExecutionRequestOrigin.Server`.
