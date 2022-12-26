#!/usr/bin/python3

"""
Unit tests for Module demonstrating the division of 
matrix elements
"""

from importlib import import_module
import unittest

class MatrixTestCase(unittest.TestCase):
    def setUp(self):
        self.matrix_divided = import_module('2-matrix_divided').matrix_divided
        self.smatrix = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
                ]
        self.tmatrix = [
                [1, 2, 3],
                [4, 5]
                ]
        self.mmatrix = [
                [1, 2, 3],
                ['b', 'c', 4],
                ['5', '7', '8']
                ]

    def test_that_matrix_is_matrix(self):
        rslt = self.matrix_divided(self.smatrix, 2)
        for row in rslt:
            for i in range(len(row)):
                self.assertEqual(type(row[i]), float)

    def test_that_div_is_int_or_float(self):
        self.assertRaises(TypeError, self.matrix_divided, self.smatrix, 'b')

    def test_that_matrix_row_is_uniform(self):
        self.assertRaises(TypeError, self.matrix_divided, self.tmatrix, 3)

    def test_that_matrix_is_a_list_of_lists_of_ints_or_floats(self):
        self.assertRaises(TypeError, self.matrix_divided, self.mmatrix, 3)
        self.assertRaises(TypeError, self.matrix_divided, None, None)
        self.assertRaises(TypeError, self.matrix_divided, None, 5)


if __name__ == '__main__':
    unittest.main()
