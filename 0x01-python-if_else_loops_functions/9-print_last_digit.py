#!/usr/bin/python3

def print_last_digit(number):
    if (number < 0):
        sign = -1
    else:
        sign = 1
    rem = (number * sign) % 10
    print(f"{rem}", end="")
    return (rem)
