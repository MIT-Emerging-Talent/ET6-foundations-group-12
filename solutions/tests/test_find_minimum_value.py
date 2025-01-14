"""
A module for testing the find_minimum_value function.

Test categories:
    - Standard test cases: test the function with typical inputs.
    - Edge test cases: test the function with extreme inputs.
    - Defensive tests: test the function with invalid inputs.


Created on 2024-12-28
Author: Lukmon Olamilekan Alao
"""

import unittest

from ..find_minimum_value import find_minimum_value


class TestFindMinimumValue(unittest.TestCase):
    """Test the find_minimum_value from a list"""

    # standard and edge test
    def test_first_four_integers(self):
        """It gives 1 when [1, 2, 3, 4] is pass to the function"""
        actual = find_minimum_value([1, 2, 3, 4])  # call function with test argument
        expected = 1  # hand-write the expected return value
        self.assertEqual(actual, expected)

    def test_float_only(self):
        """It should return the smallest float value"""
        self.assertEqual(find_minimum_value([1.2, 3.4, 2.7, 0.5]), 0.5)

    def test_list_of_float_and_int(self):
        """It returns the smallest value in list"""
        self.assertEqual(find_minimum_value([2.24, 4, 5.23, 1]), 1)

    def test_negative_values(self):
        """It should return the negative number with the highest value"""
        self.assertEqual(find_minimum_value([-1, -2, -3, -4]), -4)

    def test_list_with_negative_and_positive_int_values(self):
        """It should return the smallest value from the list"""
        self.assertEqual(find_minimum_value([-1, 15, -9, 6]), -9)

    def test_list_with_negative_and_positive_float_values(self):
        """It should return the smallest value from the list"""
        self.assertEqual(find_minimum_value([-0.35, 0.1, 2.4, -4.234]), -4.234)

    def test_list_with_both_negative_and_positive_values_of_int_and_float(self):
        """It should return the smallest value from the list"""
        self.assertEqual(find_minimum_value([-1.2, 3, 3.78, -5]), -5)

    # Defensive tests
    def test_none_input(self):
        """It should raise Assertion error for none input"""
        with self.assertRaises(AssertionError):
            find_minimum_value(None)

    def test_input_value_is_not_list(self):
        """It should raise an assertion error if the input value is a string"""
        with self.assertRaises(AssertionError):
            find_minimum_value("1")
