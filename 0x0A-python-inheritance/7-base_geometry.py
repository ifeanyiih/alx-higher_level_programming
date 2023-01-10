#!/usr/bin/python3

"""
Module contains an empty class
"""


class BaseGeometry:
    """A class with a single public method"""

    def area(self):
        """
        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an Integer

        Args:
            name (str): name
            value (int): value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if type(value) not in [int]:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
