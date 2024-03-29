#!/usr/bin/python3

"""
Module: test_square.py
Module contains Test Case for Module: square.py
Imports:
    unittest: unittest module
    square: the module to test
    Rectangle: the Parent class to Square
    Base: the Parent class to Rectangle
"""

import unittest
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle


class SquareTestCase(unittest.TestCase):
    """Tests for the class Square from the Module square.py"""
    def test_subclass(self):
        """tests that Square is a subclass of Rectangle
        and Base
        """
        sq = Square(40)
        self.assertIsInstance(sq, Square)
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(issubclass(Square, Base))

    def test_attributes(self):
        """test attributes of a Square instance"""
        sq = Square(40, id=58)
        self.assertEqual(sq.size, 40)
        self.assertEqual(sq.width, 40)
        self.assertEqual(sq.height, 40)
        self.assertEqual(sq.id, 58)

        sq = Square(10, 2)
        self.assertEqual(sq.size, 10)
        self.assertEqual(sq.x, 2)

        sq = Square(10, 2, 8)
        self.assertEqual(sq.size, 10)
        self.assertEqual(sq.x, 2)
        self.assertEqual(sq.y, 8)

    def test_that_instance_raises_right_error(self):
        """test that instance raises the right errors"""
        self.assertRaises(TypeError, Square, "23")
        self.assertRaises(TypeError, Square, 23, "2")
        self.assertRaises(TypeError, Square, 23, 4, "6")
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, -20)
        self.assertRaises(ValueError, Square, 20, -2)
        self.assertRaises(ValueError, Square, 30, 15, -10)

    def test_Square__str__(self):
        """tests the Square __str__ method return value"""
        sq = Square(40, id=2)
        self.assertEqual(sq.__str__(), "[Square] (2) 0/0 - 40")

    def test_size_getter_setter(self):
        """tests the Squares size getter method"""
        sq = Square(50)
        sq.size = 23
        self.assertEqual(sq.width, 23)
        self.assertEqual(sq.height, 23)

    def test_Square_update(self):
        """tests the Square instance update method"""
        sq = Square(200)
        args = [50, 40, 10, 10]
        args_dict = {'id': 23, 'size': 55, 'x': 5, 'y': 5}
        sq.update(*args)
        self.assertEqual(sq.size, 40)
        self.assertEqual(sq.x, 10)
        self.assertEqual(sq.id, 50)

        sq.update(**args_dict)
        self.assertEqual(sq.size, 55)
        self.assertEqual(sq.x, 5)
        self.assertEqual(sq.width, 55)
        self.assertEqual(sq.id, 23)

        sq.update(*args, **args_dict)
        self.assertEqual(sq.size, 40)
        self.assertEqual(sq.id, 50)

    def test_instance_method_to_dictionary(self):
        """tests that the instance method to_dictionary workds properly"""
        sq = Square(33, id=24)
        ob = sq.to_dictionary()
        self.assertTrue(ob == {'id': 24, 'size': 33, 'x': 0, 'y': 0})

    def test_Square_create_method(self):
        """tests the Square.create instance method"""
        sq = Square.create(**{'id': 89})
        self.assertEqual(sq.id, 89)

        sq = Square.create(**{'id': 89, 'size': 40})
        self.assertEqual(sq.id, 89)
        self.assertEqual(sq.size, 40)

        sq = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(sq.id, 89)
        self.assertEqual(sq.size, 1)
        self.assertEqual(sq.x, 2)

        sq = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(sq.id, 89)
        self.assertEqual(sq.size, 1)
        self.assertEqual(sq.x, 2)
        self.assertEqual(sq.y, 3)

    def test_Square_save_to_file_method(self):
        """tests the save_to file class method"""
        self.assertEqual(Square.save_to_file(None), None)
        self.assertEqual(Square.save_to_file([]), None)

        sq1 = Square(40, 2, 5, 88)
        sq2 = Square(44, 1, 0, 43)

        self.assertEqual(Square.save_to_file([sq1, sq2]), None)
        out = Square.load_from_file()
        self.assertEqual(out[0].size, sq1.size)

        Square.save_to_file(None)
        self.assertEqual(Square.load_from_file(), [])

        Square.save_to_file([])
        self.assertEqual(Square.load_from_file(), [])
