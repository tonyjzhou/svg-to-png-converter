
# SVG to PNG Converter

A simple Python script to convert SVG files in a given directory to PNG files.

## Requirements
- `cairosvg`: You can install it via pip:
  ```
  pip install cairosvg
  ```

## Usage
Run the script and provide the path to the directory containing the SVG files:
```
python convert_svg_to_png.py
```

## Testing
Two test functions are provided in the `tests/test_conversion.py` file:
- `test_convert_single_svg()`: Tests conversion of a single SVG file.
- `test_convert_multiple_svgs()`: Tests conversion of multiple SVG files in a directory.
