#!/usr/bin/python3

"""
Module checks the relationship between an object
and a class
"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a class

    Args:
        obj (any): The object to check
        a_class (any): The class to check against

    Returns:
        bool: True if obj is exactly an instance of the class
        False otherwise
    """
    return isinstance(obj, a_class) and type(obj) == a_class
