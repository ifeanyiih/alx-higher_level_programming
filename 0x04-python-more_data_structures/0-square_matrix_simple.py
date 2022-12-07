#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new = []
    if matrix is not None:
        for row in matrix:
            new += [list(map(lambda x: x * x, row))]
        return new
