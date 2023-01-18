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
import os
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
        self.assertEqual(rect.width, 20)
        self.assertEqual(rect.height, 30)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

        rect = Rectangle(20, 30, 15)
        self.assertEqual(rect.width, 20)
        self.assertEqual(rect.height, 30)
        self.assertEqual(rect.x, 15)

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

    def test_for_correct_errors(self):
        """tests that correct errors are raised"""
        self.assertRaises(TypeError, Rectangle, "20", 30)
        self.assertRaises(TypeError, Rectangle, 20, "30")
        self.assertRaises(TypeError, Rectangle, 20, 30, "5")
        self.assertRaises(TypeError, Rectangle, 20, 30, 5, "8")
        self.assertRaises(ValueError, Rectangle, 0, 20)
        self.assertRaises(ValueError, Rectangle, 20, 0)
        self.assertRaises(ValueError, Rectangle, 20, 30, -5)
        self.assertRaises(ValueError, Rectangle, 20, 30, 5, -3)
        self.assertRaises(ValueError, Rectangle, -30, 30)
        self.assertRaises(ValueError, Rectangle, 30, -30)

    def test_Rectangle_display(self):
        """test the the display method works properly"""
        rect = Rectangle(5, 7)
        self.assertEqual(rect.display(), None)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        
        rect = Rectangle(5, 7, 8)
        self.assertEqual(rect.display(), None)
        self.assertEqual(rect.x, 8)
        self.assertEqual(rect.y, 0)

        rect = Rectangle(5, 6, 7, 8)
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

    def test_instance_method_to_dictionary(self):
        """tests that the method to_dictionary works properly"""
        rect = Rectangle(22, 30, id=77)
        obj = rect.to_dictionary()
        self.assertTrue(obj ==
                        {'x': 0, 'y': 0, 'width': 22, 'height': 30, 'id': 77})
        self.assertEqual(type(obj), dict)

    def test_save_to_file_method_on_Rectangle(self):
        """tests the save_to_file method on Rectangle class"""
        r1 = Rectangle(20, 30)
        r2 = Rectangle(30, 50, 5, 15)
        list_obj_in = [r1, r2]
        self.assertEqual(Rectangle.save_to_file(list_obj_in), None)
        list_obj_out = Rectangle.load_from_file()
        self.assertEqual(list_obj_in[0].x, list_obj_out[0].x)

        self.assertEqual(Rectangle.save_to_file(None), None)
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Rectangle.save_to_file([]), None)
        self.assertEqual(Rectangle.load_from_file(), [])

        self.assertEqual(Rectangle.save_to_file([]), None)
        self.assertTrue(os.path.exists("Rectangle.json"))
        self.assertTrue(Rectangle.save_to_file)
        self.assertIsNone(Rectangle.save_to_file([]))
