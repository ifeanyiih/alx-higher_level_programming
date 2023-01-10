#!/usr/bin/python3

"""
Module contains function that reads a text file(UTF8)
and prints it to stdout
"""


def read_file(filename=""):
    """
    Args:
        filename (str): name of the file to read
    """
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
