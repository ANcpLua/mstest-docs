# DynamicDataSourceType enum

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

Enum to specify whether the data is stored as property, in method, or in field.

```csharp
public enum DynamicDataSourceType
```

## Fields

| Name | Value | Description |
| --- | --- | --- |
| `Property` | `0` | Data is declared as property. |
| `Method` | `1` | Data is declared in method. |
| `AutoDetect` | `2` | The data source type is auto-detected. |
| `Field` | `3` | Data is declared as field. |
