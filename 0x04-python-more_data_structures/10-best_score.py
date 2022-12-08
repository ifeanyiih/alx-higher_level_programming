#!/usr/bin/python3

def best_score(a_dict):
    maximum = None
    key_ = None
    if a_dict is None:
        return None
    for key, value in a_dict.items():
        if type(value) is int and value > maximum:
            key_ = key
            value = value
            maximum = value
    return key_
