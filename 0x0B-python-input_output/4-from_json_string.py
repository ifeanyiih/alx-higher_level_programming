#!/usr/bin/python3

"""
Modules contains function that returns an object
from JSON string
"""
import json


def from_json_string(my_str):
    """Returns object from a JSON string

    Args:
        my_str (str): JSON string

    Returns:
        obj: an object(Python data structure)
    """
    return json.loads(my_str)
