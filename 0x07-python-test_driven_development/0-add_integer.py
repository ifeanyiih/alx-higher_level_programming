#!/usr/bin/python3

"""
Module to demonstrate adding integers
"""


def add_integer(a, b=98):
    """This function adds to integers together

    Args:
        a (int|float): The first parameter
        b (int|float): The second parameter. This is optional

    Returns:
        int: The result of the addition of the two numbers

    Raises:
        TypeError: If either of the parameters is not an integer
            or a float type
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
