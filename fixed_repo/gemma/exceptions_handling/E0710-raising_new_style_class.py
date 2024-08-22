class CustomException(Exception):
    Custom exception class that inherits from Exception.
        raise CustomException("Width is zero")
    Pixels which fall outside of the background are ignored
"""
CustomException module
"""

class CustomException(Exception):
    """Custom exception class"""

    def __init__(self, message):
        super().__init__(message)


raise CustomException("Width is zero")
