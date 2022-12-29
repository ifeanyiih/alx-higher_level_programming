#!/usr/bin/python3

"""
Unit tests for Module '5-text_indentation.py'
"""

import sys
import unittest
from importlib import import_module
sys.path.insert(1, '../')


class TextIndentTestCase(unittest.TestCase):
    """Tests for function text_indent
    Checks that the functions runs as is supposed

    Attributes:
        text_indentation: function to test
    """
    def setUp(self):
        """Sets up the function"""
        self.text_indentation = import_module('5-text_indentation').text_indentation

    def test_for_correct_parameter_type(self):
        """Tests that the parameter is the right type"""
        self.assertRaises
        (TypeError, self.text_indentation, "Hello. Who are you")

    def test_for_correct_output(self):
        """Tests that the print output is correct"""
        self.assertEqual(self.text_indentation("Hello"), None)


if __name__ == '__main__':
    unittest.main()
