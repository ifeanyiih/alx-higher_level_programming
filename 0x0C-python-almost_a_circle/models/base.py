#!/usr/bin/python3

"""
Module: base.py
Module contains a class Base
the class will be the 'base' of all other classes in this project
The goal of it is to manage 'id' attribute in all future classes
to avoid duplicating the same code (by extension, same bugs)

Imports:
    json: handle JSON data
    os: check for file existence
    csv: to handle csv
    turtle: to handle drawing shapes with tkinter
"""

import json
import os
import csv
import turtle


class Base:
    """Base for all future classes

    Attributes:
        __nb_objects (int): private class attribute
        id (int): public instance attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize instance

        Args:
            id (int): integer argument
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dict):
        """Returns the JSON string representation of list_dict"""
        if list_dict is None or len(list_dict) == 0:
            return "[]"
        return json.dumps(list_dict)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write(cls.to_json_string([]))
            else:
                list_dict = []
                for obj in list_objs:
                    list_dict.append(obj.to_dictionary())
                f.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        if not os.path.exists(f"{cls.__name__}.json"):
            return []
        with open(f"{cls.__name__}.json", "r", encoding="utf-8") as f:
            loaded = cls.from_json_string(f.read())
            arr = []
            for load in loaded:
                arr.append(cls.create(**load))
            return arr

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves to a CSV file in the format

        Rectangle:
            <id>,<width>,<height>,<x>,<y>
        Square:
            <id>,<size>,<x>,<y>
        """
        with open(f"{cls.__name__}.csv", "w", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=",")
            cls.create()
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width,
                                    obj.height, obj.x, obj.y])
            if cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Loads from a CSV file
        And returns a list of obj instances
        """
        list_objs = []
        with open(f"{cls.__name__}.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                row = list(map(lambda i: int(i), row))
                if cls.__name__ == "Rectangle":
                    obj = cls(row[1], row[2], row[3], row[4], row[0])
                if cls.__name__ == "Square":
                    obj = cls(row[1], row[2], row[3], row[0])
                list_objs.append(obj)
        return list_objs

    @staticmethod
    def draw(list_rect, list_sqr):
        """that opens a window and draws all the
        Rectangles and Squares
        """
        turtle.delay(50)
        for rect in list_rect:
            turtle.begin_poly()
            turtle.setx(rect.x)
            turtle.sety(rect.y)
            turtle.fillcolor('yellow')
            turtle.begin_fill()
            turtle.pd()
            turtle.fd(rect.width)
            turtle.right(90)
            turtle.fd(rect.height)
            turtle.right(90)
            turtle.fd(rect.width)
            turtle.right(90)
            turtle.fd(rect.height)
            turtle.end_poly()
            turtle.pu()
            turtle.end_fill()
            turtle.setpos(0, 0)
        for sq in list_sqr:
            turtle.begin_poly()
            turtle.setx(sq.x)
            turtle.sety(sq.y)
            turtle.fillcolor('red')
            turtle.begin_fill()
            turtle.pd()
            turtle.fd(sq.size)
            turtle.right(90)
            turtle.fd(sq.size)
            turtle.right(90)
            turtle.fd(sq.size)
            turtle.right(90)
            turtle.fd(sq.size)
            turtle.end_poly()
            turtle.pu()
            turtle.end_fill()
            turtle.setpos(0, 0)
        turtle.exitonclick()
