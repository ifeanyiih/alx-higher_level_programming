#!/usr/bin/python3

"""
Unit tests for Module demonstrating the division of
matrix elements
"""

import sys
from importlib import import_module
import unittest

sys.path.insert(1, '../')


class MatrixTestCase(unittest.TestCase):
    """Test class for module 2-matrix_divided

    Attributes:
        matrix_divided: function to run test with
        smatrix: example matrix to pass to function matrix_divided
        tmatrix: example matrix to pass to function matrix_divided
        matrix: example matrix to pass to function matrix_divided
    """
    def setUp(self):
        """Sets up the test by creating the necessary objects"""
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

    def tearDown(self):
        """clears the setUp"""
        del self.smatrix
        del self.tmatrix
        del self.mmatrix
        del self.matrix_divided

    def test_that_matrix_is_matrix(self):
        """Test that matrix is actually a matrix
            i.e matrix is a list of lists with integer/float
            elements
        """
        rslt = self.matrix_divided(self.smatrix, 2)
        for row in rslt:
            for i in range(len(row)):
                self.assertEqual(type(row[i]), float)

    def test_that_div_is_int_or_float(self):
        """Tests that div is int or float"""
        self.assertRaises(TypeError, self.matrix_divided, self.smatrix, 'b')

    def test_that_matrix_row_is_uniform(self):
        """Tests that all the rows of the matrix have equal length"""
        self.assertRaises(TypeError, self.matrix_divided, self.tmatrix, 3)

    def test_that_matrix_is_a_list_of_lists_of_ints_or_floats(self):
        """Tests for correctly raised exceptions from matrix"""
        self.assertRaises(TypeError, self.matrix_divided, self.mmatrix, 3)
        self.assertRaises(TypeError, self.matrix_divided, None, None)
        self.assertRaises(TypeError, self.matrix_divided, None, 5)


if __name__ == '__main__':
    unittest.main()
