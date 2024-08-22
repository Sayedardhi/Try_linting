                if back.in
"""
Module providing utility functions for bound checking.
"""

def in_bounds(x, y):
    """
    Checks if a point is within a bounded region.

    Args:
        x (float): The x-coordinate of the point.
        y (float): The y-coordinate of the point.

    Returns:
        bool: True if the point is in bounds, False otherwise.
    """
    return x >= 0 and y >= 0 and x <= 1 and y <= 1
