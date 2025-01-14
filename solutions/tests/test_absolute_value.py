#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 12.29.2024

@author: Abdul Qader Dost
"""

import unittest

from ..absolute_value import absolute_value


class TestAbsoluteValue(unittest.TestCase):
    """Test the absolute_value function"""

    def test_absolute_value_of_zero(self):
        """It should return 0 when the input is 0"""
        actual = absolute_value(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_absolute_value_of_positive_number(self):
        """It should return the positive value of a number"""
        actual = absolute_value(10)
        expected = 10
        self.assertEqual(actual, expected)

    def test_absolute_value_of_negative_number(self):
        """It should return the positive value of a negative number"""
        actual = absolute_value(-10)
        expected = 10
        self.assertEqual(actual, expected)

    def test_absolute_value_of_float(self):
        """It should return the absolute value of a float"""
        actual = absolute_value(-3.14)
        expected = 3.14
        self.assertEqual(actual, expected)

    def test_absolute_value_of_large_number(self):
        """It should handle large numbers correctly"""
        actual = absolute_value(1000000)
        expected = 1000000
        self.assertEqual(actual, expected)

    def test_absolute_value_of_small_number(self):
        """It should handle small numbers correctly"""
        actual = absolute_value(0.000001)
        expected = 0.000001
        self.assertEqual(actual, expected)

    def test_type_error_for_non_number_input(self):
        """It should raise a TypeError for non-number input"""
        with self.assertRaises(TypeError):
            absolute_value("hello")

    def test_type_error_for_string_input(self):
        """It should raise a TypeError for string input"""
        with self.assertRaises(TypeError):
            absolute_value("42")

    def test_type_error_for_list_input(self):
        """It should raise a TypeError for list input"""
        with self.assertRaises(TypeError):
            absolute_value([1, 2, 3])

    def test_type_error_for_dict_input(self):
        """It should raise a TypeError for dict input"""
        with self.assertRaises(TypeError):
            absolute_value({"a": 1})
