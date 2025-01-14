#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for testing the find_maximum_value function.

Test categories:
    - Standard test cases: test the function with typical inputs.
    - Edge test cases: test the function with extreme inputs.
    - Defensive tests: test the function with invalid inputs.


Created on 2024-12-28
Author: Lukmon Alao
"""

import unittest

from ..find_maximum_value import find_maximum_value


class TestFindMaximumValue(unittest.TestCase):
    """Test the find_maximum_value from a list"""

    # standard and edge test
    def test_first_four_integers(self):
        """It gives 4 when [1, 2, 3, 4] is pass to the function"""
        actual = find_maximum_value([1, 2, 3, 4])  # call function with test argument
        expected = 4  # hand-write the expected return value
        self.assertEqual(actual, expected)

    def test_float_only(self):
        """It should return the highest float value"""
        self.assertEqual(find_maximum_value([1.2, 3.4, 2.7, 0.5]), 3.4)

    def test_list_of_float_and_int(self):
        """It returns the highest value in list"""
        self.assertEqual(find_maximum_value([2.24, 4, 5.23, 1]), 5.23)

    def test_negative_values(self):
        """It should return the negative number with the lowest value"""
        self.assertEqual(find_maximum_value([-1, -2, -3, -4]), -1)

    def test_list_with_negative_and_positive_int_values(self):
        """It should return the highest value from the list"""
        self.assertEqual(find_maximum_value([-1, 15, -9, 6]), 15)

    def test_list_with_negative_and_positive_float_values(self):
        """It should return the highest value from the list"""
        self.assertEqual(find_maximum_value([-0.35, 0.1, 2.4, -4.234]), 2.4)

    def test_list_with_both_negative_and_positive_values_of_int_and_float(self):
        """It should return the highest value from the list"""
        self.assertEqual(find_maximum_value([-1.2, 3, 3.78, -5]), 3.78)

    # Defensive tests
    def test_none_input(self):
        """It should raise Assertion error for none input"""
        with self.assertRaises(AssertionError):
            find_maximum_value(None)

    def test_input_value_is_not_list(self):
        """It should raise an assertion error if the input value is a string"""
        with self.assertRaises(AssertionError):
            find_maximum_value("1")
