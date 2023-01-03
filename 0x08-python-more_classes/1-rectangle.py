#!/usr/bin/python3

"""
A class Rectangle that defines a rectangle
"""


class Rectangle:
    """Defines a rectangle

    Attributes:
        __width (int): width of the rectangle
        __height (int): height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Args:
            width (int): the width
            height (int): the height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns the width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of the width"""
        if type(value) not in [int]:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns the height value"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) not in [int]:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
