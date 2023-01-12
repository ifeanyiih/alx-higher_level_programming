#!/usr/bin/python3

"""
Module inherits from Rectangle (9-rectangle.py)
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Attributes:
        __size (int): size of the side
    """
    def __init__(self, size):
        """
        Args:
            size (int): integer argument
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the Square"""
        return self.__size ** 2

    def __str__(self):
        """Returns a string representation of the object"""
        return f"[{'Square'}] {self.__size}/{self.__size}"
