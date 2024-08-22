
def simple_image(filename):
    """
    A wrapper class for PIL Image to facilitate pixel manipulation.
    """
    image = Image.open(filename)
    pixels = image.load()
    width, height = image.size
    return SimpleImage(image, pixels, width, height)
    def __init__(self, image, pixels, width, height):
        self.image = image
        self.pixels = pixels
        self.width = width
        self.height = height
    # ... (remaining code remains the same)
    # ... (remaining code remains the same)
    # ... (remaining code remains the same)
    if len(args) not in [2, 4]:
```python
"""
Image processing module
"""

def do_back(image, width, height, mask):
    """
    Processes an image by shrinking it to the given dimensions and applying a mask.

    Args:
        image: The input image.
        width: The desired width of the processed image.
        height: The desired height of the processed image.
        mask: A binary mask to apply to the processed image.

    Returns:
        The processed image.
    """
    return do_back(image, int(width), int(height), mask)
