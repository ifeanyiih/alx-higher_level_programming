#!/usr/bin/python3

"""
Module: test_base.py
Unit Tests for Module: base.py
Imports:
    unittest:
    base: the module to test
"""

import unittest
Base = __import__('../../models/base').Base

print(Base)
class BaseTestCase(unittest.TestCase):
    """Test for the class Base from Module base.py"""
    def test_fail(self):
        """Dummy Test"""
        pass
