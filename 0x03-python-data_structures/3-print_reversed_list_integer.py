#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new_list = list(reversed(my_list))
    for i in new_list:
        if type(i) is int:
            print("{:d}".format(i))
