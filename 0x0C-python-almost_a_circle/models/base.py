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
"""

import json
import os


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
        dummy = cls(2, 2)
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
