# DataSourceAttribute class

- Namespace: `Microsoft.VisualStudio.TestTools.UnitTesting`
- Assembly: `MSTest.TestFramework.dll`
- Package: `MSTest.TestFramework` 4.4.1

Specifies connection string, table name and row access method for data driven testing.

```csharp
[AttributeUsage(AttributeTargets.Method, Inherited = false)]
public sealed class DataSourceAttribute : Attribute
```

## Remarks

- This works only on .NET Framework and is not supported on .NET Core or later.
- The following shows example usages for this attribute: ```csharp [DataSource("Provider=SQLOLEDB.1;Data Source=source;Integrated Security=SSPI;Initial Catalog=EqtCoverage;Persist Security Info=False", "MyTable")] [DataSource("dataSourceNameFromConfigFile")]. ```

## Constructors

### DataSourceAttribute

```csharp
public DataSourceAttribute(string dataSourceSettingName)
```

Initializes a new instance of the `DataSourceAttribute` class. This instance will be initialized with a data provider and connection string associated with the setting name.

**Parameters:**

- `dataSourceSettingName`: The name of a data source found in the <microsoft.visualstudio.qualitytools> section in the app.config file.

```csharp
public DataSourceAttribute(string connectionString, string tableName)
```

Initializes a new instance of the `DataSourceAttribute` class.This instance will be initialized with a connection string and table name. Specify connection string and data table to access OLEDB data source.

**Parameters:**

- `connectionString`: Data provider specific connection string. WARNING: The connection string can contain sensitive data (for example, a password). The connection string is stored in plain text in source code and in the compiled assembly. Restrict access to the source code and assembly to protect this sensitive information.
- `tableName`: The name of the data table.

```csharp
public DataSourceAttribute(
    string providerInvariantName,
    string connectionString,
    string tableName,
    DataAccessMethod dataAccessMethod)
```

Initializes a new instance of the `DataSourceAttribute` class. This instance will be initialized with a data provider, connection string, data table and data access method to access the data source.

**Parameters:**

- `providerInvariantName`: Invariant data provider name, such as System.Data.SqlClient.
- `connectionString`: Data provider specific connection string. WARNING: The connection string can contain sensitive data (for example, a password). The connection string is stored in plain text in source code and in the compiled assembly. Restrict access to the source code and assembly to protect this sensitive information.
- `tableName`: The name of the data table.
- `dataAccessMethod`: Specifies the order to access data.

## Fields

### DefaultDataAccessMethod

```csharp
public static readonly DataAccessMethod DefaultDataAccessMethod
```

The default data access method.

### DefaultProviderName

```csharp
public static readonly string DefaultProviderName
```

The default provider name for DataSource.

## Properties

### ConnectionString

```csharp
public string? ConnectionString { get; }
```

Gets a value representing the connection string for the data source.

### DataAccessMethod

```csharp
public DataAccessMethod DataAccessMethod { get; }
```

Gets the method used to access the data source.

### DataSourceSettingName

```csharp
public string? DataSourceSettingName { get; }
```

Gets the name of a data source found in the <microsoft.visualstudio.qualitytools> section in the app.config file.

### ProviderInvariantName

```csharp
public string ProviderInvariantName { get; }
```

Gets a value representing the data provider of the data source.

### TableName

```csharp
public string? TableName { get; }
```

Gets a value indicating the table name providing data.
