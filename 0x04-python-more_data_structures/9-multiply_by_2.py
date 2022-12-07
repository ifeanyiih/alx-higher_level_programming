#!/usr/bin/python3

def multiply_by_2(a_dict):
    if a_dict is not None:
        for key, value in a_dict.items():
            a_dict[key] = value * 2
        return a_dict
    return None
