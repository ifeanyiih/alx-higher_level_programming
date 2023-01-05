#!/usr/bin/python3

"""
Module has function say_my_name that prints a string
with format:

    My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Function prints string in format:
        'My name is <first name> <last name>

    Args:
        first_name (str): The first parameter
        last_name (str): The last parameter
    Raises:
        TypeError: if either of the parameters is not string type
    """
    if type(first_name) not in [str]:
        raise TypeError("first_name must be a string")
    if type(last_name) not in [str]:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
