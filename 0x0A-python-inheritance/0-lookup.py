#!/usr/bin/python3

"""
Functions in the Module returns the list of
available attributes and methods of an object
"""


def lookup(obj):
    """
    Args:
        obj (any): any given object

    Returns:
        list: a list of available attributes and methods
    """
    return dir(obj)
