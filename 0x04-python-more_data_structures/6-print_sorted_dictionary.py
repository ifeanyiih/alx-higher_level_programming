#!/usr/bin/python3

def print_sorted_dictionary(a_dict):
    keys = []

    if a_dict is not None:
        keys = sorted(a_dict.keys())
        for key in keys:
            print("{:s}: {}".format(key, a_dict[key]))
