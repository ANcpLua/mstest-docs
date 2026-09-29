# ExecutableConditionAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

This attribute is used to conditionally control whether a test class or a test method will run or be ignored, based on whether a given executable (tool) is available.

```csharp
[AttributeUsage(AttributeTargets.Class | AttributeTargets.Method, Inherited = false, AllowMultiple = true)]
public sealed class ExecutableConditionAttribute : ConditionBaseAttribute
```

## Remarks

This is a generic, tool-agnostic condition. There are two modes:

- When no `ExecutableConditionAttribute.Arguments` are supplied, the condition only checks that the executable is *discoverable* on the system `PATH` (and, on Windows, resolvable through `PATHEXT`). It does not run the executable. For example, it can verify that `docker` is installed.
- When `ExecutableConditionAttribute.Arguments` are supplied, the condition runs `executable arguments` and is met only when the process exits with code `0` within `ExecutableConditionAttribute.TimeoutSeconds`. For example, `[ExecutableCondition("docker", "version")]` verifies that the Docker CLI actually responds. The process output is redirected and discarded, and the process (together with its child process tree, where the runtime supports it) is terminated if it exceeds the timeout.

Product-specific state (for example whether the Docker daemon is configured for Linux containers) is intentionally out of scope; layer such checks on top of this attribute or author your own `ConditionBaseAttribute`.

Executable availability depends on the runtime environment, including its `PATH`, so a missing or misspelled executable cannot be validated statically and is evaluated immediately before the test executes.

Each distinct executable-and-arguments combination forms its own condition group (see `ExecutableConditionAttribute.GroupName`). As a result, applying the attribute multiple times with different commands requires *all* of them to be satisfied (logical AND), while applying it multiple times with the same command requires only one to match (logical OR).

This attribute isn't inherited. Applying it to a base class will not affect derived classes.

## Constructors

### ExecutableConditionAttribute

```csharp
public ExecutableConditionAttribute(string executable)
```

Initializes a new instance of the `ExecutableConditionAttribute` class that includes the test only when the given executable is available on `PATH`.

**Parameters:**

- `executable`: The executable to look for. This is typically a bare command name (for example `docker`), but a path containing a directory separator is also supported, in which case it is checked directly instead of being resolved against `PATH`.

```csharp
public ExecutableConditionAttribute(ConditionMode mode, string executable)
```

Initializes a new instance of the `ExecutableConditionAttribute` class that checks whether the given executable is available on `PATH`.

**Parameters:**

- `mode`: Decides whether the test is included or excluded when the executable is available.
- `executable`: The executable to look for. This is typically a bare command name (for example `docker`), but a path containing a directory separator is also supported, in which case it is checked directly instead of being resolved against `PATH`.

```csharp
public ExecutableConditionAttribute(string executable, params string[] arguments)
```

Initializes a new instance of the `ExecutableConditionAttribute` class that includes the test only when the given command is available.

**Parameters:**

- `executable`: The executable to look for. This is typically a bare command name (for example `docker`), but a path containing a directory separator is also supported, in which case it is checked directly instead of being resolved against `PATH`.
- `arguments`: Optional arguments. When omitted, only the presence of `executable` on `PATH` is checked. When provided, `executable arguments` is executed and the condition is met only if it exits with code 0.

```csharp
public ExecutableConditionAttribute(
    ConditionMode mode,
    string executable,
    params string[] arguments)
```

Initializes a new instance of the `ExecutableConditionAttribute` class.

**Parameters:**

- `mode`: Decides whether the test is included or excluded when the command is available.
- `executable`: The executable to look for. This is typically a bare command name (for example `docker`), but a path containing a directory separator is also supported, in which case it is checked directly instead of being resolved against `PATH`.
- `arguments`: Optional arguments. When omitted, only the presence of `executable` on `PATH` is checked. When provided, `executable arguments` is executed and the condition is met only if it exits with code 0.

## Properties

### Arguments

```csharp
public IReadOnlyList<string> Arguments { get; }
```

Gets the arguments passed to the executable. When empty, only the presence of the executable on `PATH` is checked; otherwise the executable is run with these arguments and must exit with code 0.

### Executable

```csharp
public string Executable { get; }
```

Gets the executable that this condition looks for.

### GroupName

```csharp
public override string GroupName { get; }
```

Gets the group name for this attribute. Each command -- combined with `ConditionBaseAttribute.Mode` -- forms its own group, so requiring several different commands is combined with a logical AND, while the same command with opposite modes does not silently cancel out (mirroring `MemberConditionAttribute`).

#### Remarks

The two evaluation modes are prefixed (`presence` vs `run`) and segments are separated with the null character, which can't appear in an executable name or argument. This keeps the presence check for an executable literally named `"foo bar"` distinct from running `foo` with argument `bar`. `ExecutableConditionAttribute.TimeoutSeconds` is intentionally excluded so the same command with different timeouts still groups together (logical OR); it is instead part of `ExecutableConditionAttribute.CacheKey` so a different timeout re-evaluates.

### IsConditionMet

```csharp
public override bool IsConditionMet { get; }
```

Gets a value indicating whether the condition is met. The implementation of this property shouldn't read the `ConditionBaseAttribute.Mode` property.

### TimeoutSeconds

```csharp
public int TimeoutSeconds { get; set; }
```

Gets or sets the maximum number of seconds to wait for the executable to exit when `ExecutableConditionAttribute.Arguments` are provided. A value less than or equal to 0 means no timeout. The default is 30 seconds.
