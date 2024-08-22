Module name "E0710-raising_new_style_class" doesn't conform to snake_case naming style
Fix: Rename the module to e0710_raising_new_style_class.py
# ... (rest of the code remains the same)
class CustomException(Exception):
    pass


def some_function():
    raise CustomException("Width is zero")  # Raising a new style class which doesn’t inherit from BaseException (E0710)
