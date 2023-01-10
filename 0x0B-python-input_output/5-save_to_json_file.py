#!/usr/bin/python3

"""
Module contains function that an Object to a text file
using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """writes JSON to a text file

    Args:
        my_obj (any): a given object to serialize
        filename (str): file to write JSON to
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
