#!/usr/bin/python3

"""
Module with function demonstrating matrix element
division
"""


def matrix_divided(matrix, div):
    """Function to divide the elements of a matrix

    Args:
        matrix (list): matrix
        div (int | float): divisor

    Returns:
        a new matrix

    Raises:
        ZeroDivisionError: if div == 0
        TypeError: if div not of type int or float.
            Also if lists in matrix are not same size.
            If matrix not list of lists
    """
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    """
    err_str: Error string for when matrix is not a list
    for when matrix is not a list of lists
    for when matrix is not a list of lists of integers/floats
    """
    err_str = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) not in [list]:
        raise TypeError(err_str)
    for row in matrix:
        if type(row) not in [list]:
            raise TypeError(err_str)
        for i in range(len(row)):
            if type(row[i]) not in [int, float]:
                raise TypeError(err_str)
    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
    new = []
    for row in matrix:
        new_row = []
        for i in range(len(row)):
            value = row[i] / div
            new_row.append(round(value, 2))
        new.append(new_row)

    return new
