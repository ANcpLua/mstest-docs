# MSTest overview

MSTest, Microsoft Testing Framework, is a fully supported, open-source, and cross-platform test framework for .NET applications. It allows you to write and execute tests, and provides test suites with integration to Visual Studio and Visual Studio Code Test Explorers, the .NET CLI, and many CI pipelines.

MSTest is hosted on [GitHub](https://github.com/microsoft/testfx) and works with all supported .NET targets.

## Key features

MSTest provides comprehensive testing capabilities:

- **[Data-driven testing](writing-tests/data-driven.md)**: Run tests with multiple inputs using `DataRow`, `CombinatorialData`, `DynamicData`, and external data sources.
- **[Test lifecycle management](writing-tests/lifecycle.md)**: Setup and cleanup at assembly, class, and test levels.
- **[Parallel execution](writing-tests/controlling-execution.md#parallelization-attributes)**: Run tests concurrently to reduce execution time.
- **[Test organization](writing-tests/organizing.md)**: Categorize, prioritize, and filter tests with metadata attributes.
- **[Code analyzers](analyzers/overview.md)**: Detect common issues and enforce best practices at compile time.
- **[Assertions](writing-tests/assertions.md)**: Comprehensive assertion methods for validating results.

## Supported platforms

MSTest supports a wide range of .NET platforms and target frameworks. The following table summarizes platform support and special considerations:

| Platform | Target frameworks | Threading support | Special attributes | Notes |
|----------|-------------------|-------------------|-------------------|-------|
| **.NET** | .NET 8+ | Full parallelization | All attributes | Recommended for new projects |
| **.NET Framework** | 4.6.2+ | Full parallelization | All attributes | Full feature support |
| **WinUI 3** | .NET 8+ | UI thread | `UITestMethod` | Requires Windows App SDK; see [Test WinUI 3 apps with MSTest and MTP](running-tests/winui.md) |
| **Native AOT** | .NET 8+ | Full parallelization | Most attributes | Limited feature set; see [Native AOT sample](https://github.com/microsoft/testfx/tree/main/samples/public/mstest-runner/NativeAotRunner) |
| **Browser WebAssembly** | .NET 10+ custom host | Single-threaded | Limited | MTP execution support starts with the MSTest 4.4 preview |
| **WASI WebAssembly** | .NET 10+ custom host | Single-threaded | Limited | MTP execution support starts with the MSTest 4.4 preview |

### Platform-specific considerations

#### WinUI 3 testing

WinUI 3 tests also require UI thread access for testing visual components:

```csharp
[TestClass]
public class WinUITests
{
    [UITestMethod]
    public void TestWinUIControl()
    {
        // Test runs on UI thread
        var window = new MainWindow();
        Assert.IsNotNull(window);
    }
}
```

To configure unpackaged or packaged full-trust WinUI 3 tests, see [Test WinUI 3 apps with MSTest and MTP](running-tests/winui.md).

Starting with MSTest 4.4, Microsoft.Testing.Platform also supports unpackaged WinUI test applications. For setup details, see the [unpackaged WinUI sample](https://github.com/microsoft/testfx/tree/main/samples/public/mstest-runner/MSTestRunnerWinUIUnpackaged).

#### Native AOT

Native AOT compilation is supported with some limitations due to reduced reflection capabilities. Use source generators where possible and test your AOT scenarios with the [NativeAotRunner sample](https://github.com/microsoft/testfx/tree/main/samples/public/mstest-runner/NativeAotRunner).

#### Browser and WASI WebAssembly

The MSTest 4.4 preview supports custom .NET 10 browser or WASI WebAssembly hosts. To run tests from a referenced MSTest assembly, call `AddMSTest`. In the host project, set `EnableMSTestRunner` to `true` and `GenerateTestingPlatformEntryPoint` to `false`. Keep the MSTest and MTP package versions aligned.

On a single-threaded WebAssembly runtime, MSTest can't forcibly interrupt a timed-out test. Debugger wait isn't supported on browser or WASI, and browser doesn't support debugger launch options.

MTP can stream TRX data and report test and session file artifacts through the host's WebAssembly virtual file system and artifact channel. Azure DevOps publishing works only when the host provides supported HTTP access and the required pipeline authentication. These features don't grant unrestricted host file-system or network access.

For a complete browser host, see the [BrowserPlayground sample](https://github.com/microsoft/testfx/tree/main/samples/BrowserPlayground).

### STA threading support

For Windows COM interop scenarios, MSTest provides `STATestClass` and `STATestMethod` attributes to run tests in a single-threaded apartment. For details on STA threading, including async continuation support with `UseSTASynchronizationContext`, see [Threading attributes](writing-tests/controlling-execution.md#threading-attributes).

## Test runners

MSTest supports two test execution platforms:

- **[Microsoft.Testing.Platform (MTP)](running-tests/overview.md)**: The modern, recommended test platform with improved performance and extensibility.

For new projects, we recommend using [MTP](running-tests/overview.md) with [MSTest.Sdk](running-tests/sdk.md).

## MSTest support policy

Since v3.0.0, MSTest strictly follows [semantic versioning](https://learn.microsoft.com/en-us/dotnet/csharp/versioning#semantic-versioning).

The MSTest team only supports the latest released version and strongly encourages users to always update to the latest version to benefit from improvements and security patches. Preview releases aren't supported by Microsoft but are offered for public testing ahead of final release.

### Version history

MSTest has undergone significant evolution across major versions:

- **MSTest v1**: The original Visual Studio testing framework
- **MSTest v2**: First open-source release with cross-platform support
- **MSTest v3**: Modern rewrite with improved architecture and features
- **MSTest v4**: Current version with enhanced features

> [!NOTE]
> MSTest 4.4 is under development as of August 2026. Features marked as introduced in MSTest 4.4 require a preview build until version 4.4.0 is released.

For details on all releases, see the [MSTest changelog](https://github.com/microsoft/testfx/blob/main/docs/Changelog.md).

If you're upgrading from an older version, see the migration guides:

- [Migrate from MSTest v1 to v3](migration/v1-to-v3.md)
- [Migrate from MSTest v3 to v4](migration/v3-to-v4.md)

### Breaking changes

The MSTest team carefully reviews and minimizes breaking changes. When breaking changes are necessary, the team uses [GitHub Announcements](https://github.com/microsoft/testfx/discussions/categories/announcements) and [breaking change labels](https://github.com/microsoft/testfx/labels/breaking-change) on issues to inform the community early, giving users time to provide feedback and raise concerns before changes are released.

## Next steps

- [Get started with MSTest](getting-started/overview.md)
- [Write tests](writing-tests/overview.md)
- [Run tests](running-tests/overview.md)
- [Test WinUI 3 apps](running-tests/winui.md)
- [Configure MSTest](running-tests/configure.md)
- [MSTest code analyzers](analyzers/overview.md)
