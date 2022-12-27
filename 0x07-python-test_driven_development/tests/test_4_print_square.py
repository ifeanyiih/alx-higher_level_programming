#!/usr/bin/python3

"""Unit test Module to test function in
module '4-print_square'
"""

import sys
import unittest
from importlib import import_module

"""Make Python find the module path"""
sys.path.insert(1, '../')


class PrintSquareTestCase(unittest.TestCase):
    """Test class

    Attributes:
        print_square: the function that prints the square
    """

    def setUp(self):
        """Sets up the test"""
        self.print_square = import_module('4-print_square').print_square

    def test_less_than_zero(self):
        """Tests if size is less than zero"""
        self.assertRaises(ValueError, self.print_square, -1)

    def test_correct_type(self):
        """Tests if size is an integer"""
        self.assertRaises(TypeError, self.print_square, 'a')
        self.assertRaises(TypeError, self.print_square, 2.5)
        self.assertEqual(self.print_square(0), None)
        self.assertEqual(self.print_square(2), None)


if __name__ == '__main__':
    unittest.main()
