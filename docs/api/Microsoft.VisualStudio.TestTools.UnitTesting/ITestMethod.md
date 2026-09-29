# ITestMethod interface

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

TestMethod for execution.

```csharp
public interface ITestMethod
```

## Properties

### Arguments

```csharp
object?[]? Arguments { get; }
```

Gets the arguments with which test method is invoked.

### MethodInfo

```csharp
MethodInfo MethodInfo { get; }
```

Gets the methodInfo for test method.

#### Remarks

This is just to retrieve additional information about the method. Do not directly invoke the method using MethodInfo. Use ITestMethod.Invoke instead.

### ParameterTypes

```csharp
ParameterInfo[] ParameterTypes { get; }
```

Gets the parameters of test method.

### ReturnType

```csharp
Type ReturnType { get; }
```

Gets the return type of test method.

### TestClassName

```csharp
string TestClassName { get; }
```

Gets the name of test class.

### TestMethodName

```csharp
string TestMethodName { get; }
```

Gets the name of test method.

## Methods

### GetAllAttributes

```csharp
Attribute[]? GetAllAttributes()
```

Get all attributes of the test method.

**Returns:** All attributes.

### GetAttributes

```csharp
TAttributeType[] GetAttributes<TAttributeType>()
```

Get attribute of specific type.

**Type parameters:**

- `TAttributeType`: System.Attribute type.

**Returns:** The attributes of the specified type.

### InvokeAsync

```csharp
Task<TestResult> InvokeAsync(object[]? arguments)
```

Invokes the test method.

**Parameters:**

- `arguments`: Arguments to pass to test method. (E.g. For data driven).

**Returns:** Result of test method invocation.

#### Remarks

This call handles asynchronous test methods as well.
