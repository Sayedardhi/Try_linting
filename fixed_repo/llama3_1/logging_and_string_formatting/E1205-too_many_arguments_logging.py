Module name "E1205-too_many_arguments_logging" conforms to snake_case naming style
A wrapper class for PIL Image to facilitate pixel manipulation.
logging.basicConfig(level=logging.INFO, format='%(message)s')
        logging.info("Image loaded with dimensions %dx%d", self.width, self.height)
import logging

# Add a module docstring as suggested by the linter
"""
Image Loader Module

This module contains functions to load images.
"""

class ImageLoader:
    def __init__(self):
        # Initialize the image loader object
        pass

    def load_image(self, filename):
        # Load an image file
        self.width = 0
        self.height = 0

        logging.info("Image loaded with dimensions %dx%d", self.width, self.height)
