#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 12/01/2025

@author: Deborah Oyibo
"""

# test_Mode_of_numbers.py
import unittest

from solutions.mode_of_numbers import mode_of_numbers  # Corrected import

class TestModeOfNumbers(unittest.TestCase):
    """Test the mode_of_numbers function"""

    def test_Mode_0(self):
        """It should return an empty list for an empty input"""
        actual = mode_of_numbers([])
        expected = []
        self.assertEqual(actual, expected)

    def test_Mode_1(self):
        """It should return [2] for a list where 2 appears most frequently"""
        actual = mode_of_numbers([1, 2, 2, 3, 4])
        expected = [2]
        self.assertEqual(actual, expected)

    def test_Mode_2(self):
        """It should return [2, 3] for a list with two modes"""
        actual = mode_of_numbers([1, 2, 2, 3, 3, 4])
        expected = [2, 3]
        self.assertEqual(actual, expected)

    def test_Mode_3(self):
        """It should return an empty list for a list with no repeating numbers"""
        actual = mode_of_numbers([1, 2, 3, 4])
        expected = []
        self.assertEqual(actual, expected)

    def test_Mode_4(self):
        """It should return [5] for a list where 5 appears most frequently"""
        actual = mode_of_numbers([5, 5, 5, 5])
        expected = [5]
        self.assertEqual(actual, expected)

    def test_Mode_5(self):
        """It should return [1] for a list where 1 appears the most times"""
        actual = mode_of_numbers([1] * 1000 + [2] * 500)
        expected = [1]
        self.assertEqual(actual, expected)

    def test_Mode_6(self):
        """It should return [-2] for a list with negative numbers"""
        actual = mode_of_numbers([-1, -2, -2, -3])
        expected = [-2]
        self.assertEqual(actual, expected)

    def test_Mode_7(self):
        """It should return an empty list for a list where no number repeats equally"""
        actual = mode_of_numbers([1, 2, 1, 2])
        expected = []
        self.assertEqual(actual, expected)

    def test_Mode_8(self):
        """It should return an empty list for a list where all numbers appear only once"""
        actual = mode_of_numbers([1, 2, 3, 4, 5, 6])
        expected = []
        self.assertEqual(actual, expected)

    def test_Mode_9(self):
        """It should return [5, 10] for a list with two modes"""
        actual = mode_of_numbers([5, 5, 10, 10, 15])
        expected = [5, 10]
        self.assertEqual(actual, expected)

    def test_Mode_invalid_input(self):
        """It should raise an assertion error for invalid input (non-list)"""
        with self.assertRaises(AssertionError):
            mode_of_numbers("not a list")

    def test_Mode_non_numeric_input(self):
        """It should raise an assertion error if the list contains non-numeric values"""
        with self.assertRaises(AssertionError):
            mode_of_numbers([1, 2, "a"])

if __name__ == '__main__':
    unittest.main()
