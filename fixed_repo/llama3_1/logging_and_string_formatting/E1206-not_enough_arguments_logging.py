Module name "E1206-not_enough_arguments_logging" conforms to snake_case naming style

# Added module docstring as per linter suggestion
"""
This module provides a wrapper class for PIL Image to facilitate pixel manipulation.
It also contains two strategies: front and back, which can be used to manipulate images.
"""
            if pixel[2] > 128 * max(pixel[0], pixel[1]):  # Changed to make the condition consistent
            if pixel[2] <= 128 * max(pixel[0], pixel[1]):  # Changed to make the condition consistent
        image.show()  # Added to display the modified back image
if __name__ == "__main__":
import logging

class ImageLoader:
    """
    A class used for loading images.
    
    Attributes
    ----------
    width : int
        The width of the image.
    height : int
        The height of the image.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def load_image(self):
        """
        Loads an image with specified dimensions.

        Parameters
        ----------
        width (int) : The width of the image.
        height (int) : The height of the image.
        """

        logging.info(f"Image loaded with dimensions {self.width}x{self.height}")

# Create a logger
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    # Example usage:
    loader = ImageLoader(800, 600)
    loader.load_image()
