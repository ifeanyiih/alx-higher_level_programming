#!/usr/bin/python3

def add_tuple(a=(), b=()):
    if len(a) == 0 and len(b) == 0:
        return 0, 0
    if len(a) < 2 and len(b) >= 2:
        return a[0] + b[0], b[1]
    if len(b) < 2 and len(a) >= 2:
        return a[0] + b[0], a[1]
    return a[0] + b[0], a[1] + b[1]
