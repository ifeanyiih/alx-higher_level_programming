#!/usr/bin/python3
def simple_delete(a_dict, key=""):
    if a_dict is not None and key != "":
        if key in a_dict:
            del a_dict[key]
        return a_dict
