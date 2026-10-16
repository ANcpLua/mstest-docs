# FormattedTextOutputDeviceData class

- Namespace: `Microsoft.Testing.Platform.OutputDevice`
- Assembly: `Microsoft.Testing.Platform.dll`
- Package: `Microsoft.Testing.Platform` 2.5.1

Represents the data for a formatted text output device.

```csharp
public sealed class FormattedTextOutputDeviceData : TextOutputDeviceData
```

## Constructors

### FormattedTextOutputDeviceData

```csharp
public FormattedTextOutputDeviceData(string text)
```

Initializes a new instance of the `FormattedTextOutputDeviceData` class with the specified text.

**Parameters:**

- `text`: The text to be displayed.

## Properties

### BackgroundColor

```csharp
public IColor? BackgroundColor { get; init; }
```

Gets or inits the background color of the text.

### ForegroundColor

```csharp
public IColor? ForegroundColor { get; init; }
```

Gets or inits the foreground color of the text.

### Padding

```csharp
public int? Padding { get; init; }
```

Gets or inits the padding of the message.
