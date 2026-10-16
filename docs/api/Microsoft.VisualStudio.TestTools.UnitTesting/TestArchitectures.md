# TestArchitectures enum

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.5.1

An enum that is used with `ArchitectureConditionAttribute` to control which process architectures a test method or test class supports or doesn't support.

```csharp
[Flags]
public enum TestArchitectures
```

## Fields

| Name | Value | Description |
| --- | --- | --- |
| `X86` | `1` | Represents the x86 architecture. |
| `X64` | `2` | Represents the x64 architecture. |
| `Arm` | `4` | Represents the ARM architecture. |
| `Arm64` | `8` | Represents the ARM64 architecture. |
| `Wasm` | `16` | Represents the WebAssembly platform. |
| `S390x` | `32` | Represents the S390x architecture. |
| `LoongArch64` | `64` | Represents the LoongArch64 architecture. |
| `Armv6` | `128` | Represents the 32-bit ARMv6 architecture. |
| `Ppc64le` | `256` | Represents the 64-bit PowerPC little-endian architecture. |
| `RiscV64` | `512` | Represents the 64-bit RISC-V architecture. |
