#!/usr/bin/python3

def multiply_by_2(a_dict):
    if a_dict is not None:
        new_dict = {}
        for key, value in a_dict.items():
            new_dict[key] = value * 2
        return new_dict
    return {}
