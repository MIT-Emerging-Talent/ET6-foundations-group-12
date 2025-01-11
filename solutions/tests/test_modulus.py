#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test for modulus of 2 numbers

Created on 06.01.2025

@author:Simi-Solola


"""

import unittest

from solutions.modulus import modulus


class TestModulus(unittest.TestCase):
    """
    Unit tests for the modulus function.
    """

    def test_positive_numbers(self):
        """Test modulus with positive numbers."""
        self.assertEqual(modulus(10, 3), 1)
        self.assertEqual(modulus(25, 4), 1)
        self.assertEqual(modulus(100, 7), 2)

    def test_negative_numbers(self):
        """Test modulus with negative numbers."""
        self.assertEqual(modulus(-10, 3), -1)
        self.assertEqual(modulus(-10, -3), -1)
        self.assertEqual(modulus(10, -3), 1)

    def test_zero_numerator(self):
        """Test modulus when the numerator is zero."""
        self.assertEqual(modulus(0, 5), 0)

    def test_zero_denominator(self):
        """Test modulus when the denominator is zero."""
        with self.assertRaises(ValueError):
            modulus(10, 0)

    def test_float_inputs(self):
        """Test modulus with floating-point numbers."""
        self.assertAlmostEqual(modulus(10.5, 3), 1.5)
        self.assertAlmostEqual(modulus(-10.5, 3), -1.5)
        self.assertAlmostEqual(modulus(-10.5, -3), -1.5)
        self.assertAlmostEqual(modulus(10.5, -3), 1.5)


def test_large_and_small_numbers(self):
    """Test modulus with very large and very small numbers."""
    self.assertEqual(modulus(1e18, 3), 1)
    self.assertAlmostEqual(modulus(1, 1e-10), 0)


def test_defensive_inputs(self):
    """Test modulus with invalid or unusual inputs."""
    with self.assertRaises(TypeError):
        modulus("10", 3)  # When Numerator is a string
    with self.assertRaises(TypeError):
        modulus(10, "3")  # When Denominator is a string
    with self.assertRaises(TypeError):
        modulus(None, 3)  # When Numerator is None
    with self.assertRaises(TypeError):
        modulus(10, None)  # When Denominator is None


if __name__ == "__main__":
    unittest.main()
