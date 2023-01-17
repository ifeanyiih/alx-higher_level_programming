#!/usr/bin/python3

"""
Module: test_rectangle.py
Module contains Unittest Case for Module: base.py
Imports:
    unittest: unittest module
    Base: Parent class
    Rectangle: module to test
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
        rect = Rectangle(40, 50, id=3)
        self.assertEqual(rect.width, 40)
        self.assertEqual(rect.height, 50)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 3)

    def test_Rectangle_area_method(self):
        """test that the area method works normally"""
        rect = Rectangle(20, 50, 3, 5, 1888)
        self.assertEqual(rect.area(), 1000)

    def test_Rectangle_display(self):
        """test the the display method works properly"""
        rect = Rectangle(5, 7)
        self.assertEqual(rect.display(), None)

    def test_the__str__method(self):
        """test that the obj prints properly"""
        rect = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(rect.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_the_instance_update_method(self):
        """tests that the update method works properly"""
        rect = Rectangle(4, 6)
        args = [283, 30, 70, 3, 5]
        rect.update(*args)
        self.assertEqual(rect.id, 283)
        self.assertEqual(rect.width, 30)
        self.assertEqual(rect.height, 70)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 5)

        arg_dict = {'width': 30, 'height': 40, 'x': 3, 'y': 4, 'id': 23}
        rect.update(**arg_dict)
        self.assertEqual(rect.id, 23)
        self.assertEqual(rect.width, 30)
        self.assertEqual(rect.height, 40)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

        rect.update(*args, **arg_dict)
        self.assertEqual(rect.id, 283)
        self.assertEqual(rect.width, 30)
        self.assertEqual(rect.height, 70)
