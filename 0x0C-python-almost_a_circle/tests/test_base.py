#!/usr/bin/python3

"""
Module: test_base.py
Unit Tests for Module: base.py
Imports:
    unittest: unittest module
    base: the module to test
    Rectangle: for other test
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class BaseTestCase(unittest.TestCase):
    """Test for the class Base from Module base.py"""
    def test_no_given_id(self):
        """test that obj is created with no given id argument"""
        obj = Base(id=None)
        self.assertEqual(obj.id, 7)
    def test_obj_id(self):
        """Test that obj is created with an Id"""
        obj = Base(id=1)
        obj2 = Base(id=3)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj2.id, 3)

    def test_static_method_to_json_string(self):
        """tests static method to_json_string"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        self.assertEqual(type(json_string), str)
        self.assertEqual(dictionary,
                         {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8})

    def test_save_to_file(self):
        """tests save_to_file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        self.assertEqual(Rectangle.save_to_file([r1, r2]), None)

    def test_from_json_string_method(self):
        """tests that method from json_string works"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
         ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)

        self.assertEqual(list_input, list_output)

    def test_create_method(self):
        """tests that class method create works"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

        self.assertNotEqual(r1, r2)

    def test_load_from_file(self):
        """tests that method load_from_file works properly"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()

        self.assertEqual(list_rectangles_input[0].__str__(),
                         list_rectangles_output[0].__str__())

    def test_save_to_file_csv_and_load_from_file_csv(self):
        """test class methods save_to_file_csv and load_from_file_csv"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()

        self.assertEqual(list_rectangles_input[0].__str__(),
                         list_rectangles_output[0].__str__())
