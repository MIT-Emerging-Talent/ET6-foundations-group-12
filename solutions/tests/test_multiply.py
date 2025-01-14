#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test for multiplying of 2 numbers

Created on 06.01.2025

@author: Simi-Solola
"""

import unittest
import math
from solutions.multiply import multiply


class TestMultiply(unittest.TestCase):
    """
    Test case for the multiply function.
    Tests include:
    - Positive numbers
    - Negative numbers
    - Error case for non-numeric input
    - Boundary cases like large numbers, small numbers, infinity, and NaN
    """

    def test_multiply_positive_numbers(self):
        """Test multiplying two positive numbers."""
        result = multiply(2, 3)
        self.assertEqual(result, 6.0)

    def test_multiply_negative_number(self):
        """Test multiplying a positive number by a negative number."""
        result = multiply(-2, 3)
        self.assertEqual(result, -6.0)

    def test_multiply_non_numeric_input(self):
        """Test that non-numeric inputs raise an assertion error."""
        with self.assertRaises(AssertionError):
            multiply(2, "a")

    def test_multiply_float_input(self):
        """Test multiplying two floating-point numbers."""
        result = multiply(2.5, 4.0)
        self.assertEqual(result, 10.0)

    def test_multiply_large_numbers(self):
        """Test multiplying very large numbers."""
        result = multiply(1e100, 1e100)
        self.assertEqual(result, 1e200)

    def test_multiply_small_numbers(self):
        """Test multiplying very small numbers."""
        result = multiply(1e-100, 1e-100)
        self.assertEqual(result, 1e-200)

    def test_multiply_infinity(self):
        """Test multiplying by infinity."""
        result = multiply(1, math.inf)
        self.assertEqual(result, math.inf)
        result = multiply(-1, math.inf)
        self.assertEqual(result, -math.inf)

    def test_multiply_nan(self):
        """Test multiplying by NaN."""
        result = multiply(math.nan, 5)
        self.assertTrue(math.isnan(result))
        result = multiply(5, math.nan)
        self.assertTrue(math.isnan(result))


if __name__ == "__main__":
    unittest.main()
