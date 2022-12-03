#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0:
        return mylist[:]
    if idx > len(my_list) - 1:
        return mylist[:]
    new = mylist[:]
    new[idx] = element
    return new
