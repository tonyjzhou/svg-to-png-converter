
import os
from convert_svg_to_png import convert_svg_to_png

def test_convert_single_svg():
    test_directory = "/path/to/test/svg/files"
    test_svg = "test.svg"
    test_png = "test.png"

    # Assuming the test SVG file exists in the directory
    convert_svg_to_png(test_directory)

    # Check if the PNG file is created
    assert os.path.exists(os.path.join(test_directory, test_png))

    # Clean up (optional)
    os.remove(os.path.join(test_directory, test_png))

def test_convert_multiple_svgs():
    test_directory = "/path/to/test/svg/files"

    # Assuming multiple test SVG files exist in the directory
    convert_svg_to_png(test_directory)

    # Check if the corresponding PNG files are created
    for filename in os.listdir(test_directory):
        if filename.endswith(".svg"):
            png_path = os.path.join(test_directory, filename[:-3] + "png")
            assert os.path.exists(png_path)

            # Clean up (optional)
            os.remove(png_path)
