# TreeNodeFilter class

- Namespace: `Microsoft.Testing.Platform.Requests`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

A tree based filter for test execution.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public sealed class TreeNodeFilter : ITestExecutionFilter
```

## Remarks

This API is experimental. It may change, break, or be removed at any time without notice.

## Fields

### PathSeparator

```csharp
public const char PathSeparator = '/'
```

The path separator character.

## Properties

### Filter

```csharp
public string Filter { get; }
```

Gets the filter string.

## Methods

### MatchesFilter

```csharp
public bool MatchesFilter(string testNodeFullPath, PropertyBag filterableProperties)
```

Checks whether a node path matches the tree node filter.

**Parameters:**

- `testNodeFullPath`: The segment URL encoded path.
- `filterableProperties`: The URL encoded node properties.
