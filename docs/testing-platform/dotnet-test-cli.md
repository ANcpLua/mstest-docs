# dotnet test with Microsoft.Testing.Platform (MTP)

**This article applies to:** ✔️ .NET 10 SDK and later versions

## Name

`dotnet test` - .NET test driver used to execute unit tests with MTP.

## Synopsis

```dotnetcli
dotnet test
    [--project <PROJECT_PATH>]
    [--solution <SOLUTION_PATH>]
    [--test-modules <EXPRESSION>]
    [--root-directory <ROOT_PATH>]
    [--max-parallel-test-modules <NUMBER>]
    [--config-file <CONFIG_FILE>]
    [--results-directory <RESULTS_DIRECTORY>]
    [--diagnostic-output-directory <DIAGNOSTIC_OUTPUT_DIRECTORY>]
    [--minimum-expected-tests <NUMBER>]
    [-e|--environment <NAME="VALUE">]
    [-a|--arch <ARCHITECTURE>]
    [-c|--configuration <CONFIGURATION>]
    [-f|--framework <FRAMEWORK>]
    [--os <OS>]
    [-r|--runtime <RUNTIME_IDENTIFIER>]
    [-v|--verbosity <LEVEL>]
    [--no-build]
    [--no-restore]
    [--no-ansi]
    [--no-progress]
    [--output <VERBOSITY_LEVEL>]
    [--show-test-results <OUTCOME>]
    [--list-tests]
    [--no-launch-profile]
    [--no-launch-profile-arguments]
    [<args>...]

dotnet test -h|--help
```

## Description

The test-related arguments are no longer fixed, as they are tied to the registered extensions in the test project(s). Moreover, MTP supports a globbing filter when running tests. For more information, see [MTP](intro.md).

> [!IMPORTANT]
> Extension-specific options aren't built into MTP. Each targeted test application must register the extension that provides an option. Add the extension's NuGet package directly, or use a test SDK configuration or profile that includes the package. Otherwise, the test run fails with exit code 5 because the option is unrecognized. Run `dotnet test --help` to see the options available to the selected test applications, and see [Extension options by scenario](cli-options.md#extension-options-by-scenario) to find the package for an option.

> [!WARNING]
> When MTP is opted in via `global.json`, `dotnet test` expects all test projects to use MTP.

### Version requirements

The MTP mode of `dotnet test` requires the .NET 10 SDK and MTP 1.7 or later. Options added after .NET 10 have individual SDK version requirements in the following sections. Some options also require a newer MTP package because the SDK coordinates the complete run while each test application implements the corresponding capability.

## Implicit restore

You don't have to run [`dotnet restore`](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-restore) because it's run implicitly by all commands that require a restore to occur, such as `dotnet new`, `dotnet build`, `dotnet run`, `dotnet test`, `dotnet publish`, and `dotnet pack`. To disable implicit restore, use the `--no-restore` option.

The `dotnet restore` command is still useful in certain scenarios where explicitly restoring makes sense, such as [continuous integration builds in Azure DevOps Services](https://learn.microsoft.com/en-us/azure/devops/build-release/apps/aspnet/build-aspnet-core) or in build systems that need to explicitly control when the restore occurs.

For information about how to manage NuGet feeds, see the [`dotnet restore` documentation](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-restore).

> [!IMPORTANT]
> When you run a project or solution with `--no-restore`, keep both the restore-generated project state in the `obj` folder and the matching global packages folder available. Test framework and platform package imports set the MSBuild properties that `dotnet test` uses to identify MTP test applications. The `--no-build` option also implies `--no-restore`. If the test environment contains built test applications but not the project restore state, use `--test-modules` instead. For more information, see [`No test projects were found`](troubleshooting.md#dotnet-test-reports-no-test-projects-were-found).

## Options

> [!NOTE]
> You can use only one of the following options at a time: `--project`, `--solution`, or `--test-modules`. These options can't be combined.
> In addition, when you use `--test-modules`, you can't specify `--arch`, `--configuration`, `--device`, `--framework`, `--list-devices`, `--os`, `--runtime`, or `--use-current-runtime`. These options require project evaluation or aren't relevant for an already-built module.

- **`--project <PROJECT_PATH>`**

  Specifies the path of the project file to run (folder name or full path). If not specified, it defaults to the current directory.

- **`--solution <SOLUTION_PATH>`**

  Specifies the path of the solution file to run (folder name or full path). If not specified, it defaults to the current directory.

- **`--test-modules <EXPRESSION>`**

  Filters test modules using file globbing. Only tests belonging to those test modules run. Because this option doesn't evaluate projects, use it to run already-built test applications when project restore state isn't available.

- **`--root-directory <ROOT_PATH>`**

  Specifies the root directory of the `--test-modules` option. It can only be used with the `--test-modules` option.

- **`--max-parallel-test-modules <NUMBER>`**

  Specifies the maximum number of test modules that can run in parallel. The default is [`Environment.ProcessorCount`](https://learn.microsoft.com/en-us/dotnet/api/system.environment.processorcount).

- **`--config-file <CONFIG_FILE>`**

  Specifies the configuration file to use for test execution. If a relative path is provided, it's converted to an absolute path based on the current directory. For more information about the configuration file settings, see [testconfig.json](config.md#testconfigjson).

- **`--results-directory <RESULTS_DIRECTORY>`**

  Specifies the directory where test results are stored. If the directory doesn't exist, it's created. If a relative path is provided, it's converted to an absolute path based on the current directory.

- **`--diagnostic-output-directory <DIAGNOSTIC_OUTPUT_DIRECTORY>`**

  Specifies the directory where diagnostic output is stored. If the directory doesn't exist, it's created. If a relative path is provided, it's converted to an absolute path based on the current directory.

- **`--minimum-expected-tests <NUMBER>`**

  Specifies a positive minimum number of tests for the whole run. If the aggregated test count is less than the specified minimum, the test run fails with exit code 9. The global count includes skipped tests. For more information about exit codes, see [MTP exit codes](troubleshooting.md#exit-codes).

  Because this option appears before `--`, it's a global (whole-run) option. To require a minimum for each test module instead, pass the option after `--` so that it's forwarded to every test module. For more information, see [Whole-run and per-module minimums](#whole-run-and-per-module-minimums).

  > [!NOTE]
  > The global minimum requires the .NET 10 SDK (10.0.100) or a later version.

- **`-e|--environment <NAME="VALUE">`**

  Sets an environment variable for the test process. Specify the option multiple times to set multiple variables. Command-line values override values from a launch profile.

  Use .NET SDK 10.0.110 or later when no launch profile exists or when you specify `--no-launch-profile`; earlier .NET 10 SDK versions can ignore the variables in those cases.

- **`-a|--arch <ARCHITECTURE>`**

Specifies the target architecture. This is a shorthand syntax for setting the [Runtime Identifier (RID)](https://learn.microsoft.com/en-us/dotnet/core/rid-catalog), where the provided value is combined with the default RID. For example, on a `win-x64` machine, specifying `--arch x86` sets the RID to `win-x86`. If you use this option, don't use the `-r|--runtime` option. Available since .NET 6 Preview 7.

- **`-c|--configuration <CONFIGURATION>`**

Defines the build configuration. The default for most projects is `Debug`, but you can override the build configuration settings in your project.

- **`-f|--framework <FRAMEWORK>`**

  The [target framework moniker (TFM)](https://learn.microsoft.com/en-us/dotnet/standard/frameworks) of the target framework to run tests for. The target framework must also be specified in the project file.

- **`--os <OS>`**

Specifies the target operating system (OS). This is a shorthand syntax for setting the [Runtime Identifier (RID)](https://learn.microsoft.com/en-us/dotnet/core/rid-catalog), where the provided value is combined with the default RID. For example, on a `win-x64` machine, specifying `--os linux` sets the RID to `linux-x64`. If you use this option, don't use the `-r|--runtime` option. Available since .NET 6.

- **`-r|--runtime <RUNTIME_IDENTIFIER>`**

  The target runtime to test for.

  Short form `-r` available starting in .NET SDK 7.

  > [!NOTE]
  > Running tests for a solution with a global `RuntimeIdentifier` property (explicitly or via `--arch`, `--runtime`, or `--os`) isn't supported. Set `RuntimeIdentifier` on an individual project level instead.

- **`-v|--verbosity <LEVEL>`**

Sets the verbosity level of the command. Allowed values are `q[uiet]`, `m[inimal]`, `n[ormal]`, `d[etailed]`, and `diag[nostic]`. For more information, see [`LoggerVerbosity`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.build.framework.loggerverbosity).

- **`--no-build`**

  Specifies that the test project isn't built before being run. It also implicitly sets the `--no-restore` flag.

- **`--no-restore`**

  Specifies that an implicit restore isn't executed when running the command.

- **`--no-ansi`**

  Disables outputting ANSI escape characters to screen.

- **`--no-progress`**

  Disables reporting progress to screen.

- **`--output <VERBOSITY_LEVEL>`**

  Specifies the output verbosity for test results. Valid values are `Minimal`, `Normal`, and `Detailed`. The default is `Normal`. `Minimal` requires MTP 2.4.

- **`--show-test-results <OUTCOME>`**

  Selects result blocks by outcome. In MTP 2.4, use `passed`, `failed`, `skipped`, `all`, or `none`. The `failed` value also includes errors, timeouts, and cancellations.

  Combine `passed`, `failed`, and `skipped` with commas, spaces, or repeated `--show-test-results` options. Don't combine `all` or `none` with another value. This explicit option overrides the `--output` preset regardless of option order.

- **`--list-tests`**

  Lists discovered tests without executing them. Omit the value or specify `text` for human-readable output.

- **`--no-launch-profile`**

  Don't attempt to use launchSettings.json to configure the application. By default, `launchSettings.json` is used, which can apply environment variables and command-line arguments to the test executable.

- **`--no-launch-profile-arguments`**

  Don't use arguments specified by `commandLineArgs` in launch profile to run the application.

- **`--property:<NAME>=<VALUE>`**

  Sets one or more MSBuild properties. Specify multiple properties by repeating the option:

  ```dotnetcli
  --property:<NAME1>=<VALUE1> --property:<NAME2>=<VALUE2>
  ```

  The short form `-p` can be used for `--property`. The same applies for `/property:property=value` and its short form is `/p`.
  More information about the available arguments can be found in [the dotnet msbuild documentation](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-msbuild).

- **`-?|-h|--help`**

Prints out a description of how to use the command.

- **`args`**

  Specifies extra arguments to pass to the test application(s). Use a space to separate multiple arguments. For more information and examples on what to pass, see [MTP overview](intro.md) and [MTP features](features/overview.md).

  > [!TIP]
  > To specify extra arguments for specific projects, use the `TestingPlatformCommandLineArguments` MSBuild property. This property is especially useful when your solution mixes test frameworks (for example, MSTest and xUnit.net) or when only some projects reference a particular extension. For more information, see [Solutions with mixed test frameworks or extensions](dotnet-test.md#solutions-with-mixed-test-frameworks-or-extensions).

> [!NOTE]
> To enable trace logging to a file, use the environment variable `DOTNET_CLI_TEST_TRACEFILE` to provide the path to the trace file.

## Output and cancellation behavior

Live test-host output requires an MTP host that supports protocol 1.1 or later. Older hosts keep output captured and replay it for a failed module.

## Forward arguments to the test application

`dotnet test` forwards any token it doesn't recognize to the test application. When a recognized option appears between an unrecognized option name and its value, removing the recognized option can change how the leftover tokens bind to options in the test application. To avoid this ambiguity, place test application arguments after a literal `--`:

```dotnetcli
dotnet test --results-directory TestResults -- --report-trx --report-trx-filename A.trx
```

The preceding example requires the [`Microsoft.Testing.Extensions.TrxReport`](https://www.nuget.org/packages/Microsoft.Testing.Extensions.TrxReport) package, either as a direct package reference or through a test SDK configuration that includes it.

The same parser behavior applies to `dotnet run` and `dotnet build`. For a detailed example, see [Forward arguments to the application](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-run#forward-arguments-to-the-application) in the `dotnet run` reference.

## Whole-run and per-module minimums

For `--minimum-expected-tests`, the `--` separator determines the option's scope:

- Arguments *before* `--` are global. The `dotnet test` orchestrator interprets them for the whole run.
- Arguments *after* `--` are local. `dotnet test` forwards them to each test module, so each module applies them independently.

Because `--minimum-expected-tests` is available in both scopes, you can require a minimum for the whole run, for each module, or both:

```dotnetcli
dotnet test --minimum-expected-tests 5 -- --minimum-expected-tests 2
```

The preceding command requires at least 5 tests across the whole run and at least 2 tests in each test module.

The two scopes count skipped tests differently:

| Scope | Do skipped tests count toward the minimum? |
| --- | --- |
| Global | Yes. The `dotnet test` aggregated total includes skipped tests. |
| Per module | No. MTP excludes skipped tests from the number of tests that ran. |

MTP 4.3.0 and later versions provide `--zero-tests-policy <allow-skipped|strict>`. The default value, `allow-skipped`, lets an all-skipped module succeed. The `strict` value treats skipped tests as not run, so an all-skipped module exits with code 8. Pass the option after `--` to forward it to each test module:

```dotnetcli
dotnet test -- --zero-tests-policy strict
```

When you specify `--minimum-expected-tests` and the minimum isn't met, the run fails with exit code 9 (`MinimumExpectedTestsPolicyViolation`). This code is distinct from 8 so that a stricter global or per-module minimum isn't confused with an empty module. For a per-module minimum to return code 9 when the module runs zero tests, the test module must use MTP 4.4.0 or a later version.

> [!NOTE]
> `--minimum-expected-tests 0` is invalid. To suppress the zero-tests exit code, use `--ignore-exit-code 8`.

Pass execution-mode options such as `--help` and `--list-tests` directly to `dotnet test`.

## Examples

- Run the tests in the project or solution in the current directory:

  ```dotnetcli
  dotnet test
  ```

- Run the tests in the `TestProject` project:

  ```dotnetcli
  dotnet test --project ./TestProject/TestProject.csproj
  ```

- Run the tests in the `TestProjects` solution:

  ```dotnetcli
  dotnet test --solution ./TestProjects/TestProjects.sln
  ```

- Run the tests using `TestProject.dll` assembly:

  ```dotnetcli
  dotnet test --test-modules "**/bin/**/Debug/net10.0/TestProject.dll"
  ```

- Run the tests using `TestProject.dll` assembly with the root directory:

  ```dotnetcli
  dotnet test --test-modules "**/bin/**/Debug/net10.0/TestProject.dll" --root-directory "c:\code"
  ```

- Run the tests in the current directory with the Microsoft Code Coverage extension. The test application must reference [`Microsoft.Testing.Extensions.CodeCoverage`](https://www.nuget.org/packages/Microsoft.Testing.Extensions.CodeCoverage), either directly or through a test SDK configuration that includes it:

  ```dotnetcli
  dotnet test --coverage
  ```

- Run the tests and store results in a specific directory:

  ```dotnetcli
  dotnet test --results-directory ./TestResults
  ```

- Run the tests with diagnostic output in a specific directory:

  ```dotnetcli
  dotnet test --diagnostic-output-directory ./Diagnostics
  ```

- Run the tests ensuring at least 10 tests are executed:

  ```dotnetcli
  dotnet test --minimum-expected-tests 10
  ```

- Require at least 5 tests across the whole run and at least 2 tests in each test module:

  ```dotnetcli
  dotnet test --minimum-expected-tests 5 -- --minimum-expected-tests 2
  ```

- Run the tests in the `TestProject` project, providing the `-bl` (binary log) argument to `msbuild`:

  ```dotnetcli
  dotnet test --project ./TestProject/TestProject.csproj -bl
  ```

- Run the tests in the `TestProject` project, setting the MSBuild `DefineConstants` property to `DEV`:

  ```dotnetcli
  dotnet test --project ./TestProject/TestProject.csproj -p:DefineConstants="DEV"
  ```

## See also

- [Frameworks and Targets](https://learn.microsoft.com/en-us/dotnet/standard/frameworks)
- [.NET Runtime Identifier (RID) catalog](https://learn.microsoft.com/en-us/dotnet/core/rid-catalog)
- [MTP](intro.md)
- [MTP features](features/overview.md)
- [MTP CLI options](cli-options.md)
- [Run and debug MTP tests](run-and-debug.md)
- [Run tests with MSTest](../mstest/running-tests/overview.md)
- [MSTest SDK configuration](../mstest/running-tests/sdk.md)
- [dotnet test](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-test)
