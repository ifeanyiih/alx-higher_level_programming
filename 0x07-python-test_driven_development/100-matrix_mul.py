#!/usr/bin/python3

"""
Module demonstrates multiplication of two matrices
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices

    Args:
        m_a (list): matrix A
        m_b (list): matrix B

    Raises:
        TypeError: If either m_a or m_b is not a list.
            Also if either m_a or m_b is not a list of lists.
            If an element of either matrix m_a or m_b is not an int or float.
            If the rows of m_a or m_b are not of equal lengths.
        ValueError: If m_a or m_b is an empty list
            If m_a or m_b can't be multiplied
    """
    if type(m_a) not in [list]:
        raise TypeError("m_a must be a list")
    if type(m_b) not in [list]:
        raise TypeError("m_b must be a list")

    for row in m_a:
        if type(row) not in [list]:
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if type(row) not in [list]:
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_a) == 1 and len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    if len(m_b) == 1 and len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for el in row:
            if type(el) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for el in row:
            if type(el) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    size = len(m_a[0])
    for row in m_a:
        if len(row) != size:
            raise TypeError("each row of m_a must be of the same size")
    size = len(m_b[0])
    for row in m_b:
        if len(row) != size:
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    n_arr = []

    for row in m_a:
        n_row = []
        for i in range(len(row)):
            col = []
            sums = 0
            for b_row in m_b:
                col.append(b_row[i])
            for j in range(len(row)):
                sums += row[j] * col[j]
            n_row.append(sums)
        n_arr.append(n_row)

    return n_arr
