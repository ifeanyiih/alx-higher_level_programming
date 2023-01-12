#!/usr/bin/python3

"""
Module implements a class MyInt
that inherits from int
"""


class MyInt(int):
    def __eq__(self, value):
        """Inverts the equality"""
        return super().__ne__(value)

    def __ne__(self, value):
        """Inverts the inequality"""
        return super().__eq__(value)
