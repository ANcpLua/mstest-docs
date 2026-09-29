# ITestFilter interface

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

Implemented by a user-supplied test filter that decides, on a per-test basis, whether the test should run, be silently dropped, or be reported as skipped.

```csharp
[Experimental("MSTESTEXP", UrlFormat = "https://aka.ms/mstest/diagnostics#{0}")]
public interface ITestFilter
```

## Remarks

Implementations are registered via `TestFilterProviderAttribute` at the assembly level. The MSTest adapter materializes the filter lazily on the first test invocation for that assembly using the public parameterless constructor; the same instance is then reused for every test in the assembly.

Implementations should be allocation-free and thread-safe; `ITestFilter.Filter(TestFilterContext)` may be invoked concurrently for tests in different classes.

**Ordering with built-in filtering:** `ITestFilter` is composed with — not a replacement for — the adapter's default filtering. By contrast, `[Ignore]` is evaluated *after* `ITestFilter` (it requires loading the declaring type, which `ITestFilter` is specifically designed to avoid). Returning `TestFilterResult.Run` does not override a later `[Ignore]`; an ignored test is still ignored.

This API is experimental. It may change, break, or be removed at any time without notice.

## Methods

### Filter

```csharp
TestFilterResult Filter(TestFilterContext context)
```

Decides whether the test described by `context` should run.

**Parameters:**

- `context`: Metadata describing the test under consideration.

**Returns:** `TestFilterResult.Run` to let the test execute normally, `TestFilterResult.Drop` to silently drop the test (no result emitted), or `TestFilterResult.Skip(String)` to report the test as Skipped with a reason.

#### Remarks

If this method throws, the test is reported as Error with diagnostic `UTA078`; the exception is never silently swallowed. Implementations that want to opt the test in to running on failure should catch their own exceptions and return `TestFilterResult.Run`.
