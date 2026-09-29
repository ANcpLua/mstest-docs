# MSTest docs — local Markdown copy

MSTest on Microsoft.Testing.Platform (MTP) as Markdown, one file per page. Nothing else is covered: MTP is the only test platform here.

```
MSTest.Sdk      = 4.4.1
MSTest API docs = mstest-net-4.4
Runner          = Microsoft.Testing.Platform
MTP             = 2.4.1
TFM             = net10.0
.NET SDK        = 10.0.401 (Runtime 10.0.12)
```

## How to use this folder

- Find the topic below, open **one** file, read it. Don't load the whole folder.
- Paths are relative to this folder. `grep -ril <term> docs/` when the index doesn't name it.
- `docs/mstest/` and `docs/testing-platform/` are the guides, `docs/api/` is the API reference of exactly the pinned packages.
- The guides describe the current release and name the version a feature arrived in; the API reference is proof of what the pinned version has.

## Sources

- Guides: [dotnet/docs](https://github.com/dotnet/docs/tree/2afde00bc94b9c2ffa6a3d607be48f555f3fdc5c/docs/core/testing) (branch `live`, commit `2afde00`), © Microsoft, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
  Changed for this copy: includes and snippets are inlined, links point to local files or learn.microsoft.com, package versions in examples follow the pins above, and everything about other test platforms is removed.
- API reference: generated from the assemblies and XML documentation of the NuGet packages `MSTest.TestFramework` 4.4.1 and `Microsoft.Testing.Platform` 2.4.1 ([microsoft/testfx](https://github.com/microsoft/testfx), MIT).

## Refresh

- Edit `VERSION` to pin other versions.
- `python3 scripts/refresh_docs.py` — rebuild `docs/` and this file. Needs `git` and the .NET SDK (`dotnet run scripts/api_reference.cs` writes the API reference).

This file is generated — edit `scripts/refresh_docs.py`, not this file.

## Index

### `docs/mstest/`

- `docs/mstest/intro.md` — **MSTest overview**: Learn about MSTest, Microsoft's testing framework for .NET, including supported platforms, key features, and getting started.

### `docs/testing-platform/`

- `docs/testing-platform/cli-options.md` — **Microsoft.Testing.Platform (MTP) CLI options reference**: Find platform and extension command-line options for MTP in one place.
- `docs/testing-platform/config.md` — **Microsoft.Testing.Platform (MTP) config options**: Learn how to configure MTP using testconfig.json configuration settings and environment variables.
- `docs/testing-platform/dotnet-test-cli.md` — **dotnet test command with Microsoft.Testing.Platform (MTP)**: The dotnet test command is used to execute unit tests in a given project using MTP.
- `docs/testing-platform/dotnet-test.md` — **Testing with 'dotnet test'**: The `dotnet test` command runs test applications built with MTP in *MTP* mode, introduced with the .NET 10 SDK.
- `docs/testing-platform/intro.md` — **Microsoft.Testing.Platform overview - .NET test runner**: Microsoft.Testing.Platform (MTP) is a lightweight and portable test platform for running tests in all contexts, including continuous integration (CI) pipelin…
- `docs/testing-platform/run-and-debug.md` — **Run and debug tests with Microsoft.Testing.Platform (MTP)**: Learn how to run and debug MTP test projects from CLI, Visual Studio, Visual Studio Code, and CI pipelines.
- `docs/testing-platform/troubleshooting.md` — **Microsoft.Testing.Platform (MTP) troubleshooting**: Troubleshoot MTP issues, exit codes, and known problems.

### `docs/mstest/analyzers/`

- `docs/mstest/analyzers/design-rules.md` — **MSTest Design rules (code analysis)**: Learn about MSTest code analysis design rules.
- `docs/mstest/analyzers/mstest0001.md` — **MSTEST0001: Explicitly enable or disable tests parallelization**: Learn about code analysis rule MSTEST0001: Explicitly enable or disable tests parallelization
- `docs/mstest/analyzers/mstest0002.md` — **MSTEST0002: Test classes should have valid layout**: Learn about code analysis rule MSTEST0002: Test classes should have valid layout
- `docs/mstest/analyzers/mstest0003.md` — **MSTEST0003: Test methods should have valid layout**: Learn about code analysis rule MSTEST0003: Test methods should have valid layout
- `docs/mstest/analyzers/mstest0004.md` — **MSTEST0004: Public types should be test classes**: Learn about code analysis rule MSTEST0004: Public types should be test classes
- `docs/mstest/analyzers/mstest0005.md` — **MSTEST0005: Test context property should have valid layout**: Learn about code analysis rule MSTEST0005: Test context property should have valid layout
- `docs/mstest/analyzers/mstest0006.md` — **MSTEST0006: Avoid '[ExpectedException]'**: Learn about code analysis rule MSTEST0006: Avoid '[ExpectedException]'
- `docs/mstest/analyzers/mstest0007.md` — **MSTEST0007: Use test attributes only on test methods**: Learn about code analysis rule MSTEST0007: Ensure test attributes are set only on methods marked with the `TestMethod` attribute
- `docs/mstest/analyzers/mstest0008.md` — **MSTEST0008: TestInitialize method should have valid layout**: Learn about code analysis rule MSTEST0008: TestInitialize method should have valid layout
- `docs/mstest/analyzers/mstest0009.md` — **MSTEST0009: TestCleanup method should have valid layout**: Learn about code analysis rule MSTEST0009: TestCleanup method should have valid layout
- `docs/mstest/analyzers/mstest0010.md` — **MSTEST0010: ClassInitialize method should have valid layout**: Learn about code analysis rule MSTEST0010: ClassInitialize method should have valid layout
- `docs/mstest/analyzers/mstest0011.md` — **MSTEST0011: ClassCleanup method should have valid layout**: Learn about code analysis rule MSTEST0011: ClassCleanup method should have valid layout
- `docs/mstest/analyzers/mstest0012.md` — **MSTEST0012: AssemblyInitialize method should have valid layout**: Learn about code analysis rule MSTEST0012: AssemblyInitialize method should have valid layout
- `docs/mstest/analyzers/mstest0013.md` — **MSTEST0013: AssemblyCleanup method should have valid layout**: Learn about code analysis rule MSTEST0013: AssemblyCleanup method should have valid layout
- `docs/mstest/analyzers/mstest0014.md` — **MSTEST0014: DataRow should be valid**: Learn about code analysis rule MSTEST0014: DataRow should be valid
- `docs/mstest/analyzers/mstest0015.md` — **MSTEST0015: Test method should not be ignored**: Learn about code analysis rule MSTEST0015: Test method should not be ignored
- `docs/mstest/analyzers/mstest0016.md` — **MSTEST0016: Test class should have test method**: Learn about code analysis rule MSTEST0016: Test class should have test method
- `docs/mstest/analyzers/mstest0017.md` — **MSTEST0017: Assertion arguments should be passed in the correct order**: Learn about code analysis rule MSTEST0017: Assertion arguments should be passed in the correct order
- `docs/mstest/analyzers/mstest0018.md` — **MSTEST0018: DynamicData should be valid**: Learn about code analysis rule MSTEST0018: DynamicData should be valid
- `docs/mstest/analyzers/mstest0019.md` — **MSTEST0019: Prefer TestInitialize methods over constructors**: Learn about code analysis rule MSTEST0019: Prefer TestInitialize methods over constructors
- `docs/mstest/analyzers/mstest0020.md` — **MSTEST0020: Prefer constructors over TestInitialize methods**: Learn about code analysis rule MSTEST0020: Prefer constructors over TestInitialize methods
- `docs/mstest/analyzers/mstest0021.md` — **MSTEST0021: Prefer Dispose over TestCleanup methods**: Learn about code analysis rule MSTEST0021: Prefer Dispose over TestCleanup methods
- `docs/mstest/analyzers/mstest0022.md` — **MSTEST0022: Prefer TestCleanup over Dispose methods**: Learn about code analysis rule MSTEST0022: Prefer TestCleanup over Dispose methods
- `docs/mstest/analyzers/mstest0023.md` — **MSTEST0023: Do not negate boolean assertions**: Learn about code analysis rule MSTEST0023: Do not negate boolean assertions
- `docs/mstest/analyzers/mstest0024.md` — **MSTEST0024: Do not store TestContext in a static member**: Learn about code analysis rule MSTEST0024: Do not store TestContext in a static member
- `docs/mstest/analyzers/mstest0025.md` — **MSTEST0025: Use 'Assert.Fail' instead of an always-failing assert**: Learn about code analysis rule MSTEST0025: Use 'Assert.Fail' instead of an always-failing assert
- `docs/mstest/analyzers/mstest0026.md` — **MSTEST0026: Avoid conditional access in assertions**: Learn about code analysis rule MSTEST0026: Avoid conditional access in assertions
- `docs/mstest/analyzers/mstest0027.md` — **MSTEST0027: Use Async suffix for async methods suppressor.**: Learn about code suppressor MSTEST0027: Use Async suffix for async methods suppressor.
- `docs/mstest/analyzers/mstest0028.md` — **MSTEST0028: Use Async suffix for async methods suppressor.**: Learn about code suppressor MSTEST0028: Use Async suffix for async methods suppressor.
- `docs/mstest/analyzers/mstest0029.md` — **MSTEST0029: Public method should be test method**: Learn about code analysis rule MSTEST0029: Public method should be test method
- `docs/mstest/analyzers/mstest0030.md` — **MSTEST0030: Type containing `[TestMethod]` should be marked with `[TestClass]`**: Learn about code analysis rule MSTEST0030: Type containing `[TestMethod]` should be marked with `[TestClass]`, otherwise the test method will be silently ign…
- `docs/mstest/analyzers/mstest0031.md` — **MSTEST0031: `System.ComponentModel.DescriptionAttribute` has no effect on test methods.**: Learn about code analysis rule MSTEST0031: `System.ComponentModel.DescriptionAttribute` has no effect in the context of tests, so likely user wanted to use `…
- `docs/mstest/analyzers/mstest0032.md` — **MSTEST0032: Review or remove the assertion as its condition is known to be always true.**: Learn about code analysis rule MSTEST0032: Review or remove the assertion as its condition is known to be always true.
- `docs/mstest/analyzers/mstest0033.md` — **MSTEST0033: Non-nullable reference not initialized suppressor.**: Learn about code suppressor MSTEST0033: Non-nullable reference not initialized suppressor.
- `docs/mstest/analyzers/mstest0034.md` — **MSTEST0034: Use `ClassCleanupBehavior.EndOfClass` with the `[ClassCleanup]`.**: Learn about code analysis rule MSTEST0034: Use `ClassCleanupBehavior.EndOfClass` with the `[ClassCleanup]`.
- `docs/mstest/analyzers/mstest0035.md` — **MSTEST0035: [DeploymentItem] can be specified only on test class or test method.**: Learn about code analysis rule MSTEST0035: `[DeploymentItem]` can be specified only on test class or test method.
- `docs/mstest/analyzers/mstest0036.md` — **MSTEST0036: Do not use shadowing inside test class.**: Learn about code analysis rule MSTEST0036: Do not use shadowing inside test class.
- `docs/mstest/analyzers/mstest0037.md` — **MSTEST0037: Use proper 'Assert' methods**: Learn about code analysis rule MSTEST0037: Use proper 'Assert' methods.
- `docs/mstest/analyzers/mstest0038.md` — **MSTEST0038: Don't use 'Assert.AreSame' or 'Assert.AreNotSame' with value types**: Learn about code analysis rule MSTEST0038: Don't use 'Assert.AreSame' or 'Assert.AreNotSame' with value types
- `docs/mstest/analyzers/mstest0039.md` — **MSTEST0039: Use newer 'Assert.Throws' methods**: Learn about code analysis rule MSTEST0039: Use 'Assert.ThrowsExactly' instead of 'Assert.ThrowsException'
- `docs/mstest/analyzers/mstest0040.md` — **MSTEST0040: Do not assert inside 'async void' contexts**: Learn about code analysis rule MSTEST0040: Do not assert inside 'async void' methods, local functions, or lambdas because they may not fail the test
- `docs/mstest/analyzers/mstest0041.md` — **MSTEST0041: Use 'ConditionBaseAttribute' on test classes**: Learn about code analysis rule MSTEST0041: Use 'ConditionBaseAttribute' on test classes
- `docs/mstest/analyzers/mstest0042.md` — **MSTEST0042: Avoid duplicated 'DataRow' entries**: Learn about code analysis rule MSTEST0042: Avoid duplicated 'DataRow' entries
- `docs/mstest/analyzers/mstest0043.md` — **MSTEST0043: Use retry attribute on test method**: Learn about code analysis rule MSTEST0043: Use retry attribute on test method
- `docs/mstest/analyzers/mstest0044.md` — **MSTEST0044: Prefer TestMethod over DataTestMethod**: Learn about code analysis rule MSTEST0044: Prefer TestMethod over DataTestMethod
- `docs/mstest/analyzers/mstest0045.md` — **MSTEST0045: Use cooperative cancellation for timeout**: Learn about code analysis rule MSTEST0045: Use cooperative cancellation for timeout
- `docs/mstest/analyzers/mstest0046.md` — **MSTEST0046: Use Assert instead of StringAssert**: Learn about code analysis rule MSTEST0046: Use Assert instead of StringAssert
- `docs/mstest/analyzers/mstest0047.md` — **MSTEST0047: Unused TestContext parameter suppressor.**: Learn about code suppressor MSTEST0047: Unused TestContext parameter suppressor.
- `docs/mstest/analyzers/mstest0048.md` — **MSTEST0048: Avoid TestContext properties in fixture methods**: Learn about code analysis rule MSTEST0048: Avoid TestContext properties in fixture methods
- `docs/mstest/analyzers/mstest0049.md` — **MSTEST0049: Flow TestContext cancellation token**: Learn about code analysis rule MSTEST0049: Flow TestContext cancellation token
- `docs/mstest/analyzers/mstest0050.md` — **MSTEST0050: Global test fixture should be valid**: Learn about code analysis rule MSTEST0050: Global test fixture should be valid
- `docs/mstest/analyzers/mstest0051.md` — **MSTEST0051: Assert.Throws should contain only a single statement**: Learn about code analysis rule MSTEST0051: Assert.Throws should contain only a single statement
- `docs/mstest/analyzers/mstest0052.md` — **MSTEST0052: Avoid passing an explicit 'DynamicDataSourceType' and use the default auto detect behavior**: Learn about code analysis rule MSTEST0052: Avoid passing an explicit 'DynamicDataSourceType' and use the default auto detect behavior
- `docs/mstest/analyzers/mstest0053.md` — **MSTEST0053: Avoid using Assert methods with format parameters**: Learn about code analysis rule MSTEST0053: Avoid using Assert methods with format parameters
- `docs/mstest/analyzers/mstest0054.md` — **MSTEST0054: Use TestContext.CancellationToken instead of TestContext.CancellationTokenSource.Token**: Learn about code analysis rule MSTEST0054: Use TestContext.CancellationToken instead of TestContext.CancellationTokenSource.Token
- `docs/mstest/analyzers/mstest0055.md` — **MSTEST0055: Do not ignore the return value of string methods**: Learn about code analysis rule MSTEST0055: Do not ignore the return value of string methods
- `docs/mstest/analyzers/mstest0056.md` — **MSTEST0056: Use DisplayName property for test method display names**: Learn about code analysis rule MSTEST0056: Use DisplayName property for test method display names
- `docs/mstest/analyzers/mstest0057.md` — **MSTEST0057: Propagate source information in custom test method attributes**: Learn about code analysis rule MSTEST0057: Propagate source information in custom test method attributes
- `docs/mstest/analyzers/mstest0058.md` — **MSTEST0058: Avoid assertions in catch blocks**: Learn about code analysis rule MSTEST0058: Avoid assertions in catch blocks
- `docs/mstest/analyzers/mstest0059.md` — **MSTEST0059: Do not use both Parallelize and DoNotParallelize attributes**: Learn about code analysis rule MSTEST0059: Do not use both Parallelize and DoNotParallelize attributes
- `docs/mstest/analyzers/mstest0060.md` — **MSTEST0060: Avoid duplicate test method attributes**: Learn about code analysis rule MSTEST0060: Avoid duplicate test method attributes
- `docs/mstest/analyzers/mstest0061.md` — **MSTEST0061: Use OSCondition attribute instead of runtime checks**: Learn about code analysis rule MSTEST0061: Use OSCondition attribute instead of runtime checks
- `docs/mstest/analyzers/mstest0062.md` — **MSTEST0062: Avoid out and ref parameters in test methods**: Learn about code analysis rule MSTEST0062: Avoid out and ref parameters in test methods
- `docs/mstest/analyzers/mstest0063.md` — **MSTEST0063: Test classes should have valid constructors**: Learn about code analysis rule MSTEST0063: Test classes should have valid constructors
- `docs/mstest/analyzers/mstest0064.md` — **MSTEST0064: Prefer async assertion methods**: Learn about code analysis rule MSTEST0064: Prefer async assertion methods
- `docs/mstest/analyzers/mstest0065.md` — **MSTEST0065: Avoid Assert.AreEqual on collection types**: Learn about code analysis rule MSTEST0065: Avoid Assert.AreEqual on collection types
- `docs/mstest/analyzers/mstest0066.md` — **MSTEST0066: '[Ignore]' should specify a justification**: Learn about code analysis rule MSTEST0066: '[Ignore]' should specify a justification
- `docs/mstest/analyzers/mstest0067.md` — **MSTEST0067: Avoid synchronously blocking calls in test code**: Learn about code analysis rule MSTEST0067: Avoid synchronously blocking calls in test code
- `docs/mstest/analyzers/mstest0068.md` — **MSTEST0068: Use Assert instead of CollectionAssert**: Learn about code analysis rule MSTEST0068: Use Assert instead of CollectionAssert
- `docs/mstest/analyzers/mstest0069.md` — **MSTEST0069: Inherited [TestClass] is ignored by the MSTest source generator**: Learn about code analysis rule MSTEST0069: Inherited [TestClass] is ignored by the MSTest source generator
- `docs/mstest/analyzers/mstest0070.md` — **MSTEST0070: [MemberCondition] arguments should be valid**: Learn about code analysis rule MSTEST0070: [MemberCondition] arguments should be valid
- `docs/mstest/analyzers/mstest0071.md` — **MSTEST0071: Test method should not specify a display name equal to its name**: Learn about code analysis rule MSTEST0071: Test method should not specify a display name equal to its name
- `docs/mstest/analyzers/mstest0072.md` — **MSTEST0072: '[AssemblyFixtureProvider]' isn't supported with ahead-of-time compilation**: Learn about code analysis rule MSTEST0072: '[AssemblyFixtureProvider]' isn't supported with ahead-of-time compilation
- `docs/mstest/analyzers/mstest0073.md` — **MSTEST0073: Prefer a constant for the '[ResourceLock]' resource key**: Learn about code analysis rule MSTEST0073: Prefer a constant for the '[ResourceLock]' resource key
- `docs/mstest/analyzers/mstest0074.md` — **MSTEST0074: Test mutating process-global state should declare a resource lock**: Learn about code analysis rule MSTEST0074: Test mutating process-global state should declare a resource lock
- `docs/mstest/analyzers/mstest0075.md` — **MSTEST0075: Avoid changing the current directory in a parallelized test**: Learn about code analysis rule MSTEST0075: Avoid changing the current directory in a parallelized test
- `docs/mstest/analyzers/mstest0076.md` — **MSTEST0076: Avoid mutating process-wide culture in a parallelized test**: Learn about code analysis rule MSTEST0076: Avoid mutating process-wide culture in a parallelized test
- `docs/mstest/analyzers/mstest0077.md` — **MSTEST0077: Avoid hardcoded or shared filesystem paths in a parallelized test**: Learn about code analysis rule MSTEST0077: Avoid hardcoded or shared filesystem paths in a parallelized test
- `docs/mstest/analyzers/mstest0078.md` — **MSTEST0078: '[DependsOn]' arguments should be valid**: Learn about code analysis rule MSTEST0078: '[DependsOn]' arguments should be valid
- `docs/mstest/analyzers/mstest0079.md` — **MSTEST0079: Use ArchitectureCondition attribute instead of runtime checks**: Learn about code analysis rule MSTEST0079: Use ArchitectureCondition attribute instead of runtime checks
- `docs/mstest/analyzers/mstest0080.md` — **MSTEST0080: Use CICondition attribute instead of environment checks**: Learn about code analysis rule MSTEST0080: Use CICondition attribute instead of environment checks
- `docs/mstest/analyzers/mstest0081.md` — **MSTEST0081: '[TestFilterProvider]' should reference a valid test filter type**: Learn about code analysis rule MSTEST0081: '[TestFilterProvider]' should reference a valid test filter type
- `docs/mstest/analyzers/mstest0082.md` — **MSTEST0082: A test class inherits a lifecycle or test method from a different MSTest version**: Learn about code analysis rule MSTEST0082: A test class inherits a lifecycle or test method from a different MSTest version
- `docs/mstest/analyzers/mstest0083.md` — **MSTEST0083: Use '[ExecutableCondition]' instead of 'File.Exists' checks before 'Process.Start'**: Learn about code analysis rule MSTEST0083: Use '[ExecutableCondition]' instead of 'File.Exists' checks before 'Process.Start'
- `docs/mstest/analyzers/overview.md` — **MSTest code analysis**: Learn about the MSTest code analysis.
- `docs/mstest/analyzers/performance-rules.md` — **MSTest Performance rules (code analysis)**: Learn about MSTest code analysis performance rules.
- `docs/mstest/analyzers/suppression-rules.md` — **MSTest Suppression rules (code analysis)**: Learn about MSTest code suppression rules.
- `docs/mstest/analyzers/usage-rules.md` — **MSTest Usage rules (code analysis)**: Learn about MSTest code analysis usage rules.

### `docs/mstest/getting-started/`

- `docs/mstest/getting-started/csharp.md` — **Get started with C# and MSTest**: Learn unit test concepts in C# and .NET through an interactive experience building a sample solution step-by-step using dotnet test and MSTest.
- `docs/mstest/getting-started/fsharp.md` — **Get started with F# and MSTest**: Learn unit test concepts for F# in .NET through an interactive experience building a sample solution step-by-step using dotnet test and MSTest.
- `docs/mstest/getting-started/overview.md` — **Get started with MSTest**: Learn how to create your first MSTest project and run tests.
- `docs/mstest/getting-started/visual-basic.md` — **Get started with Visual Basic and MSTest**: Learn unit test concepts in .NET through an interactive experience building a sample Visual Basic solution step-by-step using MSTest.

### `docs/mstest/migration/`

- `docs/mstest/migration/v1-to-v3.md` — **MSTest migration to v3**: Learn about migrating from legacy MSTest (MSTest v1) to latest MSTest (MSTest v3).
- `docs/mstest/migration/v3-to-v4.md` — **MSTest migration from v3 to v4**: Learn about migrating to MSTest v4.

### `docs/mstest/running-tests/`

- `docs/mstest/running-tests/configure.md` — **Configure MSTest**: Learn how to configure MSTest.
- `docs/mstest/running-tests/filter.md` — **Run selected unit tests**: How to use a filter expression to run selected unit tests with the dotnet test command in .NET Core.
- `docs/mstest/running-tests/overview.md` — **Run tests with MSTest**: There are several ways to run MSTest tests depending on your needs.
- `docs/mstest/running-tests/sdk.md` — **MSTest SDK configuration**: Learn how to configure MSTest.Sdk profiles, extensions, and advanced features.
- `docs/mstest/running-tests/winui.md` — **Test WinUI 3 apps with MSTest and Microsoft.Testing.Platform**: Learn how to configure unpackaged and packaged full-trust WinUI 3 test apps with MSTest and Microsoft.Testing.Platform.

### `docs/mstest/writing-tests/`

- `docs/mstest/writing-tests/assertions.md` — **MSTest assertions**: Learn about MSTest assertions including Assert, StringAssert, and CollectionAssert classes for validating test results.
- `docs/mstest/writing-tests/controlling-execution.md` — **Test execution and control in MSTest**: Learn how to control test execution in MSTest with parallelization, threading, timeouts, retries, and conditional execution.
- `docs/mstest/writing-tests/data-driven.md` — **Data-driven testing in MSTest**: Learn how to use DataRow, DynamicData, CombinatorialData, and TestDataRow to run MSTest tests with multiple inputs.
- `docs/mstest/writing-tests/deployment-items.md` — **Deploy files alongside MSTest tests**: Learn how to use the DeploymentItemAttribute in MSTest to copy files and folders alongside test assemblies for use during test execution.
- `docs/mstest/writing-tests/lifecycle.md` — **MSTest test lifecycle**: Learn about the creation and lifecycle of test classes and test methods in MSTest, including initialization and cleanup at assembly, class, and test levels.
- `docs/mstest/writing-tests/ordering.md` — **Order unit tests**: Learn how to order unit tests with .NET Core.
- `docs/mstest/writing-tests/organizing.md` — **Test organization and metadata in MSTest**: Learn how to organize and categorize tests in MSTest using categories, properties, priorities, owners, and work item references.
- `docs/mstest/writing-tests/overview.md` — **Write tests with MSTest**: Learn how to write tests using MSTest, including attributes, assertions, data-driven testing, and test lifecycle management.
- `docs/mstest/writing-tests/testcontext.md` — **MSTest TestContext**: Learn about the TestContext class of MSTest.

### `docs/testing-platform/extending/`

- `docs/testing-platform/extending/capabilities.md` — **Microsoft.Testing.Platform (MTP) capabilities overview**: Learn about MTP capabilities concept.
- `docs/testing-platform/extending/extensions.md` — **Build extensions for Microsoft.Testing.Platform (MTP)**: Learn how to create in-process and out-of-process extensions for Microsoft.Testing.Platform (MTP).
- `docs/testing-platform/extending/overview.md` — **Create custom extensions for Microsoft.Testing.Platform (MTP)**: Learn how to build custom test frameworks and extensions for Microsoft.Testing.Platform (MTP).
- `docs/testing-platform/extending/server-mode.md` — **Microsoft.Testing.Platform (MTP) server mode**: Learn how tools and IDEs drive MTP test applications through JSON-RPC server mode.
- `docs/testing-platform/extending/services.md` — **Microsoft.Testing.Platform services overview**: Learn about the available Microsoft.Testing.Platform (MTP) services.
- `docs/testing-platform/extending/test-framework.md` — **Build a test framework for Microsoft.Testing.Platform (MTP)**: Learn how to create a custom test framework for Microsoft.Testing.Platform (MTP), including registration, lifecycle, and test node reporting.

### `docs/testing-platform/features/`

- `docs/testing-platform/features/ai.md` — **Microsoft.Testing.Platform (MTP) AI integrations**: Learn how MTP extensions access AI chat clients and configure the Azure AI Foundry provider.
- `docs/testing-platform/features/code-coverage.md` — **Microsoft.Testing.Platform (MTP) code coverage**: Learn about collecting code coverage data with MTP.
- `docs/testing-platform/features/crash-hang-dumps.md` — **Microsoft.Testing.Platform (MTP) crash and hang dumps**: Learn about the MTP extensions for collecting crash dumps and hang dumps during test execution.
- `docs/testing-platform/features/diagnostics.md` — **Microsoft.Testing.Platform (MTP) diagnostics**: Learn about the MTP extensions that capture evidence, such as screen recordings, to help you diagnose a test run.
- `docs/testing-platform/features/extensions-integration.md` — **Microsoft.Testing.Platform (MTP) Microsoft.Extensions integration**: Learn about the MTP extensions that bridge Microsoft.Testing.Platform to the Microsoft.Extensions.* libraries your application already uses.
- `docs/testing-platform/features/fakes.md` — **Microsoft Fakes support for Microsoft.Testing.Platform (MTP)**: Learn about the MTP Fakes extension capabilities and how to use it.
- `docs/testing-platform/features/hot-reload.md` — **Microsoft.Testing.Platform (MTP) Hot Reload**: Learn about the MTP Hot Reload extension for running tests with hot reload.
- `docs/testing-platform/features/open-telemetry.md` — **Microsoft.Testing.Platform (MTP) OpenTelemetry**: Learn how to use the OpenTelemetry extension to emit traces and metrics from MTP.
- `docs/testing-platform/features/overview.md` — **Microsoft.Testing.Platform features**: Learn about the various Microsoft.Testing.Platform features, both built-in and available as extensions.
- `docs/testing-platform/features/retry.md` — **Microsoft.Testing.Platform (MTP) retry**: Learn about retrying failed tests with MTP.
- `docs/testing-platform/features/telemetry.md` — **Microsoft.Testing.Platform (MTP) telemetry**: Learn about the telemetry data collected by MTP and how to disable it.
- `docs/testing-platform/features/terminal-output.md` — **Microsoft.Testing.Platform (MTP) terminal output**: Learn about the built-in terminal test reporter in MTP, including output modes, ANSI support, and progress indicators.
- `docs/testing-platform/features/test-host-deployment.md` — **Microsoft.Testing.Platform (MTP) test host deployment**: Learn how MTP extensions control test host deployment and startup.
- `docs/testing-platform/features/test-reports.md` — **Microsoft.Testing.Platform (MTP) test reports**: Learn about the MTP extensions that create test report files (TRX, HTML, JUnit, CTRF, Azure DevOps, GitHub Actions).

### `docs/testing-platform/migration/`

- `docs/testing-platform/migration/v1-to-v2.md` — **Migrating from Microsoft.Testing.Platform (MTP) v1 to v2**: Learn how to migrate to MTP v2 and understand the key changes.

### `docs/api/Microsoft.Testing.Platform.Builder/`

- `docs/api/Microsoft.Testing.Platform.Builder/ConfigurationOptions.md` — **ConfigurationOptions class**: Represents the configuration options for the builder.
- `docs/api/Microsoft.Testing.Platform.Builder/ConfigurationSourcesOptions.md` — **ConfigurationSourcesOptions class**: Represents the options for configuration sources.
- `docs/api/Microsoft.Testing.Platform.Builder/IArtifactPostProcessingApplicationBuilder.md` — **IArtifactPostProcessingApplicationBuilder interface**: Represents a test application builder that supports registering artifact post-processors and tools.
- `docs/api/Microsoft.Testing.Platform.Builder/ITestApplication.md` — **ITestApplication interface**: Represents an interface for a test application.
- `docs/api/Microsoft.Testing.Platform.Builder/ITestApplicationBuilder.md` — **ITestApplicationBuilder interface**: Represents an interface for building test applications.
- `docs/api/Microsoft.Testing.Platform.Builder/TestApplication.md` — **TestApplication class**: Represents a test application.
- `docs/api/Microsoft.Testing.Platform.Builder/TestApplicationOptions.md` — **TestApplicationOptions class**: Represents the options for a test application.

### `docs/api/Microsoft.Testing.Platform.Capabilities.TestFramework/`

- `docs/api/Microsoft.Testing.Platform.Capabilities.TestFramework/IBannerMessageOwnerCapability.md` — **IBannerMessageOwnerCapability interface**: An optional test framework capability that allows the test framework to provide the banner message to the platform.
- `docs/api/Microsoft.Testing.Platform.Capabilities.TestFramework/IGracefulStopTestExecutionCapability.md` — **IGracefulStopTestExecutionCapability interface**: A capability to support stopping test execution gracefully, without cancelling/aborting everything.
- `docs/api/Microsoft.Testing.Platform.Capabilities.TestFramework/IGracefulStopTestExecutionResultCapability.md` — **IGracefulStopTestExecutionResultCapability interface**: A graceful-stop capability that reports whether a stop request was accepted.
- `docs/api/Microsoft.Testing.Platform.Capabilities.TestFramework/ITestFrameworkCapabilities.md` — **ITestFrameworkCapabilities interface**: Represents the capabilities of a test framework.
- `docs/api/Microsoft.Testing.Platform.Capabilities.TestFramework/ITestFrameworkCapability.md` — **ITestFrameworkCapability interface**: Represents a capability for a test framework.
- `docs/api/Microsoft.Testing.Platform.Capabilities.TestFramework/TestFrameworkCapabilities.md` — **TestFrameworkCapabilities class**: Represents the capabilities of a test framework.
- `docs/api/Microsoft.Testing.Platform.Capabilities.TestFramework/TestFrameworkCapabilitiesExtensions.md` — **TestFrameworkCapabilitiesExtensions class**: Provides extension methods for `ITestFrameworkCapabilities`.

### `docs/api/Microsoft.Testing.Platform.Capabilities/`

- `docs/api/Microsoft.Testing.Platform.Capabilities/ICapabilities-1.md` — **ICapabilities<TCapability> interface**: Represents the capabilities provided by an extension.
- `docs/api/Microsoft.Testing.Platform.Capabilities/ICapability.md` — **ICapability interface**: Represents a capability.

### `docs/api/Microsoft.Testing.Platform.CommandLine/`

- `docs/api/Microsoft.Testing.Platform.CommandLine/CommandLineOptionsExtensions.md` — **CommandLineOptionsExtensions class**: Provides extension methods for command-line options.
- `docs/api/Microsoft.Testing.Platform.CommandLine/CommandLineParseOption.md` — **CommandLineParseOption class**: Represents a command line parsed option.
- `docs/api/Microsoft.Testing.Platform.CommandLine/CommandLineParseResult.md` — **CommandLineParseResult class**: Represents the result of parsing a command line.
- `docs/api/Microsoft.Testing.Platform.CommandLine/ICommandLineManager.md` — **ICommandLineManager interface**: Represents a command line manager.
- `docs/api/Microsoft.Testing.Platform.CommandLine/ICommandLineOptions.md` — **ICommandLineOptions interface**: Represents the interface for command line options.

### `docs/api/Microsoft.Testing.Platform.Configurations/`

- `docs/api/Microsoft.Testing.Platform.Configurations/ConfigurationExtensions.md` — **ConfigurationExtensions class**: Provides extension methods for the IConfiguration interface.
- `docs/api/Microsoft.Testing.Platform.Configurations/IConfiguration.md` — **IConfiguration interface**: Represents a configuration interface.
- `docs/api/Microsoft.Testing.Platform.Configurations/IConfigurationManager.md` — **IConfigurationManager interface**: Represents a configuration manager.
- `docs/api/Microsoft.Testing.Platform.Configurations/IConfigurationProvider.md` — **IConfigurationProvider interface**: Represents a configuration provider.
- `docs/api/Microsoft.Testing.Platform.Configurations/IConfigurationRoot.md` — **IConfigurationRoot interface**: Represents the root of an aggregated hierarchical configuration.
- `docs/api/Microsoft.Testing.Platform.Configurations/IConfigurationSection.md` — **IConfigurationSection interface**: Represents a section of an aggregated hierarchical configuration.
- `docs/api/Microsoft.Testing.Platform.Configurations/IConfigurationSource.md` — **IConfigurationSource interface**: Represents a configuration source.
- `docs/api/Microsoft.Testing.Platform.Configurations/IHierarchicalConfigurationProvider.md` — **IHierarchicalConfigurationProvider interface**: Represents a configuration provider that exposes hierarchical configuration sections.

### `docs/api/Microsoft.Testing.Platform.Extensions.ArtifactPostProcessing/`

- `docs/api/Microsoft.Testing.Platform.Extensions.ArtifactPostProcessing/ArtifactPostProcessingContext.md` — **ArtifactPostProcessingContext class**: Describes the test run that produced artifacts supplied to an `IArtifactPostProcessor`.
- `docs/api/Microsoft.Testing.Platform.Extensions.ArtifactPostProcessing/ArtifactPostProcessingMode.md` — **ArtifactPostProcessingMode enum**: Specifies how the supplied artifacts relate to one another.
- `docs/api/Microsoft.Testing.Platform.Extensions.ArtifactPostProcessing/ArtifactPostProcessingRunSummary.md` — **ArtifactPostProcessingRunSummary class**: Describes authoritative run-level values supplied by the outer test orchestrator.
- `docs/api/Microsoft.Testing.Platform.Extensions.ArtifactPostProcessing/ArtifactPostProcessingTruncationReason.md` — **ArtifactPostProcessingTruncationReason enum**: Specifies why a test run was truncated before every scheduled test module completed.
- `docs/api/Microsoft.Testing.Platform.Extensions.ArtifactPostProcessing/IArtifactPostProcessingManager.md` — **IArtifactPostProcessingManager interface**: Registers artifact post-processors with a test application.
- `docs/api/Microsoft.Testing.Platform.Extensions.ArtifactPostProcessing/IArtifactPostProcessor.md` — **IArtifactPostProcessor interface**: Processes artifacts of one or more well-known kinds after test execution completes.
- `docs/api/Microsoft.Testing.Platform.Extensions.ArtifactPostProcessing/IArtifactPostProcessorRequiresPostProcessing.md` — **IArtifactPostProcessorRequiresPostProcessing interface**: Marks an artifact post-processor whose inputs are internal coordination artifacts that must always be post-processed, including when only one matching input…
- `docs/api/Microsoft.Testing.Platform.Extensions.ArtifactPostProcessing/InputArtifact.md` — **InputArtifact class**: Describes an artifact supplied to an `IArtifactPostProcessor`.
- `docs/api/Microsoft.Testing.Platform.Extensions.ArtifactPostProcessing/ProcessedArtifact.md` — **ProcessedArtifact class**: Describes an artifact produced by an `IArtifactPostProcessor`.

### `docs/api/Microsoft.Testing.Platform.Extensions.CommandLine/`

- `docs/api/Microsoft.Testing.Platform.Extensions.CommandLine/ArgumentArity.md` — **ArgumentArity struct**: Represents the arity (minimum and maximum number of arguments) for a command line argument.
- `docs/api/Microsoft.Testing.Platform.Extensions.CommandLine/CommandLineOption.md` — **CommandLineOption class**: Represents a command line option.
- `docs/api/Microsoft.Testing.Platform.Extensions.CommandLine/ICommandLineOptionsProvider.md` — **ICommandLineOptionsProvider interface**: Represents an interface for providing command line options.

### `docs/api/Microsoft.Testing.Platform.Extensions.Messages/`

- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/AssertionFailureProperty.md` — **AssertionFailureProperty class**: Property that carries the structured `expected` and `actual` values of a failed assertion, so consumers can render an expected-vs-actual diff instead of only…
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/CancelledTestNodeStateProperty.md` — **CancelledTestNodeStateProperty class**: Property that represents an eventual cancellation of a test node.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/CoverageAggregation.md` — **CoverageAggregation enum**: How per-scope values are combined for a threshold evaluation.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/CoverageMetric.md` — **CoverageMetric enum**: Identifies a code-coverage metric.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/CoverageReportFormat.md` — **CoverageReportFormat enum**: The on-disk format of a coverage report artifact.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/CoverageScope.md` — **CoverageScope struct**: Identifies the entity a coverage measurement or threshold describes.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/CoverageScopeLevel.md` — **CoverageScopeLevel enum**: The entity a coverage / threshold entry describes.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/DataWithSessionUid.md` — **DataWithSessionUid class**: Represents data with a session UID.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/DiscoveredTestNodeStateProperty.md` — **DiscoveredTestNodeStateProperty class**: Property that represents test node that has been discovered.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/ErrorTestNodeStateProperty.md` — **ErrorTestNodeStateProperty class**: Property that represents an eventual error in the test node.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/FailedTestNodeStateProperty.md` — **FailedTestNodeStateProperty class**: Property that represents a test node that has been failed.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/FileArtifact.md` — **FileArtifact class**: Represents a file artifact.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/FileArtifactProperty.md` — **FileArtifactProperty class**: Property that represents multiple artifacts/attachments to associate with a test node.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/FileLocationProperty.md` — **FileLocationProperty class**: Base property that represents a file location.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/IData.md` — **IData interface**: Represents the data interface.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/IDataProducer.md` — **IDataProducer interface**: Represents a data producer extension.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/IProperty.md` — **IProperty interface**: The interface that every test node property must implement.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/InProgressTestNodeStateProperty.md` — **InProgressTestNodeStateProperty class**: Property that represents a test node that is being executed.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/LinePosition.md` — **LinePosition struct**: Line position in a file.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/LinePositionSpan.md` — **LinePositionSpan struct**: Line position span in a file.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/PassedTestNodeStateProperty.md` — **PassedTestNodeStateProperty class**: Property that represents a test node that has been executed and passed.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/PropertyBag.md` — **PropertyBag class**: Represents a property bag.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/PropertyBagData.md` — **PropertyBagData class**: Represents a property bag data.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/RetryAttemptProperty.md` — **RetryAttemptProperty class**: Property that identifies a test node update as one attempt of an in-process retry sequence, i.e. several executions of the same test that a test framework pe…
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/SessionFileArtifact.md` — **SessionFileArtifact class**: Represents a session file artifact.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/SkippedTestNodeStateProperty.md` — **SkippedTestNodeStateProperty class**: Property that represents a test node that has been skipped.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/StandardErrorProperty.md` — **StandardErrorProperty class**: Property that represents standard error to associate with a test node.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/StandardOutputProperty.md` — **StandardOutputProperty class**: Property that represents standard output to associate with a test node.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/StepTimingInfo.md` — **StepTimingInfo class**: Information about the timing of a test node step.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/TestCoverageMessage.md` — **TestCoverageMessage class**: Reports a single code-coverage measurement (one metric for one scope) as counts.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/TestCoverageReportMessage.md` — **TestCoverageReportMessage class**: References a coverage report artifact so deep consumers (HTML/UI generators) can parse full-fidelity per-line data that the summary intentionally does not ca…
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/TestCoverageThresholdMessage.md` — **TestCoverageThresholdMessage class**: Reports the result of a coverage threshold evaluation.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/TestFileLocationProperty.md` — **TestFileLocationProperty class**: Property that represents a file location for a test node.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/TestMetadataProperty.md` — **TestMetadataProperty class**: Property that represents a generic test metadata property in the shape of a key-value pair associated with a `TestNode`.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/TestMethodIdentifierProperty.md` — **TestMethodIdentifierProperty class**: Property that uniquely identifies a test method.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/TestNode.md` — **TestNode class**: Represents a test node.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/TestNodeStateProperty.md` — **TestNodeStateProperty class**: Base class for test node state properties.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/TestNodeUid.md` — **TestNodeUid class**: Represents a test node unique identifier.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/TestNodeUpdateMessage.md` — **TestNodeUpdateMessage class**: A message representing a test node update.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/TimeoutTestNodeStateProperty.md` — **TimeoutTestNodeStateProperty class**: Property that represents an eventual timeout in the test node.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/TimingInfo.md` — **TimingInfo struct**: Information about the timing of a test node.
- `docs/api/Microsoft.Testing.Platform.Extensions.Messages/TimingProperty.md` — **TimingProperty class**: Property that represents the timing of a test node.

### `docs/api/Microsoft.Testing.Platform.Extensions.OutputDevice/`

- `docs/api/Microsoft.Testing.Platform.Extensions.OutputDevice/IOutputDeviceDataProducer.md` — **IOutputDeviceDataProducer interface**: Represents a producer of data that will be directed to the output device.

### `docs/api/Microsoft.Testing.Platform.Extensions.TestFramework/`

- `docs/api/Microsoft.Testing.Platform.Extensions.TestFramework/CloseTestSessionContext.md` — **CloseTestSessionContext class**: Context passed to a test framework adapter when `ITestFramework.CloseTestSessionAsync(CloseTestSessionContext)` is called.
- `docs/api/Microsoft.Testing.Platform.Extensions.TestFramework/CloseTestSessionResult.md` — **CloseTestSessionResult class**: Represents the result of closing a test session.
- `docs/api/Microsoft.Testing.Platform.Extensions.TestFramework/CreateTestSessionContext.md` — **CreateTestSessionContext class**: Context passed to a test framework adapter when `ITestFramework.CreateTestSessionAsync(CreateTestSessionContext)` is called.
- `docs/api/Microsoft.Testing.Platform.Extensions.TestFramework/CreateTestSessionResult.md` — **CreateTestSessionResult class**: Represents the result of creating a test session.
- `docs/api/Microsoft.Testing.Platform.Extensions.TestFramework/ExecuteRequestContext.md` — **ExecuteRequestContext class**: This class represents the context that is passed to a test framework adapter when the `ITestFramework.ExecuteRequestAsync(ExecuteRequestContext)` method is c…
- `docs/api/Microsoft.Testing.Platform.Extensions.TestFramework/ITestFramework.md` — **ITestFramework interface**: A specialized extension that represents a test framework.

### `docs/api/Microsoft.Testing.Platform.Extensions.TestHost/`

- `docs/api/Microsoft.Testing.Platform.Extensions.TestHost/ITestHostApplicationLifetime.md` — **ITestHostApplicationLifetime interface**: Represents the interface for test application lifecycle callbacks.
- `docs/api/Microsoft.Testing.Platform.Extensions.TestHost/ITestHostExtension.md` — **ITestHostExtension interface**: Represents a test host specialized extension.
- `docs/api/Microsoft.Testing.Platform.Extensions.TestHost/ITestSessionLifetimeHandler.md` — **ITestSessionLifetimeHandler interface**: Represents an interface for handling the lifetime of a test session.

### `docs/api/Microsoft.Testing.Platform.Extensions.TestHostControllers/`

- `docs/api/Microsoft.Testing.Platform.Extensions.TestHostControllers/EnvironmentVariable.md` — **EnvironmentVariable class**: Represents an environment variable.
- `docs/api/Microsoft.Testing.Platform.Extensions.TestHostControllers/IEnvironmentVariables.md` — **IEnvironmentVariables interface**: Represents an interface for managing environment variables.
- `docs/api/Microsoft.Testing.Platform.Extensions.TestHostControllers/IReadOnlyEnvironmentVariables.md` — **IReadOnlyEnvironmentVariables interface**: Represents an interface for reading environment variables.
- `docs/api/Microsoft.Testing.Platform.Extensions.TestHostControllers/ITestHostControllerConnectionAuthorizer.md` — **ITestHostControllerConnectionAuthorizer interface**: Implemented by an `ITestHostLauncher` that starts the test host under an operating-system security identity of its own, to authorize that identity on control…
- `docs/api/Microsoft.Testing.Platform.Extensions.TestHostControllers/ITestHostControllersExtension.md` — **ITestHostControllersExtension interface**: Represents an extension for test host controllers.
- `docs/api/Microsoft.Testing.Platform.Extensions.TestHostControllers/ITestHostEnvironmentVariableProvider.md` — **ITestHostEnvironmentVariableProvider interface**: Represents an interface for providing environment variables to the test host.
- `docs/api/Microsoft.Testing.Platform.Extensions.TestHostControllers/ITestHostHandle.md` — **ITestHostHandle interface**: Represents a launched test host that the platform monitors for completion.
- `docs/api/Microsoft.Testing.Platform.Extensions.TestHostControllers/ITestHostLauncher.md` — **ITestHostLauncher interface**: Allows an extension to control how the out-of-process test host is launched, replacing the platform's default `Process.Start` behavior.
- `docs/api/Microsoft.Testing.Platform.Extensions.TestHostControllers/ITestHostProcessInformation.md` — **ITestHostProcessInformation interface**: Represents information about a test host process.
- `docs/api/Microsoft.Testing.Platform.Extensions.TestHostControllers/ITestHostProcessLifetimeHandler.md` — **ITestHostProcessLifetimeHandler interface**: Represents an interface for handling the lifetime of the test host process.
- `docs/api/Microsoft.Testing.Platform.Extensions.TestHostControllers/OwnedEnvironmentVariable.md` — **OwnedEnvironmentVariable class**: Represents an owned environment variable.
- `docs/api/Microsoft.Testing.Platform.Extensions.TestHostControllers/TestHostLaunchContext.md` — **TestHostLaunchContext class**: Carries the fully prepared information the platform would have used to start the test host, passed to an `ITestHostLauncher`.

### `docs/api/Microsoft.Testing.Platform.Extensions.TestHostOrchestrator/`

- `docs/api/Microsoft.Testing.Platform.Extensions.TestHostOrchestrator/ITestHostExecutionOrchestrator.md` — **ITestHostExecutionOrchestrator interface**: Represents an extension that orchestrates test host execution.
- `docs/api/Microsoft.Testing.Platform.Extensions.TestHostOrchestrator/ITestHostOrchestratorApplicationLifetime.md` — **ITestHostOrchestratorApplicationLifetime interface**: Represents the application lifetime for a test host orchestrator.
- `docs/api/Microsoft.Testing.Platform.Extensions.TestHostOrchestrator/ITestHostOrchestratorExtension.md` — **ITestHostOrchestratorExtension interface**: Represents an extension for test host orchestrators.

### `docs/api/Microsoft.Testing.Platform.Extensions/`

- `docs/api/Microsoft.Testing.Platform.Extensions/CompositeExtensionFactory-1.md` — **CompositeExtensionFactory<TExtension> class**: Represents a factory for creating composite extensions.
- `docs/api/Microsoft.Testing.Platform.Extensions/IAsyncCleanableExtension.md` — **IAsyncCleanableExtension interface**: Represents an interface for asynchronously cleaning up resources.
- `docs/api/Microsoft.Testing.Platform.Extensions/IAsyncInitializableExtension.md` — **IAsyncInitializableExtension interface**: Represents an interface for asynchronously initializing an extension.
- `docs/api/Microsoft.Testing.Platform.Extensions/IBlockingDataConsumer.md` — **IBlockingDataConsumer interface**: Marker interface for a `IDataConsumer` that must consume the data inline, before the call to publish the data returns to the producer.
- `docs/api/Microsoft.Testing.Platform.Extensions/IDataConsumer.md` — **IDataConsumer interface**: Represents a data consumer that can consume data produced by a data producer.
- `docs/api/Microsoft.Testing.Platform.Extensions/IExtension.md` — **IExtension interface**: The interface that all extensions must implement.
- `docs/api/Microsoft.Testing.Platform.Extensions/ValidationResult.md` — **ValidationResult struct**: Represents the result of a validation operation.

### `docs/api/Microsoft.Testing.Platform.Helpers/`

- `docs/api/Microsoft.Testing.Platform.Helpers/TestApplicationBuilderExtensions.md` — **TestApplicationBuilderExtensions class**: A collection of extension methods for `ITestApplicationBuilder`.

### `docs/api/Microsoft.Testing.Platform.Logging/`

- `docs/api/Microsoft.Testing.Platform.Logging/ILogger-1.md` — **ILogger<TCategoryName> interface**: Represents a logger that can be used for logging messages with a specific category.
- `docs/api/Microsoft.Testing.Platform.Logging/ILogger.md` — **ILogger interface**: Represents a logger that can be used for logging messages.
- `docs/api/Microsoft.Testing.Platform.Logging/ILoggerFactory.md` — **ILoggerFactory interface**: Represents a factory for creating loggers.
- `docs/api/Microsoft.Testing.Platform.Logging/ILoggerProvider.md` — **ILoggerProvider interface**: Represents a logger provider that can be used to create loggers.
- `docs/api/Microsoft.Testing.Platform.Logging/ILoggingManager.md` — **ILoggingManager interface**: Represents a logging manager that can be used to add logger providers.
- `docs/api/Microsoft.Testing.Platform.Logging/LogLevel.md` — **LogLevel enum**: An enumeration of the supported logging levels.
- `docs/api/Microsoft.Testing.Platform.Logging/LoggerFactoryExtensions.md` — **LoggerFactoryExtensions class**: Provides extension methods for the `ILoggerFactory` interface.
- `docs/api/Microsoft.Testing.Platform.Logging/LoggingExtensions.md` — **LoggingExtensions class**: A set of extension methods for `ILogger`.

### `docs/api/Microsoft.Testing.Platform.Messages/`

- `docs/api/Microsoft.Testing.Platform.Messages/IMessageBus.md` — **IMessageBus interface**: Represents a message bus for publishing data.

### `docs/api/Microsoft.Testing.Platform.OutputDevice/`

- `docs/api/Microsoft.Testing.Platform.OutputDevice/ErrorMessageOutputDeviceData.md` — **ErrorMessageOutputDeviceData class**: Represents an error message output data.
- `docs/api/Microsoft.Testing.Platform.OutputDevice/ExceptionOutputDeviceData.md` — **ExceptionOutputDeviceData class**: Represents an exception output data.
- `docs/api/Microsoft.Testing.Platform.OutputDevice/FormattedTextOutputDeviceData.md` — **FormattedTextOutputDeviceData class**: Represents the data for a formatted text output device.
- `docs/api/Microsoft.Testing.Platform.OutputDevice/IColor.md` — **IColor interface**: Represents a color.
- `docs/api/Microsoft.Testing.Platform.OutputDevice/IOutputDevice.md` — **IOutputDevice interface**: Represents an output device.
- `docs/api/Microsoft.Testing.Platform.OutputDevice/IOutputDeviceData.md` — **IOutputDeviceData interface**: Represents the data for an output device.
- `docs/api/Microsoft.Testing.Platform.OutputDevice/ProgressMessageOutputDeviceData.md` — **ProgressMessageOutputDeviceData class**: Represents a transient message displayed in the terminal progress area.
- `docs/api/Microsoft.Testing.Platform.OutputDevice/SessionMessageOutputDeviceData.md` — **SessionMessageOutputDeviceData class**: Represents a durable session message that remains visible in the terminal output.
- `docs/api/Microsoft.Testing.Platform.OutputDevice/SystemConsoleColor.md` — **SystemConsoleColor class**: Represents a system console color.
- `docs/api/Microsoft.Testing.Platform.OutputDevice/TextOutputDeviceData.md` — **TextOutputDeviceData class**: Represents a text data for directed to the output device.
- `docs/api/Microsoft.Testing.Platform.OutputDevice/WarningMessageOutputDeviceData.md` — **WarningMessageOutputDeviceData class**: Represents a warning message output data.

### `docs/api/Microsoft.Testing.Platform.Requests/`

- `docs/api/Microsoft.Testing.Platform.Requests/CompositeTestExecutionFilter.md` — **CompositeTestExecutionFilter class**: Represents an explicit composition of test execution filters.
- `docs/api/Microsoft.Testing.Platform.Requests/DiscoverTestExecutionRequest.md` — **DiscoverTestExecutionRequest class**: Represents a request to discover test execution.
- `docs/api/Microsoft.Testing.Platform.Requests/IExecuteRequestCompletionNotifier.md` — **IExecuteRequestCompletionNotifier interface**: Interface to notify the completion of a request.
- `docs/api/Microsoft.Testing.Platform.Requests/IRequest.md` — **IRequest interface**: Represents a request interface.
- `docs/api/Microsoft.Testing.Platform.Requests/ITestExecutionFilter.md` — **ITestExecutionFilter interface**: Represents a filter for test execution.
- `docs/api/Microsoft.Testing.Platform.Requests/ITestExecutionFilterProvider.md` — **ITestExecutionFilterProvider interface**: Provides an additional constraint for a test execution request.
- `docs/api/Microsoft.Testing.Platform.Requests/NopFilter.md` — **NopFilter class**: Represents a filter that does nothing.
- `docs/api/Microsoft.Testing.Platform.Requests/RunTestExecutionRequest.md` — **RunTestExecutionRequest class**: Represents a request to run test execution.
- `docs/api/Microsoft.Testing.Platform.Requests/TestExecutionFilterContext.md` — **TestExecutionFilterContext class**: Describes the request for which a test execution filter provider is being evaluated.
- `docs/api/Microsoft.Testing.Platform.Requests/TestExecutionFilterOperator.md` — **TestExecutionFilterOperator enum**: Specifies how child test execution filters are combined.
- `docs/api/Microsoft.Testing.Platform.Requests/TestExecutionRequest.md` — **TestExecutionRequest class**: Represents a request for test execution.
- `docs/api/Microsoft.Testing.Platform.Requests/TestExecutionRequestKind.md` — **TestExecutionRequestKind enum**: Specifies the kind of test execution request.
- `docs/api/Microsoft.Testing.Platform.Requests/TestExecutionRequestOrigin.md` — **TestExecutionRequestOrigin enum**: Specifies where a test execution request originated.
- `docs/api/Microsoft.Testing.Platform.Requests/TestNodeUidListFilter.md` — **TestNodeUidListFilter class**: Represents a filter based on test node UIDs.
- `docs/api/Microsoft.Testing.Platform.Requests/TreeNodeFilter.md` — **TreeNodeFilter class**: A tree based filter for test execution.

### `docs/api/Microsoft.Testing.Platform.Services/`

- `docs/api/Microsoft.Testing.Platform.Services/ClientCapabilitiesExtensions.md` — **ClientCapabilitiesExtensions class**: Provides extension methods for `IClientCapabilities`.
- `docs/api/Microsoft.Testing.Platform.Services/CoverageMetricResult.md` — **CoverageMetricResult class**: A single correlated coverage measurement (one metric for one scope) exposed through `ITestCoverageResult`.
- `docs/api/Microsoft.Testing.Platform.Services/CoverageReportReference.md` — **CoverageReportReference class**: A pointer to a rich coverage report artifact, correlated through `ITestCoverageResult`.
- `docs/api/Microsoft.Testing.Platform.Services/CoverageScopeSummary.md` — **CoverageScopeSummary class**: All coverage metrics correlated for a single scope.
- `docs/api/Microsoft.Testing.Platform.Services/IArtifactNamingService.md` — **IArtifactNamingService interface**: Provides file-name templating for artifacts produced by the test platform and its extensions.
- `docs/api/Microsoft.Testing.Platform.Services/IClientCapabilities.md` — **IClientCapabilities interface**: Represents the capabilities declared by the client that is driving the test host.
- `docs/api/Microsoft.Testing.Platform.Services/IClientInfo.md` — **IClientInfo interface**: Represents the client information.
- `docs/api/Microsoft.Testing.Platform.Services/IPlatformInformation.md` — **IPlatformInformation interface**: Provides information about the platform.
- `docs/api/Microsoft.Testing.Platform.Services/ITestCoverageCapabilities.md` — **ITestCoverageCapabilities interface**: Describes the test-coverage messaging capabilities available in the current test application.
- `docs/api/Microsoft.Testing.Platform.Services/ITestCoverageResult.md` — **ITestCoverageResult interface**: A correlated, session-scoped view of all coverage data for consumers.
- `docs/api/Microsoft.Testing.Platform.Services/ITestSessionContext.md` — **ITestSessionContext interface**: Interface representing the context of a test session.
- `docs/api/Microsoft.Testing.Platform.Services/ServiceProviderExtensions.md` — **ServiceProviderExtensions class**: Extension methods for getting services from an `IServiceProvider`.

### `docs/api/Microsoft.Testing.Platform.TestHost/`

- `docs/api/Microsoft.Testing.Platform.TestHost/ClientInfo.md` — **ClientInfo class**: Represents client information.
- `docs/api/Microsoft.Testing.Platform.TestHost/ITestHostManager.md` — **ITestHostManager interface**: Represents the interface for managing the test host.
- `docs/api/Microsoft.Testing.Platform.TestHost/SessionUid.md` — **SessionUid struct**: Represents a unique identifier for a session.
- `docs/api/Microsoft.Testing.Platform.TestHost/TestSessionContext.md` — **TestSessionContext class**: Represents the context of a test session.
- `docs/api/Microsoft.Testing.Platform.TestHost/WellKnownClients.md` — **WellKnownClients class**: Represents well-known clients in the testing platform.

### `docs/api/Microsoft.Testing.Platform.TestHostControllers/`

- `docs/api/Microsoft.Testing.Platform.TestHostControllers/ITestHostControllersManager.md` — **ITestHostControllersManager interface**: Represents a manager for test host controllers.

### `docs/api/Microsoft.Testing.Platform.TestHostOrchestrator/`

- `docs/api/Microsoft.Testing.Platform.TestHostOrchestrator/ITestHostOrchestratorManager.md` — **ITestHostOrchestratorManager interface**: Represents a manager for test host orchestrators.

### `docs/api/Microsoft.Testing.Platform.Tools/`

- `docs/api/Microsoft.Testing.Platform.Tools/ITool.md` — **ITool interface**: Represents a non-test command that can be invoked by passing its `ITool.Name` as the first positional command-line argument.
- `docs/api/Microsoft.Testing.Platform.Tools/IToolCommandLineOptionsProvider.md` — **IToolCommandLineOptionsProvider interface**: Represents command-line options that apply to a specific `ITool`.
- `docs/api/Microsoft.Testing.Platform.Tools/IToolsManager.md` — **IToolsManager interface**: Registers tools with a test application.

### `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting.Combinatorial/`

- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting.Combinatorial/CombinatorialDataAttribute.md` — **CombinatorialDataAttribute class**: Provides every possible combination of values for the parameters of a test method.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting.Combinatorial/CombinatorialRandomDataAttribute.md` — **CombinatorialRandomDataAttribute class**: Specifies randomly generated integer values for a parameter on a combinatorial test method.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting.Combinatorial/CombinatorialRangeAttribute.md` — **CombinatorialRangeAttribute class**: Specifies a range of values for a parameter on a combinatorial test method.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting.Combinatorial/CombinatorialValuesAttribute.md` — **CombinatorialValuesAttribute class**: Specifies the values for a parameter on a combinatorial test method.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting.Combinatorial/ICombinatorialValuesProvider.md` — **ICombinatorialValuesProvider interface**: Provides values for a parameter on a combinatorial test method.

### `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting.Logging/`

- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting.Logging/Logger.LogMessageHandler.md` — **Logger.LogMessageHandler delegate**: Handler for LogMessage.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting.Logging/Logger.md` — **Logger class**: Enables users to log/write traces from unit tests for diagnostics.

### `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/`

- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/ArchitectureConditionAttribute.md` — **ArchitectureConditionAttribute class**: This attribute is used to ignore a test class or a test method based on the current process architecture.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/AssemblyCleanupAttribute.md` — **AssemblyCleanupAttribute class**: The assembly cleanup attribute.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/AssemblyFixtureProviderAttribute.md` — **AssemblyFixtureProviderAttribute class**: Indicates that the methods on the specified `AssemblyFixtureProviderAttribute.FixtureType` annotated with `AssemblyInitializeAttribute` or `AssemblyCleanupAt…
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/AssemblyInitializeAttribute.md` — **AssemblyInitializeAttribute class**: The assembly initialize attribute.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/Assert.md` — **Assert class**: A collection of helper classes to test various conditions within unit tests.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/AssertExtensions.md` — **AssertExtensions class**: Provides That extension to Assert class.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/AssertFailedException.md` — **AssertFailedException class**: AssertFailedException class.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/AssertInconclusiveException.md` — **AssertInconclusiveException class**: The assert inconclusive exception.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/CIConditionAttribute.md` — **CIConditionAttribute class**: This attribute is used to conditionally control whether a test class or a test method will run or be ignored based on whether the test is running in a CI env…
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/ClassCleanupAttribute.md` — **ClassCleanupAttribute class**: The class cleanup attribute.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/ClassInitializeAttribute.md` — **ClassInitializeAttribute class**: The class initialize attribute.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/CollectionAssert.md` — **CollectionAssert class**: A collection of helper classes to test various conditions associated with collections within unit tests.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/ConditionBaseAttribute.md` — **ConditionBaseAttribute class**: This attribute is used to conditionally control whether a test class or a test method will run or be ignored, based on a condition and using an optional mess…
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/ConditionMode.md` — **ConditionMode enum**: An enumeration used with `ConditionBaseAttribute` to control whether the condition is reversed.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/DataAccessMethod.md` — **DataAccessMethod enum**: Enumeration for how we access data rows in data driven testing.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/DataRowAttribute.md` — **DataRowAttribute class**: Attribute to define in-line data for a test method.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/DataSourceAttribute.md` — **DataSourceAttribute class**: Specifies connection string, table name and row access method for data driven testing.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/DelayBackoffType.md` — **DelayBackoffType enum**: Specifies a backoff type for the delay between retries.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/DependsOnAttribute.md` — **DependsOnAttribute class**: Declares that a test (or every test of a test class) must not start until one or more other tests have finished, forming a dependency graph that the in-assem…
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/DeploymentItemAttribute.md` — **DeploymentItemAttribute class**: Used to specify a deployment item (file or directory) for per-test deployment.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/DescriptionAttribute.md` — **DescriptionAttribute class**: Description of the test.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/DiscoverInternalsAttribute.md` — **DiscoverInternalsAttribute class**: The presence of this attribute in a test assembly causes MSTest to discover test classes (i.e. classes having the "TestClass" attribute) and test methods (i.…
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/DoNotParallelizeAttribute.md` — **DoNotParallelizeAttribute class**: Excludes a test, test class, or test assembly from in-assembly parallelization.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/DynamicDataAttribute.md` — **DynamicDataAttribute class**: Attribute to define dynamic data for a test method.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/DynamicDataSourceType.md` — **DynamicDataSourceType enum**: Enum to specify whether the data is stored as property, in method, or in field.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/ExecutableConditionAttribute.md` — **ExecutableConditionAttribute class**: This attribute is used to conditionally control whether a test class or a test method will run or be ignored, based on whether a given executable (tool) is a…
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/ExecutionScope.md` — **ExecutionScope enum**: Parallel execution mode.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/GitHubWorkItemAttribute.md` — **GitHubWorkItemAttribute class**: GitHubWorkItem attribute; used to specify a GitHub issue associated with this test.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/GlobalTestCleanupAttribute.md` — **GlobalTestCleanupAttribute class**: A global test cleanup attribute that applies to every test method in the assembly.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/GlobalTestInitializeAttribute.md` — **GlobalTestInitializeAttribute class**: A global test initialize attribute that applies to every test method in the assembly.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/ITestDataSource.md` — **ITestDataSource interface**: Test data source for data driven tests.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/ITestDataSourceEmptyDataSourceExceptionInfo.md` — **ITestDataSourceEmptyDataSourceExceptionInfo interface**: Optional capability for a custom `ITestDataSource` to provide richer information when the data source returns no rows.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/ITestDataSourceIgnoreCapability.md` — **ITestDataSourceIgnoreCapability interface**: Specifies the capability of a test data source to be ignored and define the ignore reason.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/ITestFilter.md` — **ITestFilter interface**: Implemented by a user-supplied test filter that decides, on a per-test basis, whether the test should run, be silently dropped, or be reported as skipped.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/ITestMethod.md` — **ITestMethod interface**: TestMethod for execution.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/ITestRunInfo.md` — **ITestRunInfo interface**: Read-only ambient information about the current test run.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/IgnoreAttribute.md` — **IgnoreAttribute class**: This attribute is used to ignore a test class or a test method, with an optional message.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/InheritanceBehavior.md` — **InheritanceBehavior enum**: Enumeration for inheritance behavior, that can be used with both the `ClassInitializeAttribute` class and `ClassCleanupAttribute` class.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/MemberConditionAttribute.md` — **MemberConditionAttribute class**: Conditionally runs or ignores a test class or test method based on the value of one or more `static` `Boolean` members (property, field, or parameterless met…
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/MessageLevel.md` — **MessageLevel enum**: Specifies the severity level of messages displayed using the `TestContext.DisplayMessage(MessageLevel,String)` API.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/OSConditionAttribute.md` — **OSConditionAttribute class**: This attribute is used to ignore a test class or a test method, with an optional message.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/OperatingSystems.md` — **OperatingSystems enum**: An enum that is used with `OSConditionAttribute` to control which operating systems a test method or test class supports or doesn't support.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/OwnerAttribute.md` — **OwnerAttribute class**: Test Owner.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/ParallelizeAttribute.md` — **ParallelizeAttribute class**: Specification for parallelization level for a test run.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/PlannedTest.md` — **PlannedTest class**: Represents a single test that is planned to run (i.e. has been discovered and passed the active filter) in the current test run.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/PriorityAttribute.md` — **PriorityAttribute class**: Priority attribute; used to specify the priority of a unit test.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/ResourceAccessMode.md` — **ResourceAccessMode enum**: Specifies how a test accesses a resource declared with `ResourceLockAttribute`.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/ResourceLockAttribute.md` — **ResourceLockAttribute class**: Declares that a test or test class contends on a named shared resource, so that the in-assembly parallel scheduler serializes it only against other tests tha…
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/RetryAttribute.md` — **RetryAttribute class**: This attribute is used to set a retry count on a test method in case of failure.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/RetryBaseAttribute.md` — **RetryBaseAttribute class**: An abstract attribute that controls retrying a test method if it failed.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/RetryContext.md` — **RetryContext struct**: Represents the context for a test retry.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/RetryResult.md` — **RetryResult class**: The result of a test retry.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/STATestClassAttribute.md` — **STATestClassAttribute class**: The test class attribute.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/STATestMethodAttribute.md` — **STATestMethodAttribute class**: The test class attribute.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/SequenceOrder.md` — **SequenceOrder enum**: Specifies whether sequence elements must appear in the same order, or in any order, when comparing collections with `Assert.AreSequenceEqual(IEnumerable<T0>,…
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/StringAssert.md` — **StringAssert class**: The string assert.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/TestArchitectures.md` — **TestArchitectures enum**: An enum that is used with `ArchitectureConditionAttribute` to control which process architectures a test method or test class supports or doesn't support.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/TestCategoryAttribute.md` — **TestCategoryAttribute class**: TestCategory attribute; used to specify the category of a unit test.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/TestCategoryBaseAttribute.md` — **TestCategoryBaseAttribute class**: Base class for the "Category" attribute.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/TestClassAttribute.md` — **TestClassAttribute class**: This attribute is used to mark test classes.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/TestCleanupAttribute.md` — **TestCleanupAttribute class**: The test cleanup attribute marks methods that are executed after every test marked with a `TestMethodAttribute`.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/TestContext.md` — **TestContext class**: Used to store information that is provided to unit tests.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/TestDataRow-1.md` — **TestDataRow<T> class**: When this type is returned from `ITestDataSource.GetData(MethodInfo)` (for example, through `DynamicDataAttribute`), it determines information related to the…
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/TestDataSourceOptionsAttribute.md` — **TestDataSourceOptionsAttribute class**: Specifies options for all `ITestDataSource` of the current assembly.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/TestDataSourceUnfoldingStrategy.md` — **TestDataSourceUnfoldingStrategy enum**: Specifies how parameterized tests should be executed, either as individual test cases for each data row or as a single test case.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/TestFilterAction.md` — **TestFilterAction enum**: Indicates how the MSTest adapter should treat a test for which an `ITestFilter` returned a particular `TestFilterResult`.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/TestFilterContext.md` — **TestFilterContext class**: Snapshot of the metadata MSTest exposes to an `ITestFilter` for a single test under consideration.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/TestFilterProviderAttribute-1.md` — **TestFilterProviderAttribute<TFilter> class**: Strongly typed variant of `TestFilterProviderAttribute` that registers `TFilter` as the `ITestFilter` implementation the MSTest adapter invokes for every tes…
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/TestFilterProviderAttribute.md` — **TestFilterProviderAttribute class**: Registers a user-supplied `ITestFilter` implementation that the MSTest adapter invokes for every test it is about to run, after any command-line filter (`--f…
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/TestFilterResult.md` — **TestFilterResult struct**: The decision returned by an `ITestFilter` for a single test.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/TestInitializeAttribute.md` — **TestInitializeAttribute class**: The test initialize attribute.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/TestMethodAttribute.md` — **TestMethodAttribute class**: This attribute is used to mark test methods.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/TestPropertyAttribute.md` — **TestPropertyAttribute class**: The test property attribute.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/TestResult.md` — **TestResult class**: TestResult object to be returned to adapter.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/TestRun.md` — **TestRun class**: Provides ambient access to information about the currently-executing test run.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/TimeoutAttribute.md` — **TimeoutAttribute class**: Timeout attribute; used to specify the timeout of a unit test.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/UnitTestAssertException.md` — **UnitTestAssertException class**: Base class for Framework Exceptions.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/UnitTestOutcome.md` — **UnitTestOutcome enum**: unit test outcomes.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/WellKnownResources.md` — **WellKnownResources class**: Well-known resource keys for common process-global state, for use with `ResourceLockAttribute`.
- `docs/api/Microsoft.VisualStudio.TestTools.UnitTesting/WorkItemAttribute.md` — **WorkItemAttribute class**: WorkItem attribute; used to specify a work item associated with this test.
