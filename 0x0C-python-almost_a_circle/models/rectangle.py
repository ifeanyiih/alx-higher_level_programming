#!/usr/bin/python3

"""
Module: rectangle.py
Module contains class Rectangle,
Which imports and inherits from class Base
"""

from models.base import Base


class Rectangle(Base):
    """Inherits from class Base

    Attributes:
        __width (int): private instance attribute
        defines the width of the Rectangle instance
        __height (int): private instance attribute
        defines the height of the Rectangle instance
        __x (int): private instance attribute
        __y (int): private instance attribute
        width: getter/setter for __width
        height: getter/setter for __height
        x: getter/setter for __x
        y: getter/setter for __y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the instance

        Args:
            width (int): width
            height (int): height
            x (int): x
            y (int): y
            id (int/None): id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """The getter method for the private instance attribute __width"""
        return self.__width

    @width.setter
    def width(self, value):
        """The setter method for the private instance attribute __width

        Args:
            value (int): value
        """
        if type(value) not in [int]:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """The getter method for the private instance attribute __height"""
        return self.__height

    @height.setter
    def height(self, value):
        """The setter method for the private instance attribute __height

        Args:
            value (int): value
        """
        if type(value) not in [int]:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """The getter method for the private instance attribute __x"""
        return self.__x

    @x.setter
    def x(self, value):
        """The setter method for the private instance attribute __x

        Args:
            value (int): value
        """
        if type(value) not in [int]:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """The getter method for the private instance attribute __y"""
        return self.__y

    @y.setter
    def y(self, value):
        """The setter method for the private instance attribute __y

        Args:
            value (int): value
        """
        if type(value) not in [int]:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the Rectangle instance"""
        return self.width * self.height

    def display(self):
        """Prints a rectangle using '#' to stdout"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            for i in range(self.x):
                print(" ", end="")
            for n in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """String formating of class instance"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} -"\
            f" {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Updates the Rectangle instance attributes"""
        if args and args is not None:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.width = args[i]
                if i == 2:
                    self.height = args[i]
                if i == 3:
                    self.x = args[i]
                if i == 4:
                    self.y = args[i]
        else:
            for name in kwargs.keys():
                if name == 'x':
                    self.x = kwargs[name]
                if name == 'y':
                    self.y = kwargs[name]
                if name == 'width':
                    self.width = kwargs[name]
                if name == 'height':
                    self.height = kwargs[name]
                if name == 'id':
                    self.id = kwargs[name]

    def to_dictionary(self):
        """returns the dictionary representation of Rectangle"""
        val = {}
        val['id'] = self.id
        val['width'] = self.width
        val['height'] = self.height
        val['x'] = self.x
        val['y'] = self.y
        return val
