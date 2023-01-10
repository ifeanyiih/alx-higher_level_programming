#!/usr/bin/python3

"""
Module contains function that checks the relationship
between an object and a class
"""


def inherits_from(obj, a_class):
    """
    Args:
        obj (any): the object to check
        a_class (any): the class to check against

    Returns:
        bool: True if the object is an instance
        of a class that inherited (directly or indirectly)
        from the specified class ; otherwise False
    """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
