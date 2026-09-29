# DependsOnAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

Declares that a test (or every test of a test class) must not start until one or more other tests have finished, forming a dependency graph that the in-assembly scheduler executes in topological order. Unlike a flat ordering attribute, independent branches of the graph still run in parallel.

```csharp
[AttributeUsage(AttributeTargets.Class | AttributeTargets.Method, AllowMultiple = true, Inherited = false)]
public sealed class DependsOnAttribute : Attribute
```

## Remarks

The attribute declares an edge "this test depends on that test". Applying it several times is how a test declares more than one prerequisite (fan-in); several tests naming the same prerequisite is how a graph fans out. Fan-out is the point of the feature: once the shared prerequisite has passed, every dependent becomes runnable at the same time and the scheduler is free to run them concurrently, subject to `ParallelizeAttribute` and worker availability.

When applied to a class, the dependency applies to every test in that class. When the target is a *type* (rather than a specific method), the edge points at *every* test of that type, so the dependent starts only once all of them have finished.

**Scope.** Dependencies are resolved within a single test source. A target in another assembly cannot be waited on, even though `DependsOnAttribute.ctor(Type)` and `DependsOnAttribute.ctor(Type,String)` will happily accept a type from one: such an edge matches nothing and is reported as an ignored dependency rather than silently ordering anything.

**Failure semantics.** If a prerequisite does not pass, the dependent is *skipped*, not failed, and the skip propagates transitively down the graph. Skipping is the established convention (TestNG's `dependsOnMethods`, TUnit's `[DependsOn]`, pytest-dependency) and it keeps the signal readable: one root cause is reported as one failure plus a set of clearly-labelled skips, instead of a wall of failures. Set `DependsOnAttribute.ProceedOnFailure` to `true` for a dependent that must run anyway -- typically an audit or cleanup test.

**Cycles.** A dependency cycle is a configuration error and is reported before any test in the assembly runs. Every test in the cycle is failed with a message naming the cycle path.

**Interaction with parallelization.** Ordering is enforced regardless of `ParallelizeAttribute.Scope`. Under `ExecutionScope.ClassLevel` (the default) the scheduling unit is the whole class, so dependencies between two classes are honored at class granularity; a dependency between two *methods of the same class* orders them within that class's run. Under `ExecutionScope.MethodLevel` every test is scheduled individually, which gives the most parallelism and the finest ordering. If class-level scheduling would require running two classes before each other (class A's test depends on class B's and vice versa), the declared order is still honored - those classes' tests are run sequentially, in dependency order, and a warning names them - but they lose their parallelism; switching to `ExecutionScope.MethodLevel` gets it back.

A test marked `DoNotParallelizeAttribute` runs in the sequential phase, which happens after the parallel phase. A parallelizable test that depends on such a test is therefore moved into the sequential phase as well (transitively), so that its prerequisite really has run first.

**Data-driven tests.** Naming a test that expands into several test cases (for example via `[DataRow]`) creates an edge to *all* of its cases: the dependent waits for every row and is skipped if any row does not pass. Per-row matching is not supported.

**Inheritance.** A test method declared on a base class runs as a test of every derived test class, and the dependency it declares travels with it: the edge is resolved against the *derived* class, so each derived class gets its own edge between its own copies of the two tests. Dropping the edge there would silently discard the declared ordering in every concrete test class. What `Inherited = false` opts out of is *override* chains: a method that overrides a dependent test without re-declaring the attribute has no dependency, because re-pointing a prerequisite onto a method the author rewrote tends to create edges nobody asked for.

Test dependencies couple tests together and make it impossible to run a dependent in isolation, so they are a poor fit for unit tests. They exist for multi-step integration and end-to-end suites, where re-establishing expensive state in every test is impractical.

## Example

```csharp
[TestClass]
public class CheckoutTests
{
    [TestMethod]
    public void CreateCart() { }
            
    // Fan-out: both of these wait for CreateCart, then may run in parallel with each other.
    [TestMethod]
    [DependsOn(nameof(CreateCart))]
    public void AddItem() { }
            
    [TestMethod]
    [DependsOn(nameof(CreateCart))]
    public void ApplyCoupon() { }
            
    // Fan-in: waits for both.
    [TestMethod]
    [DependsOn(nameof(AddItem))]
    [DependsOn(nameof(ApplyCoupon))]
    public void Checkout() { }
            
    // Runs even when its prerequisite failed.
    [TestMethod]
    [DependsOn(nameof(Checkout), ProceedOnFailure = true)]
    public void WriteAuditRecord() { }
}
```

## Constructors

### DependsOnAttribute

```csharp
public DependsOnAttribute(Type testClass)
```

Initializes a new instance of the `DependsOnAttribute` class declaring a dependency on *every* test of another test class.

**Parameters:**

- `testClass`: The prerequisite test class.

**Exceptions:**

- `ArgumentNullException`: `testClass` is `null`.

```csharp
public DependsOnAttribute(string testMethodName)
```

Initializes a new instance of the `DependsOnAttribute` class declaring a dependency on another test method of the same test class.

**Parameters:**

- `testMethodName`: The name of the prerequisite test method. Use `nameof` so that renaming the method is caught by the compiler.

**Exceptions:**

- `ArgumentNullException`: `testMethodName` is `null`.
- `ArgumentException`: `testMethodName` is empty or whitespace.

```csharp
public DependsOnAttribute(Type testClass, string testMethodName)
```

Initializes a new instance of the `DependsOnAttribute` class declaring a dependency on a specific test method of another test class.

**Parameters:**

- `testClass`: The test class declaring the prerequisite.
- `testMethodName`: The name of the prerequisite test method. Use `nameof` so that renaming the method is caught by the compiler.

**Exceptions:**

- `ArgumentNullException`: `testClass` or `testMethodName` is `null`.
- `ArgumentException`: `testMethodName` is empty or whitespace.

## Properties

### ProceedOnFailure

```csharp
public bool ProceedOnFailure { get; set; }
```

Gets or sets a value indicating whether the dependent still runs when a prerequisite does not pass. Defaults to `false`, meaning the dependent is skipped. Set it to `true` for a test that must run regardless of its prerequisites' outcome, such as an audit or cleanup test; ordering is still enforced.

#### Remarks

The flag is evaluated per dependent test rather than per edge: a test that declares several prerequisites runs past a failure only when *every* one of its declarations sets this to `true`. One declaration left at the default is therefore enough to skip the test when any of its prerequisites does not pass. That conservative direction is deliberate - opting out of waiting on one prerequisite says nothing about the others, and running a test whose remaining preconditions were never established just produces a second, misleading failure.

### TestClass

```csharp
public Type? TestClass { get; }
```

Gets the test class declaring the prerequisite, or `null` when the prerequisite is a method of the same class as the dependent.

### TestMethodName

```csharp
public string? TestMethodName { get; }
```

Gets the name of the prerequisite test method, or `null` when the dependency targets every test of `DependsOnAttribute.TestClass`.
