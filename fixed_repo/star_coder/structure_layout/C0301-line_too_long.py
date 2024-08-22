25/04/18 09:30:07  WARNING   C0301: Line too long (166/120)
            I will give you the original code, and pylint report, and you have to fix the problems. Here is the corrected code:
            #!/usr/bin/env python3


            """
Stanford Bluescreen Example
Shows front and back strategies. The functions are mostly complete, missing only the key if-logic line.

    Front strategy: loop over front image, detect blue pixels there, substitute in pixels from back. Return changed front image.
                image.set_pixel(x, y, back_pixel)
    return image
    Back strategy: loop over image, detect *non-blue* pixels. Copy those pixels to back, shifted by shift_x, shift_y. Pixels which fall outside of the background are ignored. Return changed back image.
    return back
    - **`
    
    If your project contains multiple
   
 
 """

        if args[0] == "help":

            return self.__doc__
