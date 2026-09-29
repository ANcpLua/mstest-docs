# TestRun class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.Extensions.dll`
- Package: `MSTest.TestFramework` 4.4.1

Provides ambient access to information about the currently-executing test run.

```csharp
[Experimental("MSTESTEXP", UrlFormat = "https://aka.ms/mstest/diagnostics#{0}")]
public static class TestRun
```

## Remarks

`TestRun.Current` always returns a non-`null` `ITestRunInfo`; before tests start executing it exposes empty collections.

The information is scoped to the current process and (on .NET Framework) the current AppDomain. Cross-process or cross-AppDomain test runs each have their own snapshot.

This API is experimental. It may change, break, or be removed at any time without notice.

## Properties

### Current

```csharp
public static ITestRunInfo Current { get; }
```

Gets information about the currently-executing test run. Never returns `null`.
