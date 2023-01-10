#!/usr/bin/python3

"""
Module contains function that writes a string to a text file,
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """Writes text, to a text file

    Args:
        filename (str): the name of the file to write to
        text (str): the content to write to the file
    Returns:
        int: the number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
