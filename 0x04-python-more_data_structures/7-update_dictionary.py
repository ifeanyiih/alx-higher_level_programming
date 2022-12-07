#!/usr/bin/python3
def update_dictionary(a_dict, key, value):
    if a_dict is None:
        a_dict = {}
        a_dict[key] = value
        return a_dict
    a_dict[key] = value
    return a_dict
