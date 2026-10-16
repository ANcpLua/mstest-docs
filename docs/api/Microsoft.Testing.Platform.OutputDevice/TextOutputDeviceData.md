# TextOutputDeviceData class

- Namespace: `Microsoft.Testing.Platform.OutputDevice`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents a text data for directed to the output device.

```csharp
public class TextOutputDeviceData : IOutputDeviceData
```

## Constructors

### TextOutputDeviceData

```csharp
public TextOutputDeviceData(string text)
```

Initializes a new instance of the `TextOutputDeviceData` class with the specified text.

**Parameters:**

- `text`: The text for the output device.

## Properties

### Text

```csharp
public string Text { get; }
```

Gets the text for the output device.
