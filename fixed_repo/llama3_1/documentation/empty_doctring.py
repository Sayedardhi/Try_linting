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
        return 0 <= x < self.width and 0 <= y < self.height

    def show(self):
        """
        Display the image.
        """
        self.image.show()


def do_front(front_filename, back_filename):
    """
    Front strategy: loop over front image,
    detect blue pixels there,
    substitute in pixels from back.
    Return changed front image.
    """
    image = SimpleImage(front_filename)
    back = SimpleImage(back_filename)
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)

            # Detect blue pixels in front and replace with back pixels
            if pixel[2] > 2 * max(pixel[0], pixel[1]):
                back_pixel = back.get_pixel(x, y)
                image.set_pixel(x, y, back_pixel)
    return image


"""
Module docstring: This module contains a function for performing back-and-forth operations.
"""

    """
    Performs back-and-forth operation between two files.

    Args:
        front_filename (str): The filename of the front file.
        shift_x (int): The x-coordinate to shift by.
        shift_y (int): The y-coordinate to shift by.
        back_filename (str): The filename of the back file.

    Returns:
        None
    """
    # Your original function code remains unchanged here...
    """
    """
    image = SimpleImage(front_filename)
    back = SimpleImage(back_filename)
    # Loop over front image - copy non-blue pixels
    # to background
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)

            # Detect non-blue pixels and copy to back
            if pixel[2] <= 2 * max(pixel[0], pixel[1]):
                dest_x = x + shift_x
                dest_y = y + shift_y
                # Only copy pixels to back if they will be in-bounds
                if back.in_bounds(dest_x, dest_y):
                    back.set_pixel(dest_x, dest_y, pixel)
    return back


def main():
    """
    Main function to handle argument parsing and strategy execution.
    """
    args = sys.argv[1:]

    # args:
    # front-image back-image                 - do front strategy
    # front-image shift-x shift-y back-image - do back strategy

    if len(args) != 2 and len(args) != 4:
        print('Args not recognized. Usage:')
        print('2 args for front strategy:')
        print('  front-image back-image')
        print('4 args for back strategy:')
        print('  front-image shift-x shift-y back-image')
        return

    if len(args) == 2:
        image = do_front(args[0], args[1])
        image.show()

    if len(args) == 4:
        image = do_back(args[0], int(args[1]), int(args[2]), args[3])
        image.show()


if __name__ == '__main__':
    main()
