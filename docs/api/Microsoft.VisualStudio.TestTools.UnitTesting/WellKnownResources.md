# WellKnownResources class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

Well-known resource keys for common process-global state, for use with `ResourceLockAttribute`. These are plain string constants: they use the exact same equality-based conflict mechanism as any user-invented key, and are provided only so that tests contending on the same ambient state agree on a spelling.

```csharp
public static class WellKnownResources
```

## Fields

### Console

```csharp
public const string Console = "System.Console"
```

A key representing the process-wide console (`Console` streams, encoding, colors and cursor).

### CurrentDirectory

```csharp
public const string CurrentDirectory = "System.Environment.CurrentDirectory"
```

A key representing the process-wide current working directory (`Directory.GetCurrentDirectory` / `Environment.CurrentDirectory`).

### EnvironmentVariables

```csharp
public const string EnvironmentVariables = "System.Environment.Variables"
```

A key representing process-wide environment variables (`Environment.GetEnvironmentVariable(String)` / `Environment.SetEnvironmentVariable(String,String)`). Use this coarse key for variables whose blast radius you cannot bound, such as `PATH`, which is inherited by child processes.
