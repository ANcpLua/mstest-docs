# ITestHostExecutionOrchestratorMiddleware interface

- Namespace: `Microsoft.Testing.Platform.Extensions.TestHostOrchestrator`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents a single-invocation middleware that composes with other middleware around exactly one existing `ITestHostExecutionOrchestrator` invocation.

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
public interface ITestHostExecutionOrchestratorMiddleware : ITestHostOrchestratorExtension, IExtension
```

## Remarks

This is a v1, initial composition boundary for test host execution orchestration. Exactly one `ITestHostExecutionOrchestrator` is still active per run; middleware wraps that single invocation and can only observe or short-circuit it, not replace it with a typed multi-run engine. In particular, this version of the API does not provide repeat/retry-style re-invocation, sharding, phases, protocol metadata, or the ability to mutate identifiers such as attempt number, execution id, or instance id. The existing `--retry-failed-tests` orchestrator is not reentrant and is not extracted or reimplemented as middleware by this API. A typed, multi-run orchestration model (for example a first-class retry/stress/shard engine) is intentionally out of scope for this version and may be introduced later as a separate, additive capability.

Middleware is composed outermost-first in registration order (see `ITestHostExecutionOrchestratorMiddlewareManager.AddTestHostExecutionOrchestratorMiddleware(Func<IServiceProvider,ITestHostExecutionOrchestratorMiddleware>)`). This is an explicit, order-dependent composition: there is no numeric ordering key, and middleware must not assume its effect on the pipeline is commutative with other middleware.

This API is experimental. It may change, break, or be removed at any time without notice.

## Methods

### OrchestrateTestHostExecutionAsync

```csharp
[Experimental("TPEXP", UrlFormat = "https://aka.ms/testingplatform/diagnostics#{0}")]
Task<int> OrchestrateTestHostExecutionAsync(Func<CancellationToken, Task<int>> next, CancellationToken cancellationToken)
```

Orchestrates test host execution by optionally invoking `next` and returning its result unchanged, or by short-circuiting without invoking `next` at all.

**Parameters:**

- `next`: A delegate that invokes the remainder of the pipeline (the next middleware, or the wrapped orchestrator) with the given cancellation token, and returns its exit code.
- `cancellationToken`: The cancellation token.

**Returns:** A task representing the asynchronous operation that returns the test host exit code.

#### Remarks

`next` can be invoked at most once, and the call to `next` must begin before this method returns or throws. The platform rejects a second invocation, as well as an invocation deferred until after this method has returned or thrown. Middleware may start the call synchronously and then await its returned task asynchronously, but it cannot defer the call itself to another thread or callback after returning.

When this method invokes `next` and lets it complete (whether or not it also awaits it directly), the value this method returns must be exactly the downstream exit code: this version of the pipeline does not allow middleware to rewrite the downstream verdict. If the downstream execution faults or is canceled, the exception or cancellation must propagate unchanged; converting it to any exit code, including a non-success exit code, is unsupported and rejected by the platform. A downstream failure must not be swallowed into an apparently successful return from this method. When cancellation is signaled anywhere in the linked cancellation chain, the pipeline rethrows the resulting cancellation and does not allow middleware to replace it with a different exit code.

When this method never invokes `next` at all (short-circuiting the pipeline), the returned exit code must not be a success exit code, so that skipped execution can never be reported as if tests actually ran and passed.

The platform links whatever `CancellationToken` is passed to `next` with the root cancellation token, so passing `CancellationToken.None` does not detach the downstream execution from root cancellation.

This API is experimental. It may change, break, or be removed at any time without notice.
