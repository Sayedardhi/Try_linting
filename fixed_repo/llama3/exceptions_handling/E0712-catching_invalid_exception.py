Module to demonstrate front and back strategies for manipulating images.
The functions are mostly complete, missing only the key if-logic line.
"""
Module docstring
This module provides two main functions: do_front and do_back. The do_front function takes two image filenames as input and returns a new image with pixels from the front image replaced with those from the back image where the front pixel is blue. The do_back function also takes four parameters: the filename of the front image, shift-x, shift-y, and the filename of the back image.
"""

        Initialize the SimpleImage with a given filename. Load the image and get its size.
    Front strategy: loop over front image, detect blue pixels there,
    substitute in pixels from back. Return changed front image.
    Back strategy: loop over image, detect *non-blue* pixels.
    Copy those pixels to back, shifted by shift_x, shift_y. Pixels which fall outside of the background are ignored.
if __name__ == "__main__":
except Exception as e:  # Catching an exception which doesn’t inherit from BaseException (E0712)
    pass
    """
    Brief description: This function does something with front and back filenames.
    
    Parameters:
    front_filename (str): The name of the front image file.
    back_filename (str): The name of the back image file.
    
    Returns:
    None
    """
    if not all([front_filename, back_filename]):
        return  # either or both files are missing, so do nothing

    # rest of your code here
