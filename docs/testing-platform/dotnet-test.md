# Testing with 'dotnet test'

The `dotnet test` command runs test applications built with MTP in *MTP* mode, introduced with the .NET 10 SDK.

> [!TIP]
> For CLI reference, see [dotnet test](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-test).

## MTP mode of `dotnet test`

To enable this mode, add the following configuration to your `global.json` file:

```json
{
    "test": {
        "runner": "Microsoft.Testing.Platform"
    }
}
```

Starting with .NET 11 Preview 6, you can instead set the `DOTNET_TEST_RUNNER` environment variable to `Microsoft.Testing.Platform`. A recognized environment variable value overrides `global.json` for the current process. For accepted values and precedence, see [Choose a test runner](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-test#choose-a-test-runner).

> [!IMPORTANT]
> The `dotnet test` experience for MTP is only supported in `Microsoft.Testing.Platform` version 1.7 and later.

Since this mode is specifically designed for MTP, neither `TestingPlatformDotnetTestSupport` nor the additional `--` are required.

> [!IMPORTANT]
> This mode is only compatible with MTP version 1.7.0 and later.
>
> [!TIP]
> You can customize the command-line arguments of your test application via `TestingPlatformCommandLineArguments` MSBuild property:
> ```xml
> <PropertyGroup>
>   ...
>   <TestingPlatformCommandLineArguments>--minimum-expected-tests 10</TestingPlatformCommandLineArguments>
> </PropertyGroup>
> ```

## Migrate to MTP mode of `dotnet test`

1. Add `test` section to your `global.json` file, as shown above.
1. Remove `TestingPlatformDotnetTestSupport` MSBuild property, as it's no longer required.
1. Remove `TestingPlatformCaptureOutput` and `TestingPlatformShowTestsFailure` MSBuild properties, as they are no longer used by the new `dotnet test`.
1. Treat the extra `--` as optional. For example, `dotnet test -- --report-trx` can become `dotnet test --report-trx`. Keep the separator to forward test application arguments unambiguously. Neither syntax installs the required `Microsoft.Testing.Extensions.TrxReport` extension.
1. If passing a specific solution (or directory containing solution), for example, `dotnet test MySolution.sln`, this should become `dotnet test --solution MySolution.sln`.
1. If passing a specific project (or directory containing project), for example, `dotnet test MyProject.csproj`, this should become `dotnet test --project MyProject.csproj`.
1. If passing a specific dll, for example, `dotnet test path/to/UnitTests.dll`, this should become `dotnet test --test-modules path/to/UnitTests.dll`. Note that `--test-modules` also supports globbing.

> [!TIP]
> Even though `--` is no longer required in MTP mode, you can still use it to mark where test application arguments begin. The separator avoids a parser quirk where unrecognized arguments change meaning when interleaved with options that `dotnet test` understands. The separator also protects your scripts if `dotnet test` later starts recognizing one of those tokens. For more information, see [Forward arguments to the test application](dotnet-test-cli.md#forward-arguments-to-the-test-application).

## Solutions with mixed test frameworks or extensions

When a solution contains test projects that use different test frameworks (for example, MSTest and xUnit.net) or different sets of extensions, running `dotnet test` with framework-specific or extension-specific command-line options can fail. Options that are valid for one project are unrecognized by another, causing exit code 5 (invalid command-line arguments). For example:

- xUnit.net uses `--filter-trait` while MSTest uses `--filter`, and each framework rejects the other's options.
- A project that references `Microsoft.Testing.Extensions.HangDump` accepts `--hangdump`, but a project without that extension fails on the same option.

Use the [`TestingPlatformCommandLineArguments`](https://learn.microsoft.com/en-us/dotnet/core/project-sdk/msbuild-props#testingplatformcommandlinearguments) MSBuild property with conditions to pass arguments only to the projects that understand them.

### Use MSBuild conditions to route arguments

Define custom MSBuild properties for the framework-specific arguments, and conditionally append them to `TestingPlatformCommandLineArguments` in a `Directory.Build.props` or `Directory.Build.targets` file. Use a condition that checks for a property set by the test framework's SDK or NuGet package to determine which framework each project uses.

The following example shows a `Directory.Build.props` file for a solution that mixes MSTest (with MSTest.Sdk) and xUnit.net projects:

```xml
<PropertyGroup>
  <TestingPlatformCommandLineArguments
    Condition="'$(UsingMSTestSdk)' == 'true'"
    >$(TestingPlatformCommandLineArguments) $(MSTestSpecificArgs)</TestingPlatformCommandLineArguments>
  <TestingPlatformCommandLineArguments
    Condition="'$(UsingMSTestSdk)' != 'true'"
    >$(TestingPlatformCommandLineArguments) $(XUnitSpecificArgs)</TestingPlatformCommandLineArguments>
</PropertyGroup>
```

> [!NOTE]
> `UsingMSTestSdk` is a property defined by `MSTest.Sdk`. If your MSTest projects don't use `MSTest.Sdk`, use a different condition. Check whether your test framework's SDK or NuGet package already sets a property you can use. If it doesn't, define your own property in each project and condition on that property instead (in this case, use Directory.Build.targets instead).

With this configuration in place, you can pass framework-specific arguments from the command line using MSBuild properties:

```dotnetcli
dotnet test -p:MSTestSpecificArgs="--filter FullyQualifiedName~IntegrationTests" -p:XUnitSpecificArgs="--filter-trait Category=Integration"
```

Each test project receives only the arguments relevant to its framework, and the other framework's arguments are never passed.

> [!TIP]
> For arguments that every targeted project recognizes, set them directly in `TestingPlatformCommandLineArguments` without a condition. For example, all projects recognize `--ignore-exit-code 8`. You can pass `--report-trx` globally only when every targeted project registers `Microsoft.Testing.Extensions.TrxReport`.

The same pattern applies when only some test projects in a solution reference a particular extension. For example, if only certain projects reference `Microsoft.Testing.Extensions.HangDump`, passing `--hangdump` globally causes the other projects to fail with an unrecognized option error. Use the same conditional approach to route extension-specific arguments only to the projects that have the extension.
