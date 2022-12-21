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
    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size(int): size of a square
            position(tuple): position of the square
        """
        if not (type(size) == int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if not type(position) == tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not len(position) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not type(position[0]) == int and type(position[1]) == int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not position[0] > 0 and position[1] > 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """Retrieves the square size"""
        return self.__size

    @property
    def position(self):
        """Retrieves the square position"""
        return self.__position

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

    @position.setter
    def position(self, value):
        """position setter
        Sets the __position attribute

        Args:
            value(tuple): value to set to
        """
        if not type(value) == tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not len(value) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not type(value[0]) == int and type(value[1]) == int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not value[0] > 0 and value[1] > 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of a square"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints a square using the # character"""
        if self.__size == 0:
            print()
        else:
            for n in range(self.__size):
                if not self.__position[1] > 0:
                    print(" " * self.__position[0], end="")
                for m in range(self.__size):
                    print('#', end="")
                print()
