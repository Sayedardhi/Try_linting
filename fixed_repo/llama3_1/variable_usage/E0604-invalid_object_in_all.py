#!/usr/bin/env python3

"""
Stanford Bluescreen Example
Shows front and back strategies.
The functions are mostly complete,
missing only the key if-logic line.
"""

import sys
from PIL import Image

__all__ = ['SimpleImage', None]  # Invalid object in __all__ (E0604)

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
Module to handle image processing strategies.
"""
import sys  # pylint: disable=unused-import

def is_valid(x, y):
    """
    Check if pixel position (x, y) is within the image bounds.

    Args:
        x (int): X-coordinate of the pixel.
        y (int): Y-coordinate of the pixel.

    Returns:
        bool: True if the pixel is within the image bounds, False otherwise.
    """
    return 0 <= x < self.width and 0 <= y < self.height

def show(self):
    """
    Display the image.

    Args:
        self.image.show(): Show the image
    """
    self.image.show()

    Args:
        front_filename (str): Path to the front image file.
        back_filename (str): Path to the back image file.

    Returns:
        SimpleImage: The modified front image.

    Args:
        front_filename (str): Path to the front image file.
        shift_x (int): X-coordinate to shift the pixels.
        shift_y (int): Y-coordinate to shift the pixels.
        back_filename (str): Path to the back image file.

    Returns:
        SimpleImage: The modified back image.
