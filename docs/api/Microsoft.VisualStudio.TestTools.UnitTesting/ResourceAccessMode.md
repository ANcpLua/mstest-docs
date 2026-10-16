# ResourceAccessMode enum

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

Specifies how a test accesses a resource declared with `ResourceLockAttribute`.

```csharp
public enum ResourceAccessMode
```

## Remarks

`ResourceAccessMode.ReadWrite` is deliberately the zero value, so that a default-initialized `ResourceAccessMode` is the exclusive (safe) mode. Under-locking produces flaky races, while over-locking merely runs slower, so any unspecified value must fail closed.

## Fields

| Name | Value | Description |
| --- | --- | --- |
| `ReadWrite` | `0` | The test reads and writes the resource. The lock is exclusive: it blocks against all other readers and writers of the same resource. This is the default. |
| `Read` | `1` | The test only reads the resource. Read locks run concurrently with each other and block only against a `ResourceAccessMode.ReadWrite` holder. |
