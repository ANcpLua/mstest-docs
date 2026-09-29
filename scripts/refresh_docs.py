#!/usr/bin/env python3
"""Build docs/ as Markdown for MSTest on Microsoft.Testing.Platform, rebuild CLAUDE.md.

Guides come from dotnet/docs (branch `live`, the source of learn.microsoft.com), the API reference from the
NuGet packages pinned in VERSION. Everything about other test platforms is left out.

Run from anywhere: python3 scripts/refresh_docs.py [--source <dotnet/docs checkout>] [--removed <file>]
"""
import collections
import io
import os
import re
import subprocess
import sys
import tempfile
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SOURCE_REPO = "https://github.com/dotnet/docs.git"
SOURCE_BRANCH = "live"
SOURCE_PATHS = ["docs/core/testing", "docs/core/tools", "includes", "samples/snippets/core/testing"]
LEARN = "https://learn.microsoft.com/en-us"
NUGET = "https://api.nuget.org/v3-flatcontainer"

# Source (relative to docs/core in dotnet/docs) -> page (relative to docs/ here).
PAGES = {
    "testing/unit-testing-mstest-intro.md": "mstest/intro.md",
    "testing/unit-testing-mstest-getting-started.md": "mstest/getting-started/overview.md",
    "testing/unit-testing-csharp-with-mstest.md": "mstest/getting-started/csharp.md",
    "testing/unit-testing-fsharp-with-mstest.md": "mstest/getting-started/fsharp.md",
    "testing/unit-testing-visual-basic-with-mstest.md": "mstest/getting-started/visual-basic.md",
    "testing/unit-testing-mstest-writing-tests.md": "mstest/writing-tests/overview.md",
    "testing/unit-testing-mstest-writing-tests-assertions.md": "mstest/writing-tests/assertions.md",
    "testing/unit-testing-mstest-writing-tests-testcontext.md": "mstest/writing-tests/testcontext.md",
    "testing/unit-testing-mstest-writing-tests-data-driven.md": "mstest/writing-tests/data-driven.md",
    "testing/unit-testing-mstest-writing-tests-lifecycle.md": "mstest/writing-tests/lifecycle.md",
    "testing/unit-testing-mstest-writing-tests-controlling-execution.md": "mstest/writing-tests/controlling-execution.md",
    "testing/unit-testing-mstest-writing-tests-organizing.md": "mstest/writing-tests/organizing.md",
    "testing/unit-testing-mstest-writing-tests-deployment-items.md": "mstest/writing-tests/deployment-items.md",
    "testing/order-unit-tests.md": "mstest/writing-tests/ordering.md",
    "testing/unit-testing-mstest-running-tests.md": "mstest/running-tests/overview.md",
    "testing/unit-testing-mstest-winui.md": "mstest/running-tests/winui.md",
    "testing/unit-testing-mstest-configure.md": "mstest/running-tests/configure.md",
    "testing/unit-testing-mstest-sdk.md": "mstest/running-tests/sdk.md",
    "testing/selective-unit-tests.md": "mstest/running-tests/filter.md",
    "testing/unit-testing-mstest-migration-from-v1-to-v3.md": "mstest/migration/v1-to-v3.md",
    "testing/unit-testing-mstest-migration-v3-v4.md": "mstest/migration/v3-to-v4.md",
    "testing/microsoft-testing-platform-intro.md": "testing-platform/intro.md",
    "testing/microsoft-testing-platform-run-and-debug.md": "testing-platform/run-and-debug.md",
    "testing/microsoft-testing-platform-cli-options.md": "testing-platform/cli-options.md",
    "testing/microsoft-testing-platform-config.md": "testing-platform/config.md",
    "testing/microsoft-testing-platform-troubleshooting.md": "testing-platform/troubleshooting.md",
    "testing/unit-testing-with-dotnet-test.md": "testing-platform/dotnet-test.md",
    "tools/dotnet-test-mtp.md": "testing-platform/dotnet-test-cli.md",
    "testing/microsoft-testing-platform-features.md": "testing-platform/features/overview.md",
    "testing/microsoft-testing-platform-terminal-output.md": "testing-platform/features/terminal-output.md",
    "testing/microsoft-testing-platform-test-reports.md": "testing-platform/features/test-reports.md",
    "testing/microsoft-testing-platform-code-coverage.md": "testing-platform/features/code-coverage.md",
    "testing/microsoft-testing-platform-crash-hang-dumps.md": "testing-platform/features/crash-hang-dumps.md",
    "testing/microsoft-testing-platform-diagnostics.md": "testing-platform/features/diagnostics.md",
    "testing/microsoft-testing-platform-test-host-deployment.md": "testing-platform/features/test-host-deployment.md",
    "testing/microsoft-testing-platform-extensions-integration.md": "testing-platform/features/extensions-integration.md",
    "testing/microsoft-testing-platform-open-telemetry.md": "testing-platform/features/open-telemetry.md",
    "testing/microsoft-testing-platform-ai.md": "testing-platform/features/ai.md",
    "testing/microsoft-testing-platform-retry.md": "testing-platform/features/retry.md",
    "testing/microsoft-testing-platform-hot-reload.md": "testing-platform/features/hot-reload.md",
    "testing/microsoft-testing-platform-fakes.md": "testing-platform/features/fakes.md",
    "testing/microsoft-testing-platform-telemetry.md": "testing-platform/features/telemetry.md",
    "testing/microsoft-testing-platform-migration-from-v1-to-v2.md": "testing-platform/migration/v1-to-v2.md",
    "testing/microsoft-testing-platform-architecture.md": "testing-platform/extending/overview.md",
    "testing/microsoft-testing-platform-architecture-test-framework.md": "testing-platform/extending/test-framework.md",
    "testing/microsoft-testing-platform-architecture-extensions.md": "testing-platform/extending/extensions.md",
    "testing/microsoft-testing-platform-architecture-capabilities.md": "testing-platform/extending/capabilities.md",
    "testing/microsoft-testing-platform-architecture-services.md": "testing-platform/extending/services.md",
    "testing/microsoft-testing-platform-server-mode.md": "testing-platform/extending/server-mode.md",
}
ANALYZERS = ("testing/mstest-analyzers", "mstest/analyzers")
# MSTest and platform pages that are about another platform or the legacy runner.
LEFT_OUT = re.compile(r"bridge|migrating-|migration-from-tmi")
PIVOT = "mstest"

# Package -> assemblies inside the package, `{tfm}` being the best match for the TFM in VERSION.
API = {
    "MSTest.TestFramework": ("MSTest.Sdk", ["lib/{tfm}/MSTest.TestFramework.dll", "buildTransitive/{tfm}/MSTest.TestFramework.Extensions.dll"]),
    "Microsoft.Testing.Platform": ("MTP", ["lib/{tfm}/Microsoft.Testing.Platform.dll"]),
}
API_NAMESPACES = ("Microsoft.VisualStudio.TestTools.UnitTesting", "Microsoft.Testing.Platform")

BANNED = re.compile(r"vstest|Microsoft\.NET\.Test\.Sdk|testcasefilter|test-platforms-overview", re.IGNORECASE)
# Passages reworded before the removal, so that what they say about MTP survives: page -> [(pattern, replacement)].
PATCHES = {
    "mstest/intro.md": [
        (r"#### UWP testing.*?(?=#### WinUI 3 testing)", ""),
    ],
    "mstest/getting-started/overview.md": [
        (r"extension profiles, switching to VSTest, or integrating", "extension profiles or integrating"),
        (r"^\| \*\*BlankUwpNet9App\*\*.*\n", ""),
    ],
    "mstest/running-tests/overview.md": [
        (r"^## VSTest vs MTP$", "## MSTest runner"),
        (r"MSTest supports running tests with both VSTest and (\[Microsoft\.Testing\.Platform \(MTP\)\]\([^)]*\))\.", r"MSTest runs tests with \1."),
        (r", such as `vstest\.console` or `dotnet test`, needed", " needed"),
    ],
    "mstest/running-tests/sdk.md": [
        (r"If you're using the VSTest mode of `dotnet test`.*?```diff.*?```\n", ""),
    ],
    "mstest/analyzers/mstest0040.md": [
        (r" when using MTP or VSTest", " when using MTP"),
    ],
    "testing-platform/intro.md": [
        (r"alternative to \[VSTest\]\([^)]*\) for running tests", "test platform for running tests"),
        (r", such as `vstest\.console` or `dotnet test`,? needed", " needed"),
    ],
    "testing-platform/dotnet-test.md": [
        (
            r"This article provides insights.*?- \*MTP\* mode: Introduced with the \.NET 10 SDK, this mode exclusively supports test applications built with MTP\.",
            "The `dotnet test` command runs test applications built with MTP in *MTP* mode, introduced with the .NET 10 SDK.",
        ),
    ],
    "testing-platform/features/code-coverage.md": [
        (r", while it used to be `true` in VSTest", ""),
    ],
    "testing-platform/migration/v1-to-v2.md": [
        (
            r"### Compatibility with VSTest-based `dotnet test`.*?(?=To opt-in the MTP-based implementation)",
            "### `dotnet test` requires the MTP mode\n\nRunning MTP test projects with .NET 10 SDK now requires opting-in to the MTP-based `dotnet test`. "
            "The `TestingPlatformDotnetTestSupport` MSBuild property from MTP v1 no longer enables running them.\n\n",
        ),
        (r"Attempting to run the VSTest-based.*?mtp-error>\n", ""),
    ],
}
TAB = re.compile(r"^(#+) \[(.*)\]\(#tab/[^)]*\)\s*$", re.MULTILINE)
# Package versions in examples follow VERSION, except on migration pages, which name old versions on purpose.
PINNED = re.compile(r"(MSTest\.Sdk/|\"MSTest\.Sdk\": \"|Include=\"MSTest(?:\.[\w.]+)?\" Version=\")\d+(?:\.\d+)+")
FENCE = re.compile(r"^(\s*(?:>\s*)*)(`{3,}|~{3,})")
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
ITEM = re.compile(r"^(\s*)(?:[-*+]|\d+\.)\s+")
ALERT = re.compile(r"^\s*>\s*\[![A-Za-z]+\]\s*$")
SENTENCE = re.compile(r"(?<=[.!?])\s+(?=[A-Z\[`*_(])")
LINK = re.compile(r"(!?)\[((?:[^\]\[]|\[[^\]]*\])*)\]\((<[^>]*>|[^)\s]+)(\s+\"[^\"]*\")?\)")
INCLUDE = re.compile(r"\[!INCLUDE\s*\[[^\]]*\]\(([^)]+)\)\]", re.IGNORECASE)
CODE = re.compile(r"^([ \t>]*):::code\s+(.*?):::[ \t]*$", re.MULTILINE)
OLD_CODE = re.compile(r"^([ \t>]*)\[!code-(\w+)\[[^\]]*\]\(([^)?#]+)(?:\?([^)#]*))?(?:#([^)]*))?\)\][ \t]*$", re.MULTILINE)
IMAGE = re.compile(r":::image\s+(.*?):::")
ATTRIBUTE = re.compile(r"([\w-]+)=\"([^\"]*)\"")
ZONE = re.compile(r"^\s*:::\s*zone(?:\s+pivot=\"([^\"]*)\"|-end)\s*$")
XREF = re.compile(r"<xref:([^>\s]+)>")
SNIPPET_TAG = re.compile(r"^\s*(?://|'|#|<!--|\(\*)\s*</?[\w-]+>\s*(?:-->|\*\))?\s*$")

removed = []


def run(*command, cwd=None):
    subprocess.run(command, cwd=cwd, check=True, stdout=subprocess.DEVNULL)


def versions():
    rows = [line.split("=", 1) for line in (ROOT / "VERSION").read_text(encoding="utf-8").splitlines() if "=" in line]
    return {key.strip(): value.strip() for key, value in rows}


def checkout(target):
    run("git", "clone", "--quiet", "--depth", "1", "--filter=blob:none", "--sparse", "--branch", SOURCE_BRANCH, SOURCE_REPO, str(target))
    run("git", "sparse-checkout", "set", *SOURCE_PATHS, cwd=target)
    return head(target)


def head(repo):
    return subprocess.run(["git", "rev-parse", "HEAD"], cwd=repo, check=True, capture_output=True, text=True).stdout.strip()


def option(name):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else None


# ---------------------------------------------------------------- API reference


def best_tfm(names, prefix, wanted):
    found = {m.group(1): float(m.group(1)) for m in (re.match(re.escape(prefix) + r"net(\d+\.\d+)/", n) for n in names) if m}
    limit = float(wanted[len("net"):])
    usable = [v for v in found.values() if v <= limit]
    return "net" + [k for k, v in found.items() if v == max(usable)][0]


def build_api(pins, work):
    for package, (pin, assemblies) in API.items():
        version = pins[pin]
        url = f"{NUGET}/{package.lower()}/{version}/{package.lower()}.{version}.nupkg"
        with urllib.request.urlopen(url, timeout=120) as response:
            archive = zipfile.ZipFile(io.BytesIO(response.read()))
        folder = work / package
        archive.extractall(folder)
        paths = [str(folder / a.format(tfm=best_tfm(archive.namelist(), a.split("{tfm}")[0], pins["TFM"]))) for a in assemblies]
        run("dotnet", "run", str(ROOT / "scripts" / "api_reference.cs"), "--", str(DOCS / "api"), package, version, *paths, cwd=work)


def api_pages():
    return {f"{p.parent.name}.{p.stem}".replace("-", "`"): p for p in (DOCS / "api").rglob("*.md")}


# ---------------------------------------------------------------- guides


def front_matter(text):
    match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return {}, text
    meta = {}
    for key in ("title", "description"):
        found = re.search(rf"^{key}:\s*(.*)$", match.group(1), re.MULTILINE)
        if found:
            value = found.group(1).strip()
            meta[key] = value[1:-1] if len(value) > 1 and value[0] == value[-1] and value[0] in "\"'" else value
    return meta, text[match.end():]


def outside_code(text, change):
    """Apply `change` to everything that is not a fenced code block."""
    out, chunk, fence = [], [], None
    for line in text.split("\n"):
        mark = FENCE.match(line)
        if fence is None and mark:
            out.append(change("\n".join(chunk)))
            chunk, fence = [line], mark.group(2)[0] * 3
        elif fence is not None:
            chunk.append(line)
            if mark and mark.group(2).startswith(fence) and line.strip(" >").strip("`~") == "":
                out.append("\n".join(chunk))
                chunk, fence = [], None
        else:
            chunk.append(line)
    out.append(change("\n".join(chunk)) if fence is None else "\n".join(chunk))
    return "\n".join(out)


def keep_pivot(text):
    out, keep = [], True
    for line in text.split("\n"):
        zone = ZONE.match(line)
        if zone:
            keep = zone.group(1) is None or PIVOT in zone.group(1).split(",")
        elif keep:
            out.append(line)
    return "\n".join(out)


def dedent(lines):
    lines = [line.rstrip() for line in lines if not SNIPPET_TAG.match(line)]
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    indent = min((len(line) - len(line.lstrip()) for line in lines if line), default=0)
    return [line[indent:] for line in lines]


def snippet(path, name=None, lines=None):
    source = path.read_text(encoding="utf-8-sig").replace("\r\n", "\n").split("\n")
    if name:
        tag = re.compile(rf"<{re.escape(name)}>|#region\s+{re.escape(name)}\b", re.IGNORECASE)
        end = re.compile(rf"</{re.escape(name)}>|#endregion", re.IGNORECASE)
        start = next(i for i, line in enumerate(source) if tag.search(line))
        stop = next(i for i in range(start + 1, len(source)) if end.search(source[i]))
        return dedent(source[start + 1:stop])
    if lines:
        picked = []
        for part in lines.split(","):
            first, _, last = part.strip().partition("-")
            picked += source[int(first) - 1:int(last or first) if last != "" or "-" not in part else len(source)]
        return dedent(picked)
    return dedent(source)


def fenced(prefix, language, lines):
    language = {"vb": "vb", "fsharp": "fsharp", "csharp": "csharp"}.get(language.lower(), language.lower())
    return "\n".join(prefix + line if line else prefix.rstrip() for line in [f"```{language}"] + lines + ["```"])


class Guide:
    def __init__(self, repo, source, target, types):
        self.repo, self.source, self.target, self.types = repo, source, target, types

    def render(self):
        meta, body = front_matter(self.source.read_text(encoding="utf-8-sig").replace("\r\n", "\n"))
        body = self.expand(body, self.source)
        if TAB.search(body):
            body = re.sub(r"^---\s*$", "", TAB.sub(r"\1 \2", body), flags=re.MULTILINE)
        for pattern, replacement in PATCHES.get(self.target, []):
            body, count = re.subn(pattern, replacement, body, flags=re.DOTALL | re.MULTILINE)
            if count == 0:
                sys.exit(f"patch no longer applies to {self.target}: {pattern[:60]}")
        return meta, body

    def expand(self, body, file):
        body = keep_pivot(body)
        includes = []

        def hold(match):
            included = self.path(match.group(1), file)
            includes.append(self.expand(front_matter(included.read_text(encoding="utf-8-sig").replace("\r\n", "\n"))[1], included).strip())
            return f"\x00{len(includes) - 1}\x00"

        body = INCLUDE.sub(hold, body)
        body = CODE.sub(lambda m: self.code(m, file), body)
        body = OLD_CODE.sub(lambda m: self.old_code(m, file), body)
        body = re.sub(r"^>?\s*\[!div[^\]]*\]\s*\n", "", body, flags=re.MULTILINE)
        body = outside_code(body, lambda text: self.inline(text, file))
        return re.sub(r"\x00(\d+)\x00", lambda m: includes[int(m.group(1))], body)

    def path(self, reference, file):
        return (self.repo / reference[2:] if reference.startswith("~/") else file.parent / reference).resolve()

    def code(self, match, file):
        attributes = dict(ATTRIBUTE.findall(match.group(2)))
        lines = snippet(self.path(attributes["source"], file), attributes.get("id"), attributes.get("range"))
        return fenced(match.group(1), attributes.get("language", ""), lines)

    def old_code(self, match, file):
        query = dict(part.split("=", 1) for part in (match.group(4) or "").split("&") if "=" in part)
        lines = snippet(self.path(match.group(3), file), query.get("name"), query.get("range"))
        return fenced(match.group(1), match.group(2), lines)

    def inline(self, text, file):
        def image(match):
            attributes = dict(ATTRIBUTE.findall(match.group(1)))
            return f"![{attributes.get('alt-text', '')}]({self.url(attributes['source'], file)})"

        def link(match):
            bang, label, url, title = match.group(1), match.group(2), match.group(3).strip("<>"), match.group(4) or ""
            if url.startswith("xref:"):
                return f"[{label}]({self.api(url[5:])[1]})"
            return f"{bang}[{label}]({self.url(url, file)}{title})"

        text = IMAGE.sub(image, text)
        text = LINK.sub(link, text)
        return XREF.sub(lambda m: "[`{}`]({})".format(*self.api(m.group(1))), text)

    def url(self, url, file):
        if re.match(r"[a-z][a-z0-9+.-]*:|#", url, re.IGNORECASE):
            return url
        if url.startswith("/"):
            return LEARN + url
        path, mark, rest = re.match(r"([^?#]*)([?#]?)(.*)", url).groups()
        absolute = self.path(path, file)
        key = absolute.relative_to(self.repo / "docs" / "core").as_posix() if (self.repo / "docs" / "core") in absolute.parents else None
        page = page_for(key)
        if page:
            anchor = "#" + rest if mark == "#" else ""
            return os.path.relpath(DOCS / page, (DOCS / self.target).parent).replace(os.sep, "/") + anchor
        site = absolute.relative_to(self.repo / "docs").as_posix() if (self.repo / "docs") in absolute.parents else absolute.relative_to(self.repo).as_posix()
        site = re.sub(r"(^|/)index\.md$", r"\1", re.sub(r"\.md$", "", site) + (".md" if site.endswith("index.md") else ""))
        return f"{LEARN}/dotnet/{site}{mark}{rest}"

    def api(self, uid):
        uid, _, query = uid.replace("%60", "`").partition("?")
        name = re.sub(r"\(.*\)$", "", uid).rstrip("*")
        parts = [re.sub(r"`+\d+", "<T>", part) for part in name.split(".")]
        label = ".".join(parts[-2:]) if "nameWithType" in query else parts[-1]
        for end in range(len(name.split(".")), 0, -1):
            page = self.types.get(".".join(name.split(".")[:end]))
            if page:
                return label, os.path.relpath(page, (DOCS / self.target).parent).replace(os.sep, "/")
        view = "?view=mstest-net-" + ".".join(versions()["MSTest.Sdk"].split(".")[:2]) if name.startswith(API_NAMESPACES[0]) else ""
        return label, f"{LEARN}/dotnet/api/{name.lower().replace('`', '-')}{view}"


def page_for(key):
    if key is None:
        return None
    if key in PAGES:
        return PAGES[key]
    if key.startswith(ANALYZERS[0] + "/") and key.count("/") == 2 and key.endswith(".md"):
        return f"{ANALYZERS[1]}/{Path(key).name.lower()}"
    return None


def guide_sources(repo):
    core = repo / "docs" / "core"
    keys = list(PAGES) + sorted(p.relative_to(core).as_posix() for p in (core / ANALYZERS[0]).glob("*.md"))
    known = {Path(key).name for key in keys}
    for path in sorted((core / "testing").glob("*.md")):
        if re.match(r"unit-testing-mstest-|microsoft-testing-platform-", path.name) and path.name not in known and not LEFT_OUT.search(path.name):
            print(f"not mapped: {path.name} (add it to PAGES)", file=sys.stderr)
    return [(core / key, page_for(key)) for key in keys]


# ---------------------------------------------------------------- one platform only


def sentences(text):
    """`text` without the sentences that name another platform; second value: a dropped sentence introduced what follows."""
    text = LINK.sub(lambda m: m.group(0) if BANNED.search(m.group(2)) or not re.search("vstest", m.group(3), re.IGNORECASE) else m.group(2), text)
    if not BANNED.search(text):
        return text, False
    parts = SENTENCE.split(text)
    kept = [part for part in parts if not BANNED.search(part)]
    removed.extend(part for part in parts if BANNED.search(part))
    return " ".join(kept), bool(BANNED.search(parts[-1])) and parts[-1].rstrip().endswith(":")


def units(lines):
    """Split a block of consecutive lines into table rows, list items, alert labels and paragraphs."""
    out = []
    for line in lines:
        body = re.sub(r"^\s*>\s?", "", line)
        starts = body.lstrip().startswith("|") or ITEM.match(body) or ALERT.match(line) or (out and ALERT.match(out[-1][-1]))
        starts = starts or not body.strip() or (out and not out[-1][-1].strip(" >"))
        starts = starts or (out and out[-1][0].lstrip("> ").startswith("|"))
        if starts or not out:
            out.append([line])
        else:
            out[-1].append(line)
    return out


def filter_unit(lines):
    if ALERT.match(lines[0]) or not lines[0].strip(" >"):
        return lines, False
    first = lines[0]
    prefix = re.match(r"^(\s*(?:>\s?)*\s*(?:(?:[-*+]|\d+\.)\s+)?)", first).group(1)
    body = " ".join([first[len(prefix):]] + [re.sub(r"^\s*(?:>\s?)*", "", line).strip() for line in lines[1:]])
    if body.lstrip().startswith("|"):
        if BANNED.search(body):
            removed.append(body)
            return [], False
        return lines, False
    if not BANNED.search(body):
        return lines, False
    only_link = LINK.fullmatch(body.strip())
    if only_link and BANNED.search(only_link.group(3)):
        removed.append(body)
        return [], False
    kept, intro = sentences(body)
    return ([prefix + kept] if kept.strip() else []), intro


def drop_intro(out):
    """A removed code block takes the sentence that introduced it along."""
    index = len(out) - 1
    while index >= 0 and not out[index].strip():
        index -= 1
    if index < 0 or not out[index].rstrip().endswith(":") or HEADING.match(out[index]):
        return
    prefix = re.match(r"^(\s*(?:>\s?)*\s*(?:(?:[-*+]|\d+\.)\s+)?)", out[index]).group(1)
    parts = SENTENCE.split(out[index][len(prefix):])
    removed.append(parts[-1])
    if len(parts) > 1:
        out[index] = prefix + " ".join(parts[:-1])
    else:
        del out[index:]


def one_platform(text):
    lines = text.split("\n")
    out, index = [], 0
    skip_level = None  # inside a removed section
    skip_indent = None  # inside a removed list item
    skip_code = False  # the sentence introducing the next code block was removed
    while index < len(lines):
        line = lines[index]
        fence = FENCE.match(line)
        if fence:
            end = index + 1
            while end < len(lines) and not (FENCE.match(lines[end]) and lines[end].strip(" >").strip("`~") == "" and lines[end].strip(" >")[0] == fence.group(2)[0]):
                end += 1
            block = lines[index:end + 1]
            index = end + 1
            nested = skip_indent is not None and len(fence.group(1)) > skip_indent
            if skip_level is not None or nested:
                continue
            skip_indent = None
            kept = [block[0]] + [item for item in block[1:-1] if not BANNED.search(item)] + [block[-1]]
            if skip_code or not any(item.strip(" >") for item in kept[1:-1]):
                removed.append("\n".join(block))
                if not skip_code:
                    drop_intro(out)
                skip_code = False
                continue
            removed.extend(item for item in block if BANNED.search(item))
            out += kept
            continue
        if not line.strip():
            out.append(line)
            index += 1
            continue
        heading = HEADING.match(line)
        if heading:
            index += 1
            level = len(heading.group(1))
            if skip_level is not None and level > skip_level:
                continue
            skip_level, skip_indent, skip_code = None, None, False
            if BANNED.search(heading.group(2)):
                removed.append(line)
                skip_level = level
                continue
            out.append(line)
            continue
        end = index
        while end < len(lines) and lines[end].strip() and not FENCE.match(lines[end]) and not HEADING.match(lines[end]):
            end += 1
        block = lines[index:end]
        index = end
        if skip_level is not None:
            continue
        skip_code = False
        kept = []
        for unit in units(block):
            indent = len(unit[0]) - len(unit[0].lstrip())
            if skip_indent is not None and indent > skip_indent:
                continue
            skip_indent = None
            result, skip_code = filter_unit(unit)
            if not result and ITEM.match(re.sub(r"^\s*>\s?", "", unit[0])):
                skip_indent = indent
            kept += result
        kept = tidy(kept)
        if kept:
            out += kept
    return re.sub(r"\n{3,}", "\n\n", "\n".join(empty_sections(out))).strip() + "\n"


def tidy(block):
    """Drop alert labels, quote separators and table heads that lost their content."""
    rows = [line for line in block if line.lstrip("> ").startswith("|")]
    if rows and len(rows) == len(block) and len(rows) <= 2:
        return []
    out = list(block)
    index = 0
    while index < len(out):
        following = next((line for line in out[index + 1:] if line.strip(" >")), None)
        label = ALERT.match(out[index]) and (following is None or ALERT.match(following))
        separator = not out[index].strip(" >") and (index == 0 or following is None or not out[index - 1].strip(" >"))
        if label or separator:
            del out[index]
            index = max(index - 1, 0)
        else:
            index += 1
    return out


def empty_sections(lines):
    changed = True
    while changed:
        changed = False
        fence = False
        for index, line in enumerate(lines):
            if FENCE.match(line):
                fence = not fence
            heading = None if fence else HEADING.match(line)
            if not heading or len(heading.group(1)) == 1:
                continue
            level, inner, empty = len(heading.group(1)), False, True
            for after in lines[index + 1:]:
                if FENCE.match(after):
                    inner = not inner
                following = None if inner else HEADING.match(after)
                if following and len(following.group(1)) <= level:
                    break
                if after.strip() and not following:
                    empty = False
                    break
            if empty:
                removed.append(line)
                del lines[index]
                changed = True
                break
    return lines


# ---------------------------------------------------------------- index


def first_sentence(text):
    sentence = re.split(r"(?<![ (][a-z]\.[a-z][.])(?<=[.!?])\s+(?=[A-Z`])", text.strip(), maxsplit=1)[0].rstrip(":")
    return sentence if len(sentence) <= 160 else sentence[:157].rstrip() + "…"


def describe(path, meta):
    text = path.read_text(encoding="utf-8")
    title = meta.get("title") or re.search(r"^# (.*)$", text, re.MULTILINE).group(1)
    summary = meta.get("description")
    if summary is None:
        found = re.search(r"^- Package:.*\n\n((?!```)[^\n#].*)$", text, re.MULTILINE)
        summary = found.group(1) if found else ""
    summary = sentences(summary)[0]
    if not summary:
        summary = next((line for line in text.split("\n")[1:] if re.match(r"[A-Z`]", line)), "")
    return title, re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", summary)


def write_claude_md(rows, pins, commit):
    groups = collections.OrderedDict()
    for path, title, summary in sorted(rows, key=lambda r: (r[0].startswith("docs/api/"), r[0].count("/") > 2, r[0])):
        groups.setdefault(str(Path(path).parent), []).append((path, title, summary))

    width = max(len(key) for key in pins)
    lines = [
        "# MSTest docs — local Markdown copy",
        "",
        "MSTest on Microsoft.Testing.Platform (MTP) as Markdown, one file per page. Nothing else is covered: MTP is the only test platform here.",
        "",
        "```",
        *[f"{key.ljust(width)} = {value}" for key, value in pins.items()],
        "```",
        "",
        "## How to use this folder",
        "",
        "- Find the topic below, open **one** file, read it. Don't load the whole folder.",
        "- Paths are relative to this folder. `grep -ril <term> docs/` when the index doesn't name it.",
        "- `docs/mstest/` and `docs/testing-platform/` are the guides, `docs/api/` is the API reference of exactly the pinned packages.",
        "- The guides describe the current release and name the version a feature arrived in; the API reference is proof of what the pinned version has.",
        "",
        "## Sources",
        "",
        f"- Guides: [dotnet/docs](https://github.com/dotnet/docs/tree/{commit}/docs/core/testing) (branch `{SOURCE_BRANCH}`, commit `{commit[:7]}`), © Microsoft, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).",
        "  Changed for this copy: includes and snippets are inlined, links point to local files or learn.microsoft.com, package versions in examples follow the pins above, and everything about other test platforms is removed.",
        "- API reference: generated from the assemblies and XML documentation of the NuGet packages "
        + " and ".join(f"`{package}` {pins[pin]}" for package, (pin, _) in API.items())
        + " ([microsoft/testfx](https://github.com/microsoft/testfx), MIT).",
        "",
        "## Refresh",
        "",
        "- Edit `VERSION` to pin other versions.",
        "- `python3 scripts/refresh_docs.py` — rebuild `docs/` and this file. Needs `git` and the .NET SDK (`dotnet run scripts/api_reference.cs` writes the API reference).",
        "",
        "This file is generated — edit `scripts/refresh_docs.py`, not this file.",
        "",
        "## Index",
        "",
    ]
    for group, items in groups.items():
        lines += [f"### `{group}/`", ""]
        for path, title, summary in items:
            lines.append(f"- `{path}` — **{title}**" + (f": {first_sentence(summary)}" if summary else ""))
        lines.append("")
    (ROOT / "CLAUDE.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    pins = versions()
    with tempfile.TemporaryDirectory() as temp:
        work = Path(temp)
        repo = (Path(option("--source")) if option("--source") else work / "dotnet-docs").resolve()
        commit = head(repo) if option("--source") else checkout(repo)

        for stale in DOCS.rglob("*.md"):
            stale.unlink()
        build_api(pins, work.resolve())
        types = api_pages()

        metas = {}
        for source, page in guide_sources(repo):
            meta, body = Guide(repo, source, page, types).render()
            target = DOCS / page
            target.parent.mkdir(parents=True, exist_ok=True)
            if "/migration/" not in page:
                body = PINNED.sub(lambda m: m.group(1) + pins["MSTest.Sdk"], body)
            target.write_text(body, encoding="utf-8")
            metas[target] = meta

    rows = []
    for path in sorted(DOCS.rglob("*.md")):
        if BANNED.search(path.stem):
            path.unlink()
            continue
        path.write_text(one_platform(path.read_text(encoding="utf-8")), encoding="utf-8")
        rows.append((path.relative_to(ROOT).as_posix(), *describe(path, metas.get(path, {}))))
    for folder in sorted(DOCS.rglob("*"), reverse=True):
        if folder.is_dir() and not any(folder.iterdir()):
            folder.rmdir()

    left = [path for path in DOCS.rglob("*.md") if BANNED.search(path.read_text(encoding="utf-8"))]
    if left:
        sys.exit("still names another platform:\n" + "\n".join(str(path) for path in left))

    write_claude_md(rows, pins, commit)
    if option("--removed"):
        Path(option("--removed")).write_text("\n\n----\n\n".join(removed), encoding="utf-8")
    print(f"{len(rows)} pages, {len(removed)} passages removed")


if __name__ == "__main__":
    main()
