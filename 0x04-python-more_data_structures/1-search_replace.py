#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new = []
    index = None
    if my_list is not None:
        new = my_list[:]
        if search in my_list:
            index = my_list.index(search)
            new[index] = replace
        return new
