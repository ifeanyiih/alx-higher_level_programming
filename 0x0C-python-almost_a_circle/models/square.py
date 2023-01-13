#!/usr/bin/python3

"""
Module: square.py
Modulce contains class Square
Which Inherits Rectangle from rectangle.py
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the instance

        Args:
            size (int): size
            x (int): x
            y (int): y
            id (int): id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String format representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """getter method for self.size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter method for self.size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Method to update the Square instance"""
        if not args or len(args) == 0:
            for key in kwargs.keys():
                if key == 'id':
                    self.id = kwargs[key]
                if key == 'size':
                    self.size = kwargs[key]
                if key == 'x':
                    self.x = kwargs[key]
                if key == 'y':
                    self.y = kwargs[key]
        else:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]

    def to_dictionary(self):
        """Returns the dictionary representation of Square"""
        val = {}
        val['id'] = self.id
        val['size'] = self.size
        val['x'] = self.x
        val['y'] = self.y
        return val
