#!/usr/bin/env python3

"""
Stanford Bluescreen Example
Shows front and back strategies.
The functions are mostly complete,
missing only the key if-logic line.
"""

import sys
import logging
from PIL import Image

logging.basicConfig(level=logging.INFO)

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
 */
            '''
        """

    def check_format(self):
        """This checks if the file has a valid header"""

        with open(self._path) as f:
            # First line of the code should be a module docstring
            first_line = next(f).strip()
            is_module = False

            if first_line.startswith('"""') and not first_line.startswith("'''"):
                is_module = True

        return is_module

    def fix_format(self):
        """This fixes the code header to meet all of our formatting rules."""
        
        # Create a temporary file with the formatted text
        temp_path = f'{Path(self._temp_dir).absolute()}/{Path(self._path).stem}.py'

        try:
            with open(temp_path, 'w') as f:
                for line in self.formatted_text():
                    # We don't need to add the shebang line here because it will be added when we create a new file
                    if not line.startswith('#'):
                        f.write(line + '\n')
        except FileNotFoundError:
            pass
        
        shutil.move(temp_path, self._path)

    def formatted_text(self):
        """This returns the formatted text of the original file"""

        with open(self._path) as f:
            lines = f.readlines()

        # Remove the first line (module docstring) from the code
        if not self.check_format():
            lines.pop(0)

        # Add the shebang line to the beginning of the new file
        yield '#!/usr/bin/python3\n'

        # Iterate through each line in the original text and add a new one based on the format rules above
        for idx, line in enumerate(lines):
            corrected_line = line

            if self.check_format():
                # Remove all spaces at the beginning of lines
                corrected_line = corrected_line.lstrip()

                # Remove comments from each line
                corrected_line = re.sub(r'(^[ \t]*#[^\n]+\n)|(^[\s\S]*$)', '', corrected_line)

                # Don't put blank lines in the code
                if corrected_line != '':
                    yield corrected_line
            else:
                # Add a module docstring for each file
                if idx == 0:
                    yield '"""\n'

                    # The name of the file should be the module's name. You can use that to describe the purpose and usage of the code
                    yield f'This file was automatically fixed by Pylint.\n\nModule Name: {Path(self._path).stem}\n\nThe original module docstring is as follows:\n\n{next(f).strip()}'

                    # Add a blank line after the header
                    yield '\n"""\n'
                else:
                    yield corrected_line

        if self.check_format():
            # Add blank lines at end of file to conform to PEP8
            yield ''

    def add_shebang(self):
        """This adds the shebang line to the beginning of the code"""
        
        with open(self._path, 'w') as f:
            f.write('#!/usr/bin/python3\n')

    def save_to_temp(self):
        """Saves a copy of this file in the temp directory"""

        # Create a temporary file with the formatted text
        temp_file = NamedTemporaryFile('w+', dir=Path(self._temp_dir), delete=False, suffix='.py', mode='wt')

        try:
            for line in self.formatted_text():
                # We don't need to add the shebang line here because it will be added when we create a new file
                if not line.startswith('#'):
                    temp_file.write(line + '\n')
        except FileNotFoundError:
            pass
        
        # Rename and move the temporary file
        temp_file.name = Path(temp_file.name).absolute()
        shutil.move(temp_file.name, self._path)

        # Close the file to free resources
        temp_file.close()

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
            if pixel[2] > 2 * max(pixel[0], pixel[1]):
                back_pixel = back.get_pixel(x, y)
                image.set_pixel(x, y, back_pixel)
    return image

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
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            if pixel[2] <= 2 * max(pixel[0], pixel[1]):
                dest_x = x + shift_x
                dest_y = y + shift_y
                if back.in_bounds(dest_x, dest_y):
                    back.set_pixel(dest_x, dest_y, pixel)
    return back

def main():
    """
    Main function to handle argument parsing and strategy execution.
    """
    args = sys.argv[1:]

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


            <NAME>, 1923
        """
        print("Hello I am your post-pylint fixer")
        return self._get_original_code() + "\n"

    def _get_original_code(self):
        """This method should be implemented to provide the code that will actually be fixed. 
            In this example, we're just returning a string of text."""
        return "main()"


# -

fixer = MyPostPylintFixer()
print(fixer._get_original_code())
