Module name "E0711-not_implemented_raised" conforms to snake_case naming style
A wrapper class for PIL Image to facilitate pixel manipulation.
    elif len(args) == 4: # Fixing the lint error by using an elif statement
        try:
            shift_x = int(args[1])
            shift_y = int(args[2])
            image = do_back(args[0], shift_x, shift_y, args[3])
            image.show()
        except ValueError:
            print("Shift values must be integers.")
raise NotImplemented  # NotImplemented raised instead of NotImplementedError (E0711)
raise NotImplementedError  # NotImplemented raised instead of NotImplementedError (E0711)
