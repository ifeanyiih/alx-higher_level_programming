#!/usr/bin/python3

"""
Module contains a class that inherits from list
"""


class MyList(list):
    """
    Inherits from a list
    """

    def print_sorted(self):
        print(sorted(self))
