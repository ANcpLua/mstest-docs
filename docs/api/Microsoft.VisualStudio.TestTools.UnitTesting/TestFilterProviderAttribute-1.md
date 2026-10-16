# TestFilterProviderAttribute<TFilter> class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

Strongly typed variant of `TestFilterProviderAttribute` that registers `TFilter` as the `ITestFilter` implementation the MSTest adapter invokes for every test it is about to run.

```csharp
[AttributeUsage(AttributeTargets.Assembly, AllowMultiple = false, Inherited = false)]
[Experimental("MSTESTEXP", UrlFormat = "https://aka.ms/mstest/diagnostics#{0}")]
public sealed class TestFilterProviderAttribute<TFilter> : Attribute
```

**Type parameters:**

- `TFilter`: The `ITestFilter` implementation to instantiate and invoke for every test in the consuming test assembly.

## Remarks

This is the type-safe form of `[assembly: TestFilterProvider(typeof(MyFilter))]`. The generic constraints make the compiler enforce, at build time, what the non-generic attribute can only validate at run time: `TFilter` must implement `ITestFilter` and expose a public parameterless constructor.

Everything else behaves exactly like `TestFilterProviderAttribute`, including the "at most one per test assembly" rule — the two attributes count as one and the same registration, so applying both to a single assembly is an error. They are distinct types, so the compiler does not report that as a duplicate attribute; `MSTEST0081` does.

This attribute is only available when targeting .NET. On .NET Framework, use the non-generic `TestFilterProviderAttribute`. A test project that multi-targets both can select the right form with `#if NET`:

```csharp
#if NET
[assembly: TestFilterProvider<MyFilter>]
#else
[assembly: TestFilterProvider(typeof(MyFilter))]
#endif
```

This API is experimental. It may change, break, or be removed at any time without notice.

## Example

```csharp
[assembly: TestFilterProvider<NightlyFilter>]
            
public sealed class NightlyFilter : ITestFilter
{
    public TestFilterResult Filter(TestFilterContext context)
        => context.Categories.Contains("Nightly")
            && Environment.GetEnvironmentVariable("RUN_NIGHTLY") != "1"
            ? TestFilterResult.Skip("Set RUN_NIGHTLY=1 to run nightly tests.")
            : TestFilterResult.Run;
}
```

## Constructors

### TestFilterProviderAttribute

```csharp
public TestFilterProviderAttribute()
```
