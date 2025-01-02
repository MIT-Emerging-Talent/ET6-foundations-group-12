#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for calculate percentage function

Created on 26.12.2024
@author: Yevheniia Rudenko
"""

import unittest

from ..calculate_percentage import calculate_percentage


class TestCalculatePercentage(unittest.TestCase):
    """Test the calculate_percentage function."""

    def test_positive_numbers(self):
        """It should return percentage for positive numbers"""
        self.assertEqual(calculate_percentage(50, 200), 25.0)

    def test_zero_numerator(self):
        """It should return 0% when the first number is zero"""
        self.assertEqual(calculate_percentage(0, 100), 0.0)

    def test_denominator_zero(self):
        """It should raise ZeroDivisionError if the second number is zero"""
        with self.assertRaises(ZeroDivisionError):
            calculate_percentage(50, 0)

    def test_not_numbers(self):
        """It should raise AssertionError for non-numeric input"""
        with self.assertRaises(AssertionError):
            calculate_percentage("50", 100)

    def test_100_percent(self):
        """It should return 100% when numerator equals denominator"""
        self.assertEqual(calculate_percentage(100, 100), 100.0)

    def test_negative_numerator(self):
        """It should calculate correctly for negative numerator"""
        self.assertEqual(calculate_percentage(-50, 200), -25.0)

    def test_negative_denominator(self):
        """It should calculate correctly for negative denominator"""
        self.assertEqual(calculate_percentage(50, -200), -25.0)

    def test_percentage_greater_than_100(self):
        """It should calculate correctly for percentage greater than 100"""
        self.assertEqual(calculate_percentage(300, 200), 150.0)

    def test_small_values(self):
        """It should handle very small values correctly"""
        self.assertAlmostEqual(calculate_percentage(0.0005, 0.002), 25.0, places=5)

    def test_large_values(self):
        """It should handle very large values correctly"""
        self.assertEqual(calculate_percentage(1_000_000, 10_000_000), 10.0)

    def test_precision_handling(self):
        """It should maintain precision for floating-point calculations"""
        self.assertAlmostEqual(calculate_percentage(1, 3), 33.3333, places=4)
