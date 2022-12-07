#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new = []
    index = None
    if my_list is not None:
        new = my_list[:]
        for i in new:
            if i == search:
                index = new.index(i)
                new[index] = replace
        return new
