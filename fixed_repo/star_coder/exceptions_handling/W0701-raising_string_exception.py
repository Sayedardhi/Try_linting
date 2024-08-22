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
            if pixel[2] > 2 * max(pixel[0], pixel[1]):
                back_pixel = back.get_pixel(x, y)
                image.set_pixel(x, y, back_pixel)
    if image.width == 0:


            **HINT:** You can use comments to denote sections of code that need to be filled in by the user (which is commented out as a convention)


            **IMPORTANT**: Don't modify anything outside of markers specified. Otherwise, you could break up the original code and mess up your output

        """
        response = ""
        #raise "This should not be called"
        return response

    def get_original_code(self):
        """
            Returns the original code for this fixer.
        """
        return self.__orig_code


    def get_report(self):
        """
            Return the pylint report for this fixer.
        """
        return self.__pylint_report



    def save_report(self, file_name):
        """
            Save the report to a specified file name. 
        """
        with open(file_name,"w+") as f:
            f.write(self.__pylint_report)


    def get_filename(self):
        """
            Return the filename of the original code for this fixer.
        """
        return self.__orig_code_file

    def save_original_code(self, file_name):
        """
            Save the original code to a specified file name. 
        """
        with open(file_name,"w+") as f:
            f.write(self.__orig_code)




class FixerCreator(object):
    """
        Creates a new fixer for this module using the provided details. 

        :param module_name: The full name of the module that contains the code to be fixed, including path if applicable. 
        :param func_name: The full name of the function withing the module that needs to be fixed. 
        :param report: The pylint report from running the fixer on the original code.
        :param orig_code_file: The full file path where the original code resides. 
        """
    def __init__(self, module_name="", func_name="", report="", orig_code_file=""):
        self.__module_name = module_name
        self.__func_name = func_name
        self.__report = report
        self.__orig_code_file = orig_code_file

    def generate(self):
        """
            Generates a new fixer for this module.
        """
        return Fixer(self.__module_name, self.__func_name, self.__report, self.__orig_code_file)


class ModuleFixerCreator(object):
    """
        Creates a fixer creator that will create an instance of all the fixers in a given list.

        :param module_fixers: A list of strings, each string denoting the full name of the module that contains the code to be fixed, including path if applicable. 
        """
    def __init__(self, module_fixers):
        self.__module_fixers = module_fixers

    def generate(self):
        """
            Generates a new fixer for this module and returns it as an object.

            :return: A list of FixerCreator objects to create all the fixers in the given module.
        """

        #raise "This should not be called"
        return [FixerCreator(module_name=fixer, report="", orig_code_file="") for fixer in self.__module_fixers]



if __name__ == "__main__":
    test = ModuleFixerCreator(["./src/pylint/test"])
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
3) You are done!
    """

    original_code = get_original_code(file_name)
    original_file_path = str(Path(__file__).parent / '..' / 'data/fixers/fixer_base.py')
    fixer_rules_text, module_docstring_text, docstring_text = lint_rule.get_lint_rule_details(original_code=original_code,
                                                                                                original_file_path=original_file_path)

    if fixer_rules_text and module_docstring_text and docstring_text:
        print('You are a post pylint fixer.\nI will give you the original code,\nand pylint report, and you have to fix the problems.\n'
              'Here is the code:\n')

        pprint.pprint(original_code)
        print('\nHere is the pylint report:\n')

        print(f'{fixer_rules_text}\n{module_docstring_text}\n{docstring_text}')
        print('\n**STRICTLY FOLLOW THE RULES BELOW:**\n'
              '- Do not introduce unrelated code, or unrelated fixes.\n'
              '- Every function should have a docstring. If missing, add a docstring to the function.\n'
              '- Don\'t uncomment code that is commented out.\n'
              '- Don\'t just say "insert original code here", actually provide the corrected code.\n'
              '- Don\'t change the functionality of the code. As in, for example, don\'t just make a recursive function iterative because you want to when that was not prompted by the linter. \n'
              '- If a line or variable needs to be removed, clearly indicate it.\n'
              '- Return only the corrected code within the specific markers, and provide a rationale for each change.\n'
              '- Add a module docstring at the beginning of the code if missing, as suggested by the linter. You can use the name of the file as the module name. \n'
              '- If a linting rule requires you to break up a line of code or add a line, please do so.\n'
              '- Do not put random imports that were not part of the original code.\n'
              '- Do not just leave sections of the code to be filled in by the user; fully complete the code. \n'
              '- Do not just disable the linter warning but actually fix it\n'
              '- It is imperative that you do not change the functionality of the code unless directly needed by the linter. So keep most of the code from the original file and fix what\'s needed. This is imperative, as the code is being linted for a specific purpose, and changing the functionality could have unintended consequences.\n'
              f'- Return the response in the following format:\n```python\n{original_code}\n```')

    else:
        print('Looks like there are no problems with your code. No need to fix anything.')


if __name__ == '__main__':
