#!/usr/bin/python3

"""
Module: test_rectangle.py
Module contains Unittest Case for Module: base.py
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class RectangleTestCase(unittest.TestCase):
    """Unittests for Rectangle class"""
    def test_is_subclass(self):
        """tests that Rectangle is subclass of Base"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_instance(self):
        """test that object is instance of Rectangle"""
        rect = Rectangle(20, 30)
        self.assertIsInstance(rect, Rectangle)

    def test_two_non_optional_args(self):
        """tests if the non-optional arguments are present"""
        rect = Rectangle(40, 50)
        self.assertEqual(rect.width, 40)
        self.assertEqual(rect.height, 50)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 2)
