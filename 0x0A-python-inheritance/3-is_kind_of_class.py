#!/usr/bin/python3

"""
Module checks the relationship between a class and an obj
"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is a type of a class

    Args:
        obj (any): object to check
        a_class (any): class to check against

    Returns:
        bool: True if the object is an instance of,
        or if the object is an instance of a class that inherited from,
        the specified class ; otherwise False
    """
    return isinstance(obj, a_class)
