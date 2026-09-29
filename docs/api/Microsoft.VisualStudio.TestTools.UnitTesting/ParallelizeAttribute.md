# ParallelizeAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

Specification for parallelization level for a test run.

```csharp
[AttributeUsage(AttributeTargets.Assembly)]
public class ParallelizeAttribute : Attribute
```

## Constructors

### ParallelizeAttribute

```csharp
public ParallelizeAttribute()
```

Initializes a new instance of the `ParallelizeAttribute` class.

## Properties

### Scope

```csharp
public ExecutionScope Scope { get; set; }
```

Gets or sets the scope of the parallel run.

#### Remarks

To enable all classes to run in parallel set this to `ExecutionScope.ClassLevel`. To get the maximum parallelization level set this to `ExecutionScope.MethodLevel`.

### Workers

```csharp
public int Workers { get; set; }
```

Gets or sets the number of workers to be used for the parallel run.
