#!/usr/bin/env python3

"""
Stanford Bluescreen Example
Shows front and back strategies.
The functions are mostly complete,
missing only the key if-logic line.
"""

import sys
from PIL import Image

__all__ = ['SimpleImage', 'undefined_name']  # Undefined variable name in __all__ (E0603)

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
"""
SimpleImage module
"""
This module contains utilities for working with images.
"""

def in_bounds(x, y):
    """
    Check if pixel coordinates are within the image bounds.

    Args:
        x (int): The x coordinate of the pixel.
        y (int): The y coordinate of the pixel.

    Returns:
        bool: True if the pixel is within bounds, False otherwise.
    """
    return 0 <= x < width and 0 <= y < height

def show(image):
    """
    Display the image.
    """
    image.image.show()
    import sys

