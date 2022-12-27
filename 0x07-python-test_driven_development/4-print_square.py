#!/usr/bin/python3

"""
Module demonstrates printing a square with '#'
character
"""


def print_square(size):
    """Prints a square with l x b = size
        with character '#'

    Args:
        size (int): size

    Raises:
        ValueError: if size < 0
        TypeError: if type(size) not int
    """
    if type(size) not in [int]:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
