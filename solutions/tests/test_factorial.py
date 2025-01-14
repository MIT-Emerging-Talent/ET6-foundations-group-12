#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 01-03-2024

@author: Abdul Qader Dost
"""

import unittest

from ..factorial import factorial


class TestFactorial(unittest.TestCase):
    """Test the absolute_value function"""

    def test_factorial_of_zero(self):
        """It should return 1 for the special case of zero, where 0! = 1."""
        actual = factorial(0)
        expected = 1
        self.assertEqual(actual, expected)

    def test_factorial_of_one(self):
        """It should return 1 when the input is 1, as 1! equals 1."""
        actual = factorial(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_factorial_of_two(self):
        """It should return 1 when the input is 2, as 2! equals 2."""
        actual = factorial(2)
        expected = 2
        self.assertEqual(actual, expected)

    def test_factorial_of_three(self):
        """It should return 1 when the input is 3, as 3! equals 6."""
        actual = factorial(3)
        expected = 6
        self.assertEqual(actual, expected)

    def test_factorial_of_four(self):
        """It should return 1 when the input is 4, as 4! equals 24."""
        actual = factorial(4)
        expected = 24
        self.assertEqual(actual, expected)

    def test_factorial_of_negative_number(self):
        """It should raise a ValueError when the input is a
        negative number."""
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_factorial_float_input(self):
        """It should raise a TypeError when the input is not an integer."""
        with self.assertRaises(TypeError):
            factorial(3.5)

    def test_factorial_of_large_number(self):
        """It should return the correct factorial for large numbers,
        e.g., 10! = 3,628,800."""
        actual = factorial(40)
        expected = 815915283247897734345611269596115894272000000000
        self.assertEqual(actual, expected)

    def test_factorial_of_string(self):
        """It should raise a TypeError when the input is a string."""
        with self.assertRaises(TypeError):
            factorial("string")

    def test_factorial_of_negative_non_integer(self):
        """It should raise a TypeError for a negative non-integer."""
        with self.assertRaises(TypeError):
            factorial(-3.5)
