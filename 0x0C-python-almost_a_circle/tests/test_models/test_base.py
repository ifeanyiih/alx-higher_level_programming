#!/usr/bin/python3

"""
Module: test_base.py
Unit Tests for Module: base.py
Imports:
    unittest:
    base: the module to test
"""

import unittest
from models.base import Base


class BaseTestCase(unittest.TestCase):
    """Test for the class Base from Module base.py"""
    def setUp(self):
        """Sets up the test"""
        self.obj = Base()
        self.obj2 = Base(205)

    def tearDown(self):
        """Clears the test area"""
        del self.obj
        del self.obj2

    def test_obj_id(self):
        """Test that obj is created with an Id"""
        self.assertEqual(self.obj.id, 1)
        self.assertEqual(self.obj2.id, 205)
