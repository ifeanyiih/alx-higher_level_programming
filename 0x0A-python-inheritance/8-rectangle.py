#!/usr/bin/python3

"""
Module Imports and Inherits from Class BaseGeometry
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Attributes:
        __width (int): private attribute
        __height (int): private attribute
    """
    def __init__(self, width, height):
        """Initialization

        Args:
            width (int): integer variable
            height (int): integer variable
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
