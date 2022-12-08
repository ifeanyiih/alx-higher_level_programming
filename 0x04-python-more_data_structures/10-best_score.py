#!/usr/bin/python3

def best_score(a_dict):
    maximum = None
    key_ = None
    if a_dict is None:
        return key_
    for key, value in a_dict.items():
        if value not None and value > maximum:
            key_ = key
            value = value
            maximum = value
    return key_
