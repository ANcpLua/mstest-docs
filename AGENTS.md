# MSTest docs — local Markdown copy

MSTest on Microsoft.Testing.Platform (MTP) as Markdown, one file per page. Nothing else is covered: MTP is the only test platform here.

```
MSTest.Sdk      = 4.5.1
MSTest API docs = mstest-net-4.5
Runner          = Microsoft.Testing.Platform
MTP             = 2.5.1
TFM             = net10.0
.NET SDK        = 10.0.401 (Runtime 10.0.12)
```

## How to use this folder

- Open the relevant topic index below, then read the page you need. Do not load the whole corpus.
- Paths are relative to this folder. `rg -l <term> docs/` when the index doesn't name it.
- `docs/mstest/` and `docs/testing-platform/` are the guides, `docs/api/` is the API reference of exactly the pinned packages.
- The guides name the version a feature arrived in; the API reference is proof of what the pinned version has.
- Left out on purpose: other test platforms, migration from older versions, obsolete API, what needs a newer .NET SDK than the pinned one, and Microsoft Fakes.

## Sources

- Guides: [dotnet/docs](https://github.com/dotnet/docs/tree/9f0ca91d23811331c90405ee4e78e8150b2baf07/docs/core/testing) (branch `live`, commit `9f0ca91`), © Microsoft, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
  Changed for this copy: includes and snippets are inlined, links point to local files or learn.microsoft.com, package versions in examples follow the pins above, preview notes for the pinned versions are reworded as released, and what the list above names is removed.
- API reference: generated from the assemblies and XML documentation of the NuGet packages `MSTest.TestFramework` 4.5.1 and `Microsoft.Testing.Platform` 2.5.1 ([microsoft/testfx](https://github.com/microsoft/testfx), MIT).

## Refresh

- Edit `VERSION` to pin other versions.
- `python3 scripts/refresh_docs.py` — rebuild `docs/` and this file. Needs `git` and the .NET SDK (`dotnet run scripts/api_reference.cs` writes the API reference).

This file is generated — edit `scripts/refresh_docs.py`, not this file.

## Index

- [docs/mstest/](docs/mstest/AGENTS.md) — 113 pages.
- [docs/testing-platform/](docs/testing-platform/AGENTS.md) — 26 pages.
- [docs/api/](docs/api/AGENTS.md) — 266 pages.
