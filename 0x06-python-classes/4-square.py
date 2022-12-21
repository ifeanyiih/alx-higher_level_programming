#!/usr/bin/python3
"""
A class Square

This module creates a class Square.
"""


class Square:
    """An empty Class that defines a Square

    Attributes:
        __size: private attribute
    """
    def __init__(self, size=0):
        """
        Args:
            size(int): size of a square
        """
        if not (type(size) == int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Retrieves the square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter
        Sets the __size attribute

        Args:
            value(int): value to set to
        """
        if not (type(value) == int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of a square"""
        return (self.__size ** 2)
