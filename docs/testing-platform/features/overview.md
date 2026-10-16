# Microsoft.Testing.Platform (MTP) features

MTP ships with built-in features and can be extended through NuGet packages.

When using [Microsoft.Testing.Platform.MSBuild](https://www.nuget.org/packages/Microsoft.Testing.Platform.MSBuild) (included transitively by MSTest, NUnit, and xUnit runners), installing an extension NuGet package is all you need — extensions are automatically detected and registered, and the entry point is generated for you.

If you opt out of the auto-generated entry point by setting `<GenerateTestingPlatformEntryPoint>false</GenerateTestingPlatformEntryPoint>`, you must register extensions manually in your `Main` method. Each extension page documents the manual registration call.

Extensions that require a NuGet package are shipped with their own licensing model (some less permissive), be sure to refer to the license associated with the extensions you want to use.

Some extensions are *experimental*: their APIs are annotated with the `TPEXP` diagnostic and might change in a future release, so you must acknowledge the diagnostic to use them. Experimental extensions are marked **(experimental)** in the following lists.

## Start here

Use the following path based on your goal:

- Find command-line switches in one place: [MTP CLI options reference](../cli-options.md).
- Add capabilities to your test runs: use the feature pages in this article.
- Create your own extension: [MTP architecture](../extending/overview.md), [Extension points](../extending/extensions.md), and [Services](../extending/services.md).

## Choose by scenario

- Need to customize terminal output: [Terminal output](terminal-output.md) (built-in)
- Need TRX or Azure DevOps reports: [Test reports](test-reports.md) (extension)
- Need GitHub Actions-native output (log groups, annotations, and job summary): [GitHub Actions report](test-reports.md#github-actions-reports) (extension)
- Need coverage data: [Code coverage](code-coverage.md) (extension)
- Need crash or hang diagnostics: [Crash and hang dumps](crash-hang-dumps.md) (extension)
- Need to record the screen during a run: [Diagnostics](diagnostics.md) (extension, experimental)
- Need to deploy and launch a packaged full-trust, UWP, or AppContainer test host: [Test host deployment](test-host-deployment.md) (extension; experimental launcher API)
- Need to reuse `Microsoft.Extensions.Configuration`, `Microsoft.Extensions.Hosting`, or `Microsoft.Extensions.Logging`: [Microsoft.Extensions integration](extensions-integration.md) (extension, experimental)
- Need to build editor or IDE integration: [Server mode](../extending/server-mode.md) (built-in)
- Need to load extensions that aren't compile-time references: [Dynamic extension loading](../extending/extensions.md#load-extensions-dynamically) (built-in, opt-in)
- Need to retry failed tests: [Retry](retry.md#retry) (extension)
- Need hot reload support: [Hot Reload](hot-reload.md) (extension)
- Need OpenTelemetry traces and metrics: [OpenTelemetry](open-telemetry.md) (extension)
- Need to supply AI chat clients to a test framework or extension: [AI integrations](ai.md) (extension, experimental)
- Telemetry data collection and opt-out: [Telemetry](telemetry.md) (extension)

## Built-in features

These features are part of the core platform and don't require additional NuGet packages.

**[Terminal output](terminal-output.md)**

Status and progress reporting to the terminal: output modes, ANSI support, and progress indicators.

**[Server mode](../extending/server-mode.md)**

Drive test discovery and execution from an editor, IDE, or other tool through JSON-RPC.

**[Dynamic extension loading](../extending/extensions.md#load-extensions-dynamically)**

Load explicitly declared extension assemblies from JSON manifests when a run opts in.

## Extension features

These features require installing NuGet packages.

**[Test reports](test-reports.md)**

Generate test report files (TRX, HTML, JUnit, CTRF, Azure DevOps, GitHub Actions).

**[Code coverage](code-coverage.md)**

Collect code coverage data during test execution.

**[Crash and hang dumps](crash-hang-dumps.md)**

Collect process dump files when the test host crashes or hangs.

**[OpenTelemetry](open-telemetry.md)**

Emit traces and metrics through OpenTelemetry during test runs.

**[AI integrations](ai.md)** (experimental)

Supply provider-neutral AI chat clients to test frameworks and extensions, including through Azure AI Foundry.

**[Retry](retry.md)**

Retry failed tests with configurable policies.

**[Hot Reload](hot-reload.md)**

Run tests with hot reload support for rapid iteration.

**[Telemetry](telemetry.md)**

Telemetry collection. Learn how to opt out and what data is collected.

**[Diagnostics](diagnostics.md)** (experimental, introduced in MTP 2.3.0)

Capture evidence to diagnose a run, such as recording the screen with the video recorder.

**[Test host deployment](test-host-deployment.md)** (introduced in MTP 2.3.0; stable package API starting in MTP 2.4.0; experimental launcher API; UWP and AppContainer support introduced in MTP 2.5)

Control how and where the test host is deployed and launched, including packaged full-trust, UWP, and AppContainer test hosts.

**[Microsoft.Extensions integration](extensions-integration.md)** (experimental; logging introduced in MTP 2.3.0; configuration and hosting introduced in MTP 2.5)

Bridge MTP to the `Microsoft.Extensions.*` libraries your application already uses, including configuration snapshots, application-owned hosts, and diagnostic log forwarding.
