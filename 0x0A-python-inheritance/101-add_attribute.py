#!/usr/bin/python3

"""
Module contains function That adds a new attribute to an
object if it's possible
"""


def add_attribute(obj, name, val):
    """A function that adds a new attribute to
    obj if it's possible

    Args:
        obj (any): the object
        name (str): the attribute name
        value (any): the attribute value
    """
    test = hasattr(obj, name)
    if not test:
        raise TypeError("can't add new attribute")
