#!/usr/bin/python3
""" Create an Empty class

This module creates an empty class Square.
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
        if type(size) not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
