#!/usr/bin/python3

def number_keys(a_dictionary):
    num = 0

    if a_dictionary is None:
        return num
    num = len(a_dictionary.keys())
    return num
