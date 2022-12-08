#!/usr/bin/python3

def best_score(a_dict):
    key_ = None
    if a_dict is None:
        return key_
    key_ = list(a_dict.keys())[0]
    maximum = a_dict[key_]
    for key, value in a_dict.items():
        if value is None:
            continue
        if value > maximum:
            key_ = key
            value = value
            maximum = value
    return key_
