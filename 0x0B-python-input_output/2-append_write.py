#!/usr/bin/python3

"""
Module contains function that appends text to a file
"""


def append_write(filename="", text=""):
    """Append text to a file

    Args:
        filename (str): file to append to
        text (str): text to append to file
    Returns:
        int: the number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
