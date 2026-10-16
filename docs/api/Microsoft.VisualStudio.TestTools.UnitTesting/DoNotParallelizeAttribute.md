# DoNotParallelizeAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

Excludes a test, test class, or test assembly from in-assembly parallelization. Affected tests never run concurrently with any other test in the same test source and, when parallelization is enabled, are deferred to run sequentially after every parallelizable test in that source has finished.

```csharp
[AttributeUsage(AttributeTargets.Assembly | AttributeTargets.Class | AttributeTargets.Method)]
public class DoNotParallelizeAttribute : Attribute
```

## Remarks

The attribute provides two guarantees at once, and the second is easy to overlook:

*Mutual exclusion.* A test carrying this attribute — directly, or through its class or its assembly — is never executed at the same time as any other test in the same source. It runs on its own.

*Deferral.* When in-assembly parallelization is enabled, the scheduler partitions a source's tests into a parallelizable set and a non-parallelizable set. It runs the entire parallelizable set to completion first, and only then runs the non-parallelizable set — one test at a time — at the very end of that source's run. Because partitioning is per test source (assembly), "runs last" and "runs alone" are guarantees relative to the other tests in that same source; a run that spans several sources has a separate deferred tail for each one.

This makes the attribute's cost easy to underestimate. A deferred test cannot overlap with any other test in the same source, so its duration is *added to* that source's critical path rather than absorbed by parallel work happening alongside it. A single slow test carrying this attribute is therefore disproportionately expensive within its source: it lengthens that source's run by roughly its own duration, on top of never running in parallel with any other test in the source. (It can still overlap with tests from *other* sources, which may run in separate hosts, so this cost is to the source's critical path rather than necessarily to the whole run.)

Because the deferred tests run only after the parallelizable set has finished, a run that is canceled or aborted during the parallelizable phase can complete without executing any of them: "runs last" and "may not run at all when the run is canceled early" are both true.

*No effect when parallelization is off.* MSTest does not parallelize by default; in-assembly parallelization is opt-in via `ParallelizeAttribute` (`[assembly: Parallelize]`), the equivalent run settings, or the `MSTestParallelizeScope` / `MSTestParallelizeWorkers` MSBuild properties. When parallelization is not enabled every test already runs sequentially, so this attribute is inert — there is nothing to opt out of.

The attribute can be applied at three levels:

- *Assembly* — every test in the assembly is excluded from parallelization, equivalent to disabling parallelization for that assembly.
- *Class* — every test in the class is excluded; the class's tests run sequentially in the deferred phase.
- *Method* — only the annotated test is excluded and deferred; the rest of its class can still run in parallel.

This is a coarse control: it opts a test out of parallelism entirely. When only a specific shared resource is contended, prefer `ResourceLockAttribute`, which serializes just the tests that declare the same resource instead of excluding them from parallelization altogether. If a test carries both attributes, `DoNotParallelizeAttribute` takes precedence and the declared resource locks have no effect: such tests run in the sequential phase and never pass through the parallel scheduler that acquires locks.

## Constructors

### DoNotParallelizeAttribute

```csharp
public DoNotParallelizeAttribute()
```
