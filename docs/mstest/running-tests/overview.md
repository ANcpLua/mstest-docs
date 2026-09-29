# Run tests with MSTest

There are several ways to run MSTest tests depending on your needs. You can run tests from an IDE (for example, Visual Studio, Visual Studio Code, or JetBrains Rider), or from the command line, or from a CI service (such as GitHub Actions or Azure DevOps).

## MSTest runner

MSTest runs tests with [Microsoft.Testing.Platform (MTP)](../../testing-platform/intro.md). The support for MTP is powered by the MSTest runner, which can run tests in all contexts (for example, continuous integration (CI) pipelines, CLI, Visual Studio Test Explorer, and VS Code Text Explorer). The MSTest runner is embedded directly in your MSTest test projects, and there are no other app dependencies needed to run your tests. However, you can still run your tests using `dotnet test`.

The MSTest runner is open source and builds on the [MTP](../../testing-platform/intro.md) library. You can find `Microsoft.Testing.Platform` code in the [microsoft/testfx](https://github.com/microsoft/testfx/tree/main/src/Platform/Microsoft.Testing.Platform) GitHub repository. The MSTest runner comes bundled with `MSTest in 3.2.0` or newer.

With the .NET 10 SDK and later versions, select the dedicated MTP mode of `dotnet test` in `global.json`.

## Enable MTP in an MSTest project

Use [MSTest SDK](sdk.md) to greatly simplify your project configuration, version management, and alignment of MTP and its extensions.

`MSTest.Sdk` replaces `Microsoft.NET.Sdk` as the project SDK, and MTP is enabled by default:

```xml
<Project Sdk="MSTest.Sdk/4.4.1">

  <PropertyGroup>
    <TargetFramework>net10.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>

</Project>
```

> [!NOTE]
> `MSTest.Sdk` works only when your project can use `Microsoft.NET.Sdk` as its base SDK. If your project requires a different SDK, don't replace the `<Project Sdk="...">` value with `MSTest.Sdk`.
>
> For example, some ASP.NET Core integration test projects use `Microsoft.NET.Sdk.Web`. `MSTest.Sdk` derives from `Microsoft.NET.Sdk`, so it doesn't import the ASP.NET Core SDK targets that `Microsoft.NET.Sdk.Web` provides.

You can also configure MSTest manually instead of using `MSTest.Sdk`. Manual configuration is required when your project needs a different top-level SDK (for example, `Microsoft.NET.Sdk.Web`), but you can also choose it with the standard `Microsoft.NET.Sdk`. Add the `EnableMSTestRunner` property and set `OutputType` to `Exe` in your project file. Then add the MSTest references that your project requires. Ensure that you're using MSTest 3.2.0 or newer, and update to the latest MSTest version available.

Consider the following example project file:

```xml
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <!-- Enable Microsoft.Testing.Platform, this is an opt-in feature -->
    <EnableMSTestRunner>true</EnableMSTestRunner>

    <OutputType>Exe</OutputType>

    <TargetFramework>net10.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>

  <ItemGroup>
    <!--
      MSTest meta package is the recommended way to reference MSTest.
      It's equivalent to referencing:
          MSTest.TestAdapter
          MSTest.TestFramework
          MSTest.Analyzers
      Starting with 3.8, it also includes:
          Microsoft.Testing.Extensions.TrxReport
          Microsoft.Testing.Extensions.CodeCoverage
    -->
    <PackageReference Include="MSTest" Version="4.4.1" />
  </ItemGroup>

</Project>
```

## Configurations and filters

### .runsettings

MTP supports the runsettings through the command-line option `--settings`. For the full list of supported MSTest entries, see [Configure MSTest: Runsettings](configure.md#runsettings). The following commands show various usage examples.

Using `dotnet run`:

```dotnetcli
dotnet run --project Contoso.MyTests -- --settings config.runsettings
```

Using `dotnet exec`:

```dotnetcli
dotnet exec Contoso.MyTests.dll --settings config.runsettings
```

-or-

```dotnetcli
dotnet Contoso.MyTests.dll --settings config.runsettings
```

Using the executable:

```dotnetcli
Contoso.MyTests.exe --settings config.runsettings
```

### Tests filter

You can provide the tests [filter](filter.md) seamlessly using the command line option `--filter`. The following commands show some examples.

Using `dotnet run`:

```dotnetcli
dotnet run --project Contoso.MyTests -- --filter "FullyQualifiedName~UnitTest1|TestCategory=CategoryA"
```

Using `dotnet exec`:

```dotnetcli
dotnet exec Contoso.MyTests.dll --filter "FullyQualifiedName~UnitTest1|TestCategory=CategoryA"
```

-or-

```dotnetcli
dotnet Contoso.MyTests.dll --filter "FullyQualifiedName~UnitTest1|TestCategory=CategoryA"
```

Using the executable:

```dotnetcli
Contoso.MyTests.exe --filter "FullyQualifiedName~UnitTest1|TestCategory=CategoryA"
```

## See also

- [Testing with `dotnet test`](../../testing-platform/dotnet-test.md)
- [`dotnet test` with MTP](../../testing-platform/dotnet-test-cli.md)
- [MTP CLI options reference](../../testing-platform/cli-options.md)
- [Filter tests](filter.md)
- [Order unit tests](../writing-tests/ordering.md)
