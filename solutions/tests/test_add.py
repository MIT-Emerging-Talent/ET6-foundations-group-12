#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Test for addition of two numbers

Created on 28.12.2024
@author : Ridwan Ayinde


"""

import unittest
from solutions.add import add  # Import the function to test


class TestAddFunction(unittest.TestCase):
    """
    TestAddFunction test two numbers
    on different cases with the add function
    and returns the result.
    """

    def test_add_positive_numbers(self):
        """Test adding two positive numbers"""
        self.assertEqual(add(4, 6), 10)

    def test_add_negative_numbers(self):
        """Test add two negative numbers"""
        self.assertEqual(add(-4, -5), -9)

    def test_add_mixed_sign_numbers(self):
        """Test adding a positive and a negative number"""
        self.assertEqual(add(4, -5), -1)

    def test_add_zero(self):
        """Test adding zero to a number"""
        self.assertEqual(add(4, 0), 4)

    def test_non_numbers(self):
        """it should raise an AssertionError for non numbers input"""
        with self.assertRaises(AssertionError):
            add("a", 5)  # Invalid input: string instead of a number

    def test_for_large_values(self):
        """Test adding large values"""
        self.assertAlmostEqual(add(1e10, 2e10), 3e10, places=1)

    def test_for_small_values(self):
        """Test adding very small numbers"""
        self.assertAlmostEqual(add(1e-10, 2e-10), 3e-10, places=10)

    def test_precision_handling(self):
        """Test addition with floating point precision"""
        self.assertAlmostEqual(
            add(0.1, 0.2), 0.3, places=7, msg="precision error in add function"
        )

    def test_integer_overflow(self):
        """Test large integers. Failed to handle large
        integers correctly"""
        result = add(2**100, 2**100)
        self.assertEqual(result, 2**101)

    def test_string_inputs(self):
        """Test for strings instead of numbers"""
        with self.assertRaises(AssertionError):
            add("3", "5")

    def test_none_inputs(self):
        """Test for none input with number"""
        with self.assertRaises(AssertionError):
            add(None, 5)

    def test_non_numeric_iterables(self):
        """Test adding a list with a number"""
        with self.assertRaises(AssertionError):
            add([1, 2, 3], 5)

    def test_boolean_inputs(self):
        """Test adding booleans"""
        self.assertEqual(add(True, False), 1.0)
        self.assertEqual(add(True, True), 2.0)
        self.assertEqual(add(False, True), 1.0)
        self.assertEqual(add(False, False), 0.0)

    def test_boolean_inputs_with_numbers(self):
        """Test adding boolean input with numbers"""
        self.assertEqual(add(True, 5), 6.0)


if __name__ == "__main__":
    unittest.main()
