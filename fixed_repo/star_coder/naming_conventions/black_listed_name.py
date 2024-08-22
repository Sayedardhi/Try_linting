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



            You need to fix the following problems before submitting your code:
                Disallowed name "foo"
        """

        return (
            f"<h1 style='color:red;'>You are a post pylint fixer.</h1>"
            + f"""Here is the code:<pre><code>{self.original_code}</code></pre>"""
            + f"\n\nHere is the pylint report:<pre><code>{self.pylint_report}</code></pre>"
            + f"\n\n**STRICTLY FOLLOW THE RULES BELOW:**"
            + f"- Do not introduce unrelated code, or unrelated fixes."
            + f"- Every function should have a docstring. If missing, add a docstring to the function."
            + f"- Don't uncomment code that is commented out."
            + f"- Don't just say 'insert original code here', actually provide the corrected code."
            + f"- Don't change the functionality of the code. As in, for example, don't just make a recursive function iterative because you want to when that was not prompted by the linter."
            + f"- If a line or variable needs to be removed, clearly indicate it."
            + f"- Return only the corrected code within the specific markers, and provide a rationale for each change."
            + f"- Add a module docstring at the beginning of the code if missing, as suggested by the linter. You can use the name of the file as the module name."
            + f"- If a linting rule requires you to break up a line of code or add a line, please do so."
            + f"- Do not put random imports that were not part of the original code."
            + f"- Do not just leave sections of the code to be filled in by the user; fully complete the code."
            + f"- Do not just disable the linter warning but actually fix it"
            + f"- It is imperative that you do not change the functionality of the code unless directly needed by the linter. So keep most of the code from the original file and fix what's needed. This is imperative, as the code is being linted for a specific purpose, and changing the functionality could have unintended consequences."
            + f"\n\nReturn the response in the following format:\n"
            + f"<pre><code>{self.corrected_code}</code></pre>"
        )
    back = SimpleImage(back_filename)
    for y in range(foo.height):
        for x in range(foo.width):
            pixel = foo.get_pixel(x, y)

            # Detect blue pixels in front and replace with back pixels
            if pixel[2] > 2 * max(pixel[0], pixel[1]):
                back_pixel = back.get_pixel(x, y)
                foo.set_pixel(x, y, back_pixel)
    return foo


def do_back(front_filename, shift_x, shift_y, back_filename):
    """
    Back strategy: loop over image,
    detect *non-blue* pixels.
    Copy those pixels to back, shifted by shift_x, shift_y.
    Pixels which fall outside of the background are ignored.
    Return changed back image.
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
