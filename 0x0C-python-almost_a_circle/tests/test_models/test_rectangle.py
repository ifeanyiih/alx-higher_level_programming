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
        self.assertIsInstance(self.rect, Rectangle)

    def test_empty_class(self):
        """tests instance creation with no values"""
        self.assertRaises(TypeError, Rectangle())

    def test_one_value_present(self):
        """tests instance creation with one value"""
        self.assertRaises(TypeError, Rectangle(2))

    def test_two_non_optional_args(self):
        """tests if the non-optional arguments are present"""
        rect = Rectangle(40, 50)
        self.assertEqual(rect.width, 40)
        self.assertEqual(rect.height, 50)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 1)

    def test_that_arguments_are_int(self):
        """tests if the arguments are int"""
        obj = Rectangle(20, 20)
        self.assertRaises(TypeError, Rectangle(20, "15"))
        self.assertRaises(TypeError, Rectangle("19", 30))
        self.assertRaises(TypeError, obj.x = "2")
        self.assertRaises(TypeError, obj.y = "3")

    def test_that_values_not_negative(self):
        """tests that argument values are non-negative"""
        self.assertRaises(ValueError, Rectangle(-50, 20))
        self.assertRaises(ValueError, Rectangle(20, -50))
        self.assertRaises(ValueError, Rectangle(20, 30, -3))
        self.assertRaises(ValueError, Rectangle(20, 30, 5, -3))
