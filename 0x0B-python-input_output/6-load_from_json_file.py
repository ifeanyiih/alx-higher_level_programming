#!/usr/bin/python3

"""Module contains function that loads
JSON from a file
"""
import json


def load_from_json_file(filename):
    """Loads JSON from file

    Args:
        filename (str): file to load from

    Returns:
        any: the object decoded
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
