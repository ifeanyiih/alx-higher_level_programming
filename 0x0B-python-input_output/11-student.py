#!/usr/bin/python3

"""
Module contains a class: student
"""


class Student:
    """Defines a Student

    Attributes:
        first_name (str): students first name
        last_name (str): students last name
        age (int): students age
    """
    def __init__(self, first_name, last_name, age):
        """Initializes the Student

        Args:
            first_name (str): students first name
            last_name (str): students last_name
            age (int): students age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves the dictionary representation of a Student instance"""
        desc = {}
        if type(attrs) == list:
            for attr in attrs:
                if attr in self.__dict__.keys():
                    desc[attr] = self.__dict__[attr]
            return desc
        return self.__dict__

    def reload_from_json(self, json):
        """Reloads a Class from its dictionary representation"""
        if len(json.keys()) != 0:
            self.first_name = json['first_name']
            self.last_name = json['last_name']
            self.age = json['age']
