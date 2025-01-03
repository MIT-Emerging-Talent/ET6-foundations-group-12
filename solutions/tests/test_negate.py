#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 02.01.2025

@author: Abdul Qader Dost
"""

import unittest

from ..negate import negate


class TestNegate(unittest.TestCase):
    """Tests for the negate function."""

    def test_negate_positive_number(self):
        """It should negate positive numbers correctly."""
        actual = negate(2)
        expected = -2
        self.assertEqual(actual, expected)

    def test_negate_negative_number(self):
        """It should negate negative numbers correctly."""
        actual = negate(-2)
        expected = 2
        self.assertEqual(actual, expected)

    def test_negate_zero(self):
        """It should handle zero correctly."""
        actual = negate(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_non_numeric_input(self):
        """It should raise a TypeError for non-numeric inputs."""
        with self.assertRaises(TypeError):
            negate("hello")

    def test_overflow(self):
        """It should handle overflow correctly."""
        actual = negate(1e308)  # Maximum float value
        expected = -1e308
        self.assertEqual(actual, expected)

    def test_underflow(self):
        """It should handle underflow correctly."""
        actual = negate(-1e-323)  # Minimum subnormal positive float value
        expected = 1e-323
        self.assertEqual(actual, expected)
