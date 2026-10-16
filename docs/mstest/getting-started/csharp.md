# Get started with C# and MSTest

This tutorial takes you through an interactive experience building a sample solution step-by-step to learn unit testing concepts. If you prefer to follow the tutorial using a pre-built solution, [view or download the sample code](https://github.com/dotnet/samples/blob/main/core/getting-started/unit-testing-using-mstest/) before you begin. For download instructions, see [Samples and Tutorials](https://learn.microsoft.com/en-us/dotnet/samples-and-tutorials/#view-and-download-samples).

This article is about testing a .NET Core project. If you're testing an ASP.NET Core project, see [Integration tests in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/test/integration-tests#test-app-prerequisites).

## Prerequisites

- The latest [.NET SDK](https://dotnet.microsoft.com/download)
- [Visual Studio Code](https://code.visualstudio.com) editor
- The [C# DevKit](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csdevkit)

## Create the source project

Open a shell window. Create a directory called *unit-testing-using-mstest* to hold the solution. Inside this new directory, run [`dotnet new sln`](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-new) to create a new solution file for the class library and the test project. Create a *PrimeService* directory. The following outline shows the directory and file structure thus far:

```console
/unit-testing-using-mstest
    unit-testing-using-mstest.sln
    /PrimeService
```

Make *PrimeService* the current directory and run [`dotnet new classlib`](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-new) to create the source project. Rename *Class1.cs* to *PrimeService.cs*. Replace the code in the file with the following code to create a failing implementation of the `PrimeService` class:

```csharp
using System;

namespace Prime.Services
{
    public class PrimeService
    {
        public bool IsPrime(int candidate)
        {
            throw new NotImplementedException("Please create a test first.");
        }
    }
}
```

Change the directory back to the *unit-testing-using-mstest* directory. Run [`dotnet sln add`](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-sln) to add the class library project to the solution:

```dotnetcli
dotnet sln add PrimeService/PrimeService.csproj
```

## Create the test project

Create the *PrimeService.Tests* directory. The following outline shows the directory structure:

```console
/unit-testing-using-mstest
    unit-testing-using-mstest.sln
    /PrimeService
        Source Files
        PrimeService.csproj
    /PrimeService.Tests
```

Make the *PrimeService.Tests* directory the current directory and create a new project using [`dotnet new mstest`](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-new). The dotnet new command creates a test project that uses MSTest as the test library. The template configures the test runner in the *PrimeServiceTests.csproj* file:

```xml
<ItemGroup>
  <PackageReference Include="MSTest" Version="4.5.1" />
</ItemGroup>
```

The test project requires other packages to create and run unit tests. `dotnet new` in the previous step added the necessary MSTest packages and tools for code coverage reporting.

Add the `PrimeService` class library as another dependency to the project. Use the [`dotnet reference add`](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-reference-add) command:

```dotnetcli
dotnet reference add ../PrimeService/PrimeService.csproj
```

You can see the entire file in the [samples repository](https://github.com/dotnet/samples/blob/main/core/getting-started/unit-testing-using-mstest/PrimeService.Tests/PrimeService.Tests.csproj) on GitHub.

The following outline shows the final solution layout:

```console
/unit-testing-using-mstest
    unit-testing-using-mstest.sln
    /PrimeService
        Source Files
        PrimeService.csproj
    /PrimeService.Tests
        Test Source Files
        PrimeServiceTests.csproj
```

Change to the *unit-testing-using-mstest* directory, and run [`dotnet sln add`](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-sln):

```dotnetcli
dotnet sln add ./PrimeService.Tests/PrimeService.Tests.csproj
```

## Create the first test

Write a failing test, make it pass, then repeat the process. Remove *UnitTest1.cs* from the *PrimeService.Tests* directory and create a new C# file named *PrimeService_IsPrimeShould.cs* with the following content:

```csharp
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Prime.Services;

namespace Prime.UnitTests.Services
{
    [TestClass]
    public class PrimeService_IsPrimeShould
    {
        private readonly PrimeService _primeService;

        public PrimeService_IsPrimeShould()
        {
            _primeService = new PrimeService();
        }

        [TestMethod]
        public void IsPrime_InputIs1_ReturnFalse()
        {
            bool result = _primeService.IsPrime(1);

            Assert.IsFalse(result, "1 shouldn't be prime");
        }
    }
}
```

The [TestClass attribute](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestClassAttribute.md) denotes a class that contains unit tests. The [TestMethod attribute](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestMethodAttribute.md) indicates a method is a test method.

Save this file and execute [`dotnet test`](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-test) to build the tests and the class library and then run the tests. The MSTest test runner contains the program entry point to run your tests. `dotnet test` starts the test runner using the unit test project you created.

Your test fails because you didn't create the implementation yet. Make this test pass by writing the simplest code in the `PrimeService` class that works:

```csharp
public bool IsPrime(int candidate)
{
    if (candidate == 1)
    {
        return false;
    }
    throw new NotImplementedException("Please create a test first.");
}
```

In the *unit-testing-using-mstest* directory, run `dotnet test` again. The `dotnet test` command runs a build for the `PrimeService` project and then for the `PrimeService.Tests` project. After building both projects, it runs this single test. It passes.

## Add more features

Now that you made one test pass, it's time to write more. There are a few other simple cases for prime numbers: 0, -1. You could add new tests with the [TestMethod attribute](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/TestMethodAttribute.md), but that quickly becomes tedious. There are other MSTest attributes that enable you to write a suite of similar tests. A test method can execute the same code but have different input arguments. You can use the [DataRow attribute](../../api/Microsoft.VisualStudio.TestTools.UnitTesting/DataRowAttribute.md) to specify values for those inputs.

Instead of creating new tests, apply these two attributes to create a single data driven test. The data driven test is a method that tests several values less than two, which is the lowest prime number. Add a new test method in *PrimeService_IsPrimeShould.cs*:

```csharp
[TestMethod]
[DataRow(-1)]
[DataRow(0)]
[DataRow(1)]
public void IsPrime_ValuesLessThan2_ReturnFalse(int value)
{
    bool result = _primeService.IsPrime(value);

    Assert.IsFalse(result, $"{value} should not be prime");
}
```

Run `dotnet test`, and two of these tests fail. To make all of the tests pass, change the `if` clause at the beginning of the `IsPrime` method in the *PrimeService.cs* file:

```csharp
if (candidate < 2)
```

Continue to iterate by adding more tests, more theories, and more code in the main library. You have the [finished version of the tests](https://github.com/dotnet/samples/blob/main/core/getting-started/unit-testing-using-mstest/PrimeService.Tests/PrimeService_IsPrimeShould.cs) and the [complete implementation of the library](https://github.com/dotnet/samples/blob/main/core/getting-started/unit-testing-using-mstest/PrimeService/PrimeService.cs).

You built a small library and a set of unit tests for that library. You structured the solution so that adding new packages and tests is part of the normal workflow. You concentrated most of your time and effort on solving the goals of the application.

## See also

- [`UnitTesting`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.visualstudio.testtools.unittesting?view=mstest-net-4.5)
- [Use the MSTest framework in unit tests](https://learn.microsoft.com/en-us/visualstudio/test/using-microsoft-visualstudio-testtools-unittesting-members-in-unit-tests)
- [MSTest V2 test framework docs](https://github.com/Microsoft/testfx-docs)
