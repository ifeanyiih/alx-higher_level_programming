#!/usr/bin/python3

def best_score(a_dict):
    maximum = 0
    if a_dict is None:
        return None
    for key, value in a_dict.items():
        if value > maximum:
            key_ = key
            value = value
            maximum = value
    return key_
