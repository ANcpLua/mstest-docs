# PlannedTest class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.Extensions.dll`
- Package: `MSTest.TestFramework` 4.5.1

Represents a single test that is planned to run (i.e. has been discovered and passed the active filter) in the current test run. Returned by `ITestRunInfo.PlannedTests`.

```csharp
[Experimental("MSTESTEXP", UrlFormat = "https://aka.ms/mstest/diagnostics#{0}")]
public sealed class PlannedTest
```

## Remarks

Instances are immutable snapshots produced at the start of test execution for the assembly. They are intended for read-only inspection (for example to decide whether expensive setup is needed in `[AssemblyInitialize]`); they do not carry execution-time state such as outcome, exceptions, or data-driven rows.

This API is experimental. It may change, break, or be removed at any time without notice.

## Constructors

### PlannedTest

```csharp
public PlannedTest(
    string fullyQualifiedTestClassName,
    string testName,
    string? testDisplayName,
    string assemblyPath,
    string? managedTypeName,
    string? managedMethodName,
    string? declaringFilePath,
    int? declaringLineNumber,
    IReadOnlyCollection<string> testCategories,
    IReadOnlyCollection<KeyValuePair<string, string>> testProperties)
```

Initializes a new instance of the `PlannedTest` class.

**Parameters:**

- `fullyQualifiedTestClassName`: The fully-qualified name of the class declaring the test method.
- `testName`: The simple name of the test method.
- `testDisplayName`: The display name of the test, when set; otherwise `null`.
- `assemblyPath`: The full path of the assembly that declares the test, on disk.
- `managedTypeName`: The ECMA-335 managed type name for the declaring type, when available.
- `managedMethodName`: The ECMA-335 managed method name (encoding parameter types) for the test method, when available.
- `declaringFilePath`: The source file that declares the test, captured at compile-time by `TestMethodAttribute`, when available.
- `declaringLineNumber`: The line number within `declaringFilePath` at which the test is declared, when available.
- `testCategories`: The categories applied via `TestCategoryAttribute`.
- `testProperties`: The name/value pairs applied via `TestPropertyAttribute`. Multiple entries with the same name are preserved.

## Properties

### AssemblyPath

```csharp
public string AssemblyPath { get; }
```

Gets the full path of the assembly that declares the test, on disk.

### DeclaringFilePath

```csharp
public string? DeclaringFilePath { get; }
```

Gets the source file path that declares the test. This value is captured at compile time by `TestMethodAttribute`; it can be `null` when the test is declared via a custom test-method attribute that does not propagate the caller information.

### DeclaringLineNumber

```csharp
public int? DeclaringLineNumber { get; }
```

Gets the line number within `PlannedTest.DeclaringFilePath` at which the test is declared, when available; otherwise `null`.

### FullyQualifiedTestClassName

```csharp
public string FullyQualifiedTestClassName { get; }
```

Gets the fully-qualified name of the class declaring the test method. Mirrors `TestContext.FullyQualifiedTestClassName`.

### ManagedMethodName

```csharp
public string? ManagedMethodName { get; }
```

Gets the ECMA-335 managed method name (encoding parameter types) for the test method, when available. Use this for unambiguous identification of overloaded methods.

### ManagedTypeName

```csharp
public string? ManagedTypeName { get; }
```

Gets the ECMA-335 managed type name for the declaring type, when available.

### TestCategories

```csharp
public IReadOnlyCollection<string> TestCategories { get; }
```

Gets the categories applied to this test via `TestCategoryAttribute` at the method, class, or assembly level.

### TestDisplayName

```csharp
public string? TestDisplayName { get; }
```

Gets the display name of the test, when one was set; otherwise `null`. Mirrors `TestContext.TestDisplayName`.

### TestName

```csharp
public string TestName { get; }
```

Gets the simple name of the test method. Mirrors `TestContext.TestName`.

### TestProperties

```csharp
public IReadOnlyCollection<KeyValuePair<string, string>> TestProperties { get; }
```

Gets the name/value pairs applied to this test via `TestPropertyAttribute`. Multiple attributes with the same name are preserved as separate entries.
