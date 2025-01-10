#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 05.01.2025

@author: Zephaniah Okoye
"""

import unittest
from solutions.exponentiation import exponentiation


class TestExponentiation(unittest.TestCase):
    """Test the exponentiation function"""

    def test_exponentiation_positive_exponent(self):
        """It should return the correct result for a positive exponent"""
        actual = exponentiation(2, 3)
        expected = 8.0
        self.assertEqual(actual, expected)

    def test_exponentiation_zero_exponent(self):
        """It should return 1.0 when the exponent is 0"""
        actual = exponentiation(5, 0)
        expected = 1.0
        self.assertEqual(actual, expected)

    def test_exponentiation_negative_exponent(self):
        """It should return the correct result for a negative exponent"""
        actual = exponentiation(2, -2)
        expected = 0.25
        self.assertEqual(actual, expected)

    def test_exponentiation_float_base(self):
        """It should return the correct result for a float base"""
        actual = exponentiation(1.5, 2)
        expected = 2.25
        self.assertEqual(actual, expected)

    def test_type_error_for_invalid_base(self):
        """It should raise a TypeError for an invalid base"""
        with self.assertRaises(TypeError):
            exponentiation("2", 3)

    def test_type_error_for_invalid_exponent(self):
        """It should raise a TypeError for an invalid exponent"""
        with self.assertRaises(TypeError):
            exponentiation(2, "3")

    def test_exponentiation_large_exponent(self):
        """It should handle large exponents correctly"""
        actual = exponentiation(2, 1000)
        expected = 2**1000
        self.assertEqual(actual, expected)

    def test_exponentiation_zero_base_positive_exponent(self):
        """It should return 0.0 when the base is 0 and exponent is positive"""
        actual = exponentiation(0, 3)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_exponentiation_zero_base_zero_exponent(self):
        """It should return 1.0 when both base and exponent are 0"""
        actual = exponentiation(0, 0)
        expected = 1.0
        self.assertEqual(actual, expected)
