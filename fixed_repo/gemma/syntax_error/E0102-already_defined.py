#!/usr/bin/env python3

"""
Stanford Bluescreen Example
Shows front and back strategies.
The functions are mostly complete,
missing only the key if-logic line.
"""

import sys
from PIL import Image

class SimpleImage:
    """
    A wrapper class for PIL Image to facilitate pixel manipulation.
    """
    def __init__(self, filename):
        """
        Initialize the SimpleImage with a given filename.
        Load the image and get its size.
        """
        self.image = Image.open(filename)
        self.pixels = self.image.load()
        self.width, self.height = self.image.size

    def get_pixel(self, x, y):
        """
        Get the pixel value at the given (x, y) coordinates.
        """
        return self.pixels[x, y]

    def set_pixel(self, x, y, color):
        """
        Set the pixel value at the given (x, y) coordinates.
        """
        self.pixels[x, y] = color

    def in_bounds(self, x, y):
        """
        Check if the given (x, y) coordinates are within the image bounds.
        """
```python
"""
SimpleImage processing utilities.
"""
def in_bounds(x, y, image):
    """
    Checks if pixel coordinates are within the image boundaries.

    Args:
        x (int): The x coordinate of the pixel.
        y (int): The y coordinate of the pixel.
        image (SimpleImage): The image to check.

    Returns:
        bool: True if the pixel is within bounds, False otherwise.
    """
    return 0 <= x < image.width and 0 <= y < image.height

def show(image):
    """
    Display the image.
    """
    image.show()
                if in_bounds(dest_x, dest_y, back):
