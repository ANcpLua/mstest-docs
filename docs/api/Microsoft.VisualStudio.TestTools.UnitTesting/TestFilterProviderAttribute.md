# TestFilterProviderAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

Registers a user-supplied `ITestFilter` implementation that the MSTest adapter invokes for every test it is about to run, after any command-line filter (`--filter`, Test Explorer selection, etc.) has been applied.

```csharp
[AttributeUsage(AttributeTargets.Assembly, AllowMultiple = false, Inherited = false)]
[Experimental("MSTESTEXP", UrlFormat = "https://aka.ms/mstest/diagnostics#{0}")]
public sealed class TestFilterProviderAttribute : Attribute
```

## Remarks

Apply this attribute at the assembly level on the test assembly itself. At most one `TestFilterProviderAttribute` may be applied per test assembly; this is intentional so that filter ordering is not part of the public API. If multiple filtering strategies are needed, compose them explicitly inside a single `ITestFilter` implementation.

The filter type must be non-generic and instantiable — a concrete class or a struct, but not a `ref struct` — with a public parameterless constructor, and must implement `ITestFilter`. A single instance is created per test assembly per test run and reused for every test of that assembly.

Because the filter type is passed as a `Type`, none of those requirements are checked by the compiler. The `MSTEST0081` analyzer validates them at build time. On .NET the generic `TestFilterProviderAttribute<TFilter>` variant additionally enforces the `ITestFilter` and public-parameterless-constructor requirements through its generic constraints; the remaining ones are still only reported by `MSTEST0081`.

The filter runs *before* the test type is loaded, before `[AssemblyInitialize]`, before `[ClassInitialize]`, and before the test constructor is invoked, so dropping or skipping a test through `ITestFilter` avoids paying any of those costs.

This API is experimental. It may change, break, or be removed at any time without notice.

## Example

```csharp
[assembly: TestFilterProvider(typeof(NightlyFilter))]
            
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
public TestFilterProviderAttribute(Type filterType)
```

Initializes a new instance of the `TestFilterProviderAttribute` class.

**Parameters:**

- `filterType`: The `ITestFilter` implementation to instantiate and invoke for every test in the consuming test assembly. Must be a non-generic, instantiable type with a public parameterless constructor.

## Properties

### FilterType

```csharp
public Type FilterType { get; }
```

Gets the `ITestFilter` implementation registered by this attribute.
