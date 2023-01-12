#!/usr/bin/python3

"""
Module implements a class Square, which inherits
from a class Rectangle
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Atrributes:
        __size (int): integer attribute
    """
    def __init__(self, size):
        """Initialization"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
