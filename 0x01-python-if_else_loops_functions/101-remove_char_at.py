#!/usr/bin/python3

def remove_char_at(str, n):
    n_str = ""
    for i in range(len(str)):
        if i is n:
            continue
        else:
            n_str += str[i]
    return (n_str)
