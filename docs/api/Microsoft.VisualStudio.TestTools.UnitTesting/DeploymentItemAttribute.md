# DeploymentItemAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.Extensions.dll`
- Package: `MSTest.TestFramework` 4.5.1

Used to specify a deployment item (file or directory) for per-test deployment. The specified files and folders are copied to the `TestContext`.DeploymentDirectory, which is the directory from which the test assembly is executed and where all deployment items are present alongside the test source DLL. Can be specified on a test class or a test method. Can have multiple instances of the attribute to specify more than one item. The item path can be absolute or relative; if relative, it's resolved against the build output directory (the folder that contains the test assembly).

```csharp
[AttributeUsage(AttributeTargets.Class | AttributeTargets.Method, AllowMultiple = true)]
public sealed class DeploymentItemAttribute : Attribute
```

## Remarks

If specified on a test class, the class needs to contain at least one test method. This means that the attribute cannot be combined with a test class that would contain only an AssemblyInitialize or ClassInitialize method.

## Example

```csharp
[DeploymentItem("file1.xml")] // Copy file1.xml from the build output directory to the deployment directory.
[DeploymentItem("Resources/file2.xml", "DataFiles")] // Copy file2.xml from the Resources subfolder into a DataFiles subfolder of the deployment directory.
[DeploymentItem("TestFiles/")] // Copy all files and subfolders of the TestFiles folder to the deployment directory.
```

## Constructors

### DeploymentItemAttribute

```csharp
public DeploymentItemAttribute(string? path)
```

Initializes a new instance of the `DeploymentItemAttribute` class.

**Parameters:**

- `path`: The file or directory to deploy. The path is relative to the build output directory. The item will be copied to the same directory as the deployed test assemblies.

```csharp
public DeploymentItemAttribute(string? path, string? outputDirectory)
```

Initializes a new instance of the `DeploymentItemAttribute` class.

**Parameters:**

- `path`: The relative or absolute path to the file or directory to deploy. The path is relative to the build output directory. The item will be copied to the same directory as the deployed test assemblies.
- `outputDirectory`: The path of the directory to which the items are to be copied. It can be either absolute or relative to the deployment directory. All files and directories identified by `path` will be copied to this directory.

## Properties

### OutputDirectory

```csharp
public string? OutputDirectory { get; }
```

Gets the path of the directory to which the item is copied.

### Path

```csharp
public string? Path { get; }
```

Gets the path of the source file or folder to be copied.
