from PIL import Image
import sys

image_path = sys.argv[1]


def count_pixels(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Get the dimensions of the image
        width, height = img.size
        # Calculate the total number of pixels
        total_pixels = width * height
        print(total_pixels)

# Example usage
count_pixels(image_path)
