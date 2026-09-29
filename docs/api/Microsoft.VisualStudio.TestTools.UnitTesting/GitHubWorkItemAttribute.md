# GitHubWorkItemAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

GitHubWorkItem attribute; used to specify a GitHub issue associated with this test.

```csharp
[AttributeUsage(AttributeTargets.Method, AllowMultiple = true)]
public sealed class GitHubWorkItemAttribute : WorkItemAttribute
```

## Constructors

### GitHubWorkItemAttribute

```csharp
public GitHubWorkItemAttribute(string url)
```

Initializes a new instance of the `GitHubWorkItemAttribute` class for the GitHub WorkItem Attribute.

**Parameters:**

- `url`: The URL to a GitHub issue, pull request, or discussion.

## Properties

### Url

```csharp
public string Url { get; }
```

Gets the URL to the GitHub issue associated.
