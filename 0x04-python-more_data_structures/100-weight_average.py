#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    multipliers = 0
    divs = 0
    for a, b in my_list:
        multipliers += a * b
        divs += b
    return multipliers/divs
