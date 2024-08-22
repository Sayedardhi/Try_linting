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
"""
Image Processing Module
"""
import sys
class SimpleImage:
    pass

def return_stmt(x, self_width, self_height):
    """
    Check if x coordinates and y coordinates are within image boundaries.
    
    Args:
        x (int): The x-coordinate to be checked.
        self_width (int): The width of the image.
        self_height (int): The height of the image.
    
    Returns:
        bool: Whether the coordinates are within the image boundaries or not.
    """
    return 0 <= x < self_width and 0 <= y < self_height

def show(self):
    """
    Display the image.
    """
    self.image.show()

def show(self):
    """
    This is a redefinition of the show method (E0102).
    
    Raises:
        ValueError: Redefinition of method.
    """
    raise ValueError("Redefinition of method")
    Front strategy: loop over front image, detect blue pixels there, substitute in pixels from back. 
    
    Args:
        front_filename (str): The filename of the front image.
        back_filename (str): The filename of the back image.
    
    Returns:
        SimpleImage: The modified front image.
    Back strategy: loop over image, detect non-blue pixels. Copy those pixels to back, shifted by shift_x, shift_y.
    
    Args:
        front_filename (str): The filename of the front image.
        shift_x (int): The x-coordinate shift for the back image.
        shift_y (int): The y-coordinate shift for the back image.
        back_filename (str): The filename of the back image.
    
    Returns:
        SimpleImage: The modified back image.
    
    
