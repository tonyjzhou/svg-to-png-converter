
import cairosvg
import os

def convert_svg_to_png(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".svg"):
            svg_path = os.path.join(directory, filename)
            png_path = os.path.join(directory, filename[:-3] + "png")
            cairosvg.svg2png(url=svg_path, write_to=png_path)
            print(f"Converted {filename} to PNG")

if __name__ == "__main__":
    directory = input("Enter the path to the directory containing SVG files: ")
    convert_svg_to_png(directory)
