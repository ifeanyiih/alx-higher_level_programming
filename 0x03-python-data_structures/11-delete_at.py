#!/usr/bin/python3

def delete_at(m=[], idx=0):
    if len(m) == 0:
        return []
    if idx < 0 or idx > len(m) - 1:
        return m
    del m[idx]
    return m
