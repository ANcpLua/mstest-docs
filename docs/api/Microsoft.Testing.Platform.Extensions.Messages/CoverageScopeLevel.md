# CoverageScopeLevel enum

- Namespace: `Microsoft.Testing.Platform.Extensions.Messages`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.4.1

The entity a coverage / threshold entry describes. Append-only.

```csharp
public enum CoverageScopeLevel
```

## Fields

| Name | Value | Description |
| --- | --- | --- |
| `Overall` | `0` | The whole run. |
| `Module` | `1` | A module (assembly file on disk). |
| `Assembly` | `2` | An assembly. |
| `Namespace` | `3` | A namespace. |
| `Type` | `4` | A type. |
| `File` | `5` | A source file. |
