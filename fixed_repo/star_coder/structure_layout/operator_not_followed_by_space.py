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
            if pixel[2]>2*max(pixel[0],pixel[1]):  # Operator not followed by a space
                back_pixel = back.get_pixel(x, y)
                image.set_pixel(x, y, back_pixel)


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

    
    """
    image = do_back(args[0], int(args[1]), int(args[2]), args[3])

    return f'```\n{image}\n```'


@bot.command()
async def coginfo():
    """
        This function returns the name of all commands available in the bot.
        
        **USAGE:**
            ```python
             @bot.command()
             async def coginfo():
                 """
                     Returns a list with the names and descriptions for all commands available in the bot
                 
                 **USAGE:**
                     ```python
                      @bot.command()
                      async def coginfo():
                          pass
                      ```
                 """
             
                 return f"{bot.commands}\n"
            ```
    """
    
    return f"{bot.commands}"


@bot.command(name="ping")
async def ping_command():
    """
        This function pong's the user that executed the command

        **USAGE:**
            ```python
             @bot.command()
             async def ping():
                 """
                     Pongs the user that triggered the command
                 
                 **USAGE:**
                     ```python
                      @bot.command()
                      async def ping():
                          pass
                      ```
                 """
             
                 await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")
            ```
    """

    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")


@bot.command()
async def clear():
    """
        This function clears the channel that the command was used in.

        **USAGE:**
            ```python
             @bot.command()
             async def clear():
                 """
                     Clears all messages from current channel
                 
                 **USAGE:**
                     ```python
                      @bot.command()
                      async def clear():
                          pass
                      ```
                 """
             
                 await ctx.channel.purge(limit=99)
            ```
    """

    await ctx.channel.purge(limit=99)


@bot.command()
async def eval():
    """
        This function allows the user to execute code within the bot's environment

        **USAGE:**
            ```python
             @bot.command()
             async def eval():
                 """
                     Allows for execution of Python code, with a result being sent back
                 
                 **USAGE:**
                     ```python
                      @bot.command()
                      async def eval():
                          pass
                      ```
                 """
             
                 try:
                    await ctx.send(f"```py\n{eval(await ctx.message.content[7:])}\n```")
                 except Exception as e:
                    await ctx.send(f"{e}")
            ```
    """

    try:
        await ctx.send(f"```py\n{eval(await ctx.message.content[7:])}\n```")
    except Exception as e:
        await ctx.send(f"{e}")


@bot.command()
async def source():
    """
        This function displays the code for a specific file or module

        **USAGE:**
            ```python
             @bot.command()
             async def source():
                 """
                     Displays the source code of any Python file in the repo
                 
                 **USAGE:**
                     ```python
                      @bot.command()
                      async def source():
                          pass
                      ```
                 """
             
                 if ctx.message.content == "source":
                    await ctx.send("https://github.com/ChristopherHayes1/Discord-Image-Back-Up")
                 elif ctx.message.content[8:] in bot.__dict__.keys():
                     await ctx.send(f"```py\n{bot.__dict__[ctx.message.content[8:]]}\n```")
                 else:
                    try:
                        await ctx.send(f'```py\n{open(ctx.message.content[8:], "r").read()}\n```')
                    except Exception as e:
                        await ctx.send("https://github.com/ChristopherHayes1/Discord-Image-Back-Up")
            ```
    """

    if ctx.message.content == "source":
        await ctx.send("https://github.com/ChristopherHayes1/Discord-Image-Back-Up")
    elif ctx.message.content[8:] in bot.__dict__.keys():
        await ctx.send(f"```py\n{bot.__dict__[ctx.message.content[8:]]}\n```")
    else:
        try:
            await ctx.send(f'```py\n{open(ctx.message.content[8:], "r").read()}\n```')
        except Exception as e:
            await ctx.send("https://github.com/ChristopherHayes1/Discord-Image-Back-Up")
        image.show()


if __name__ == '__main__':

### Code Coverage Tests
- Test coverage should be at least 90%! (with optional bonus points for tests)
    - You can use any test framework that you want, but pytest is recommended and tested as well.
- The tests can be run via the terminal by typing `make test` in the root directory of the project, or alternatively they can also be run from a specific file with: 
    ```bash
    python3 -m unittest test_file.py
    ```
### Documentation 
- Add detailed documentation to your code!
    - Use type hints as much as you can for improved readability and maintainability (e.g.: `x: int`, not just `x`)
    - Comment the functions, classes, variables, etc., so that they are easy to understand what is happening in the function/class/variable
    - Include docstrings at the beginning of any function/method to provide information about its use
- For your documentation, you can also use: 
    ```bash
    make docs
    ```
    
