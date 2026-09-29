# AssemblyFixtureProviderAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

Indicates that the methods on the specified `AssemblyFixtureProviderAttribute.FixtureType` annotated with `AssemblyInitializeAttribute` or `AssemblyCleanupAttribute` should be discovered and executed once per consuming test assembly, even when the methods are not declared in that test assembly itself.

```csharp
[AttributeUsage(AttributeTargets.Assembly, AllowMultiple = true, Inherited = false)]
public sealed class AssemblyFixtureProviderAttribute : Attribute
```

## Remarks

Apply this attribute at the assembly level on the library that exposes the shared fixture. Every test assembly that ends up loading the library at runtime will then pick up its `AssemblyInitializeAttribute` / `AssemblyCleanupAttribute` methods without the test project needing to declare anything itself.

If the consuming test assembly already declares its own `AssemblyInitializeAttribute` or `AssemblyCleanupAttribute` method, the local declaration always wins; methods contributed via `AssemblyFixtureProviderAttribute` only fill empty slots.

The attribute can be applied multiple times on the same assembly to expose more than one fixture type. The attribute can also be applied on the consuming test assembly itself to opt into fixtures defined in a third-party library that cannot be modified.

## Example

```csharp
// In Contoso.TestInfra.dll
[assembly: AssemblyFixtureProvider(typeof(GlobalFixtures))]
            
public static class GlobalFixtures
{
    [AssemblyInitialize]
    public static void Init(TestContext context) { /* ... */ }
            
    [AssemblyCleanup]
    public static void Cleanup() { /* ... */ }
}
```

## Constructors

### AssemblyFixtureProviderAttribute

```csharp
public AssemblyFixtureProviderAttribute(Type fixtureType)
```

Initializes a new instance of the `AssemblyFixtureProviderAttribute` class.

**Parameters:**

- `fixtureType`: The type whose `AssemblyInitializeAttribute` and `AssemblyCleanupAttribute` methods should be exposed to assemblies referencing the assembly carrying this attribute.

## Properties

### FixtureType

```csharp
public Type FixtureType { get; }
```

Gets the type whose `AssemblyInitializeAttribute` and `AssemblyCleanupAttribute` methods are exposed.
