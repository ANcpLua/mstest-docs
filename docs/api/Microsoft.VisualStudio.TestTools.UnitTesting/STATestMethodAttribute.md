# STATestMethodAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

The test class attribute.

```csharp
[AttributeUsage(AttributeTargets.Method)]
public class STATestMethodAttribute : TestMethodAttribute
```

## Constructors

### STATestMethodAttribute

```csharp
public STATestMethodAttribute(TestMethodAttribute testMethodAttribute)
```

Initializes a new instance of the `STATestMethodAttribute` class. This constructor is intended to be called by `STATestClassAttribute` (or derived) to wrap an existing test method attribute. It can also be called by a derived `STATestMethodAttribute` which will be called by a derived `STATestClassAttribute`.

**Parameters:**

- `testMethodAttribute`: The wrapped test method.

```csharp
public STATestMethodAttribute([CallerFilePath] string callerFilePath = "", [CallerLineNumber] int callerLineNumber = -1)
```

Initializes a new instance of the `STATestMethodAttribute` class.

## Properties

### UseSTASynchronizationContext

```csharp
public bool UseSTASynchronizationContext { get; set; }
```

Gets or sets a value indicating whether the attribute will set a `SynchronizationContext` that preserves the same STA thread for async continuations. The default is `false`.

## Methods

### ExecuteAsync

```csharp
public override Task<TestResult[]> ExecuteAsync(ITestMethod testMethod)
```

Executes a test method.

**Parameters:**

- `testMethod`: The test method to execute.

**Returns:** An array of TestResult objects that represent the outcome(s) of the test.

#### Remarks

Extensions can override this method to customize running a TestMethod.

### ExecuteCoreAsync

```csharp
protected virtual Task<TestResult[]> ExecuteCoreAsync(ITestMethod testMethod)
```

The core execution of STA test method, which happens on the STA thread.

**Parameters:**

- `testMethod`: The test method to execute.

**Returns:** The test results of the test method.
