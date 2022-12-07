#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    new_set = set()
    if set_1 is None or set_2 is None:
        new_set = set(set_1 or set_2)
        return new_set
    new_set = set(set_1.symmetric_difference(set_2))
    return new_set
