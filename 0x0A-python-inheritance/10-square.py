#!/usr/bin/python3

"""
Module contains three classes
1. BaseGeometry
2. Rectangle
3. Square

Square inherits from Rectangle, which
inherits from BaseGeometry
"""


class BaseGeometry:
    """A class with a single public method
    That defines a basic geometry form
    """

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

    def area(self):
        """Returns the area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the class
        for printing
        """
        return f"[{'Rectangle'}] {self.__width}/{self.__height}"


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
