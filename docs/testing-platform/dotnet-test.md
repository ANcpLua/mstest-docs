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

> [!IMPORTANT]
> The `dotnet test` experience for MTP is only supported in `Microsoft.Testing.Platform` version 1.7 and later.

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
