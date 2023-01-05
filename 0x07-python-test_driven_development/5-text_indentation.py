#!/usr/bin/python3

"""
Module: 5-text_indentation.py
Author: Ifeanyichukwu Ifeanyichukwu
Date: Dec. 29, 2022

Module contains a function the prints a
string of text based on an indentation format
"""


def text_indentation(text):
    """Function prints a text indented,
    after the period (.) and question mark (?)

    Args:
        text (str): The first parameter which must be a string

    Raises:
        TypeError: if a value of the wrong type is passed
    """
    if type(text) not in [str]:
        raise TypeError("text must be a string")
    cpy = text
    i = 0
    while (text[i] == ' '):
        i += 1
    cpy = cpy[i:]
    i = 0
    while i < len(cpy):
        j = 0
        print(cpy[i], end="")
        if cpy[i] in '.?:':
            print()
            print()
            j = i + 1
            while (j < len(cpy) and cpy[j] == ' '):
                j += 1
            i = j
            continue
        i += 1
