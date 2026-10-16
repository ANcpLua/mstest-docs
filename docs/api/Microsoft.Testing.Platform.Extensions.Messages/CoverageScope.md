# CoverageScope struct

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Identifies the entity a coverage measurement or threshold describes. Scope levels form overlapping dimensions rather than a single parent hierarchy (a file can contain many types and a partial type can span many files), so this models scope identity, not a forced tree.

```csharp
public readonly struct CoverageScope : IEquatable<CoverageScope>
```

## Constructors

### CoverageScope

```csharp
public CoverageScope(
    CoverageScopeLevel level,
    string? name = null,
    string? containerHint = null)
```

Initializes a new instance of the `CoverageScope` struct.

**Parameters:**

- `level`: The granularity of the scope.
- `name`: The scope identifier (module path, type name, file path…); must be null for `CoverageScopeLevel.Overall` and non-empty otherwise.
- `containerHint`: Optional, non-authoritative grouping hint for UIs.

## Properties

### ContainerHint

```csharp
public string? ContainerHint { get; }
```

Gets an optional, non-authoritative grouping hint for UIs (e.g. the assembly of a type, or a representative file of a type). It is deliberately **not** a tree edge: a file can contain many types and a partial type can span many files, so scope levels form overlapping dimensions rather than a single parent hierarchy. Consumers that need exact containment should read the referenced report artifact (see `TestCoverageReportMessage`), which carries the authoritative structure.

### Level

```csharp
public CoverageScopeLevel Level { get; }
```

Gets the granularity of this scope.

### Name

```csharp
public string? Name { get; }
```

Gets the scope identifier (module path, type name, file path…); null only for `CoverageScopeLevel.Overall`.

### Overall

```csharp
public static CoverageScope Overall { get; }
```

Gets the whole-run scope.

## Methods

### Equals

```csharp
public bool Equals(CoverageScope other)
```

```csharp
public override bool Equals(object? obj)
```

### GetHashCode

```csharp
public override int GetHashCode()
```

## Operators

### Equality

```csharp
public static bool operator Equality(CoverageScope left, CoverageScope right)
```

Compares two `CoverageScope` values for equality.

**Parameters:**

- `left`: The first value.
- `right`: The second value.

**Returns:** `true` when the two values are equal.

### Inequality

```csharp
public static bool operator Inequality(CoverageScope left, CoverageScope right)
```

Compares two `CoverageScope` values for inequality.

**Parameters:**

- `left`: The first value.
- `right`: The second value.

**Returns:** `true` when the two values are not equal.
