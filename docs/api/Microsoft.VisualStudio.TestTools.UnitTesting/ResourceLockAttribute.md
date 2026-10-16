# ResourceLockAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

Declares that a test or test class contends on a named shared resource, so that the in-assembly parallel scheduler serializes it only against other tests that declare the same resource, instead of forcing whole classes or assemblies to opt out of parallelization with `DoNotParallelizeAttribute`.

```csharp
[AttributeUsage(AttributeTargets.Class | AttributeTargets.Method, AllowMultiple = true, Inherited = true)]
public sealed class ResourceLockAttribute : Attribute
```

## Remarks

The resource is identified by a free-form, opaque string key. Two locks refer to the same resource if and only if their `ResourceLockAttribute.Resource` strings are equal using an ordinal, case-sensitive comparison. Keys are identifiers, not paths: no hierarchical relationship is inferred between them (for example `C:\out` and `C:\out\sub` are unrelated keys). Prefer `const` fields and `WellKnownResources` over inline string literals so that a typo becomes a compile error rather than a silent race.

Locking scope is the current test host process only. This attribute does not coordinate across processes or machines, so it does not make parallel `dotnet test` invocations mutually exclusive.

A lock is acquired before its scheduling chunk starts and released after the chunk finishes, so the chunk - not the individual test method - determines how long a lock is held. What forms a chunk depends on `ParallelizeAttribute.Scope`:

Under `ExecutionScope.ClassLevel` (the default) the chunk is the entire class, so a class-level lock is taken once and held across every test in the class, spanning `[ClassInitialize]` and `[ClassCleanup]`. The chunk's locks are the union of the class's and every method's declared keys, each upgraded to the strongest mode declared anywhere in the class - so under this scope declaring locks on individual methods does not make locking more granular.

Under `ExecutionScope.MethodLevel` the chunk is a single test, so a class-level lock is applied to each test individually and acquired and released per test. Tests from other classes may therefore interleave between two tests of this class, and a resource established in `[ClassInitialize]` is not continuously owned through `[ClassCleanup]`.

In both cases a lock covering a test is held across that test's `[TestInitialize]` and `[TestCleanup]`. When a chunk holds more than one lock, the locks are acquired in ordinal-sorted key order, which makes deadlock impossible.

If a test is also marked `DoNotParallelizeAttribute`, that attribute takes precedence and the declared resource locks have no effect: such tests run in the sequential phase and never pass through the parallel scheduler that acquires locks.

This attribute is inherited: a lock declared on a base test class applies to every class deriving from it, matching `DoNotParallelizeAttribute`. This is the conservative direction - a base fixture that touches a shared resource still touches it from derived classes, and over-locking merely runs slower while under-locking produces races. Note the consequence: a derived class cannot remove an inherited lock, nor weaken an inherited `ResourceAccessMode.ReadWrite` to `ResourceAccessMode.Read`, so under `ExecutionScope.ClassLevel` a lock on a widely-used base class serializes the whole hierarchy. Declare locks on the most derived type that actually needs them.

## Constructors

### ResourceLockAttribute

```csharp
public ResourceLockAttribute(string resource)
```

Initializes a new instance of the `ResourceLockAttribute` class for the specified resource, using `ResourceAccessMode.ReadWrite` access.

**Parameters:**

- `resource`: The opaque key identifying the shared resource.

**Exceptions:**

- `ArgumentNullException`: `resource` is `null`.
- `ArgumentException`: `resource` is empty or whitespace.

## Properties

### Mode

```csharp
public ResourceAccessMode Mode { get; set; }
```

Gets or sets the access mode for the resource. Defaults to `ResourceAccessMode.ReadWrite` (exclusive). Set to `ResourceAccessMode.Read` when the test only reads the resource, so that it can run concurrently with other readers and blocks only against a writer.

### Resource

```csharp
public string Resource { get; }
```

Gets the opaque key identifying the shared resource. Compared using an ordinal, case-sensitive comparison.
