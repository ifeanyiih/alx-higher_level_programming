#!/usr/bin/python3

def uniq_add(my_list=[]):
    my_set = set()
    sums = 0

    if my_list is None:
        return None

    my_set = set(my_list)
    for i in my_set:
        sums += i
    return sums
