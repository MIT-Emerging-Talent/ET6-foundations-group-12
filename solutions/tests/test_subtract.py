#! usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test for subtraction of one number from the other.

Created on 31.12.2024

@author:


"""

import unittest
from solutions.subtract import subtract


class TestSubtractFunction(unittest.TestCase):
    """The TestsubtractFunction shows different
    functions for different test cases and confirms
    the result
    """

    def test_subtract_positive_numbers(self):
        """Test subtracting two positive numbers"""
        self.assertEqual(subtract(7, 4), 3)

    def test_subtract_negative_numbers(self):
        """Test subtract two negative numbers"""
        self.assertEqual(subtract(-5, -5), 0)

    def test_subtract_mixed_sign_numbers(self):
        """This test should subtract the negative second
        number from the first number"""
        self.assertEqual(subtract(7, -5), 12)

    def test_not_numbers(self):
        """This should raise an AssertionError for not numbers input"""
        self.assertEqual(subtract(-5, -5), 0)

    def test_for_small_values(self):
        """Test subtracting big number from small number"""
        self.assertEqual(subtract(2, 9), -7)

    def test_precision_handling(self):
        """Test subtraction with floating point precision"""
        self.assertAlmostEqual(
            subtract(0.3, 0.2), 0.1, places=7, msg="precision error in add function"
        )

    def test_for_very_small_values(self):
        """Test subtracting very small numbers"""
        self.assertAlmostEqual(subtract(4e-10, 2e-10), 2e-10, places=10)

    def test_integer_overflow(self):
        """Test large integers to simulate overflow scenarios in fixed systems"""
        large_number1 = 10**100
        large_number2 = 10**100 - 1
        result = subtract(large_number1, large_number2)
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
