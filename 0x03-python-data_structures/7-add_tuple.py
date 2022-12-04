#!/usr/bin/python3

def add_tuple(a=(), b=()):
    if len(a) == 0 and len(b) == 0:
        return (0, 0)
    if len(a) < 2:
        a = a[0], 0
    if len(b) < 2:
        b = b[0], 0
    return a[0] + b[0], a[1] + b[1]
