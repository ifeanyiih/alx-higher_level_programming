#!/usr/bin/python3

def multiply_by_2(a_dict):
    if a_dict is not None:
        for key in a_dict.keys():
            a_dict[key] = a_dict[key] * 2
        return a_dict
