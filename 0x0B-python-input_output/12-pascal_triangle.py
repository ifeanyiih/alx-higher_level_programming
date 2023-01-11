#!/usr/bin/python3

"""
Module contains function that returns a list of lists of
integers representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """Returns a list of lists of integers

    Args:
        n (int): size of Pascals triangle of n
    """
    if n <= 0:
        return []
    root = []
    for i in range(n):
        row = []
        if len(root) == 0:
            row.append(1)
            root.append(row)
            continue
        row.append(1)
        current = root[len(root) - 1]
        if len(current) == 1:
            row.append(1)
            root.append(row)
            continue
        i = 0
        while i < len(current) - 1:
            val = current[i] + current[i + 1]
            row.append(val)
            i += 1
        row.append(1)
        root.append(row)
    return root
