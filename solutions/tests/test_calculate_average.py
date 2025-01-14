#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for calculate_average function.

This module includes tests for the following cases:
    - Positive numbers
    - Negative numbers
    - Mixed positive and negative numbers
    - Invalid (non-numeric) inputs

Created on 26.12.2024
Author: Yevheniia Rudenko
"""

import unittest

from ..calculate_average import calculate_average


class TestCalculateAverage(unittest.TestCase):
    """Test the calculate_average function."""

    def test_positive_numbers(self):
        """It should return the correct average for positive numbers."""
        self.assertEqual(calculate_average(4, 6), 5.0)

    def test_negative_numbers(self):
        """It should return the correct average for negative numbers."""
        self.assertEqual(calculate_average(-3, -5), -4.0)

    def test_positive_and_negative_numbers(self):
        """It should return the correct average for both positive and negative numbers."""
        self.assertEqual(calculate_average(-3, 3), 0.0)

    def test_not_numbers(self):
        """It should raise TypeError for non-numeric input."""
        with self.assertRaises(TypeError):
            calculate_average("a", 3)
        with self.assertRaises(TypeError):
            calculate_average(3, None)
