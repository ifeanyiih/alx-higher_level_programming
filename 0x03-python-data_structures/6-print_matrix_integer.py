#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix) > 0:
        for row in matrix:
            if type(row) == list:
                for i in row:
                    print("{:d}".format(i), end=" ")
                print()
            else:
                print("{}".format(row))
