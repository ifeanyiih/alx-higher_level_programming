#!/usr/bin/python3

"""
A Unit test for the module '3-say_my_name.py'
"""

import sys
import unittest
from importlib import import_module

sys.path.insert(1, '../')


class Module_3_say_my_name_TestCase(unittest.TestCase):
    """Tests that the function correctly runs with given inputs

    Attributes:
        say_my_name: function to call
    """
    def setUp(self):
        """Sets up the test"""
        self.say_my_name = import_module('3-say_my_name').say_my_name

    def tearDown(self):
        """clears the set up"""
        del self.say_my_name

    def test_that_args_are_strings(self):
        """Tests that the functions runs desiredly"""
        self.assertRaises(TypeError, self.say_my_name, "Sizwe", 20)
        self.assertRaises(TypeError, self.say_my_name, 20, "Bansi")
        self.assertEqual(self.say_my_name("Sizwe", "Bansi"), None)


if __name__ == '__main__':
    unittest.main()
