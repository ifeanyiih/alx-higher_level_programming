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

    def to_json(self):
        """Retrieves the dictionary representation of a Student instance"""
        return self.__dict__
