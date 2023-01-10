#!/usr/bin/python3

"""
Module contains function that returns the JSON representation
of an object(string)
"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of my_obj

    Args:
        my_obj (any): object to encode to JSON

    Returns:
        str: JSON representaion of my_obj
    """
    return json.dumps(my_obj)
