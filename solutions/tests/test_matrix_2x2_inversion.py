#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for testing the matrix_2x2_inversion function.

Test categories:
    - Standard test cases: test the function with typical inputs.
    - Edge test cases: test the function with extreme inputs.
    - Defensive tests: test the function with invalid inputs.


Created on 2024-12-26
Author: Awaab98
"""

import unittest
from solutions.matrix_2x2_inversion import matrix_2x2_inversion


class TestMatrix2x2Inversion(unittest.TestCase):
    """Tests suite for the matrix_2x2_inversion function."""

    # Standard test cases
    def test_matrix_with_integer_elements(self):
        """It should return the inverse of the input matrix, handling integers."""
        self.assertEqual(
            matrix_2x2_inversion([[1, 2], [3, 4]]), [[-2.0, 1.0], [1.5, -0.5]]
        )

    def test_matrix_with_float_elements(self):
        """It should return the inverse of the input matrix, handling floats."""
        self.assertEqual(
            matrix_2x2_inversion([[1.0, 2.0], [3.0, 4.0]]), [[-2.0, 1.0], [1.5, -0.5]]
        )

    def test_matrix_with_mixed_elements(self):
        """It should return the inverse of the input matrix, handling mixed-types elements."""
        self.assertEqual(
            matrix_2x2_inversion([[1, 2.0], [3, 4]]), [[-2.0, 1.0], [1.5, -0.5]]
        )

    def test_matrix_with_negative_elements(self):
        """It should return the inverse of the input matrix, handling negative elements."""
        self.assertEqual(
            matrix_2x2_inversion([[-1, -2], [-3, -4]]), [[2.0, -1.0], [-1.5, 0.5]]
        )

    def test_identity_matrix(self):
        """It should return the identity matrix."""
        self.assertEqual(matrix_2x2_inversion([[1, 0], [0, 1]]), [[1, 0], [0, 1]])

    def test_symmetric_matrix(self):
        """It should return the inverse."""
        self.assertEqual(
            matrix_2x2_inversion([[2, 1], [1, 2]]),
            [
                [0.6666666666666666, -0.3333333333333333],
                [-0.3333333333333333, 0.6666666666666666],
            ],
        )

    # Edge test cases
    def test_matrix_with_zero_determinant(self):
        """It should raise a ValueError because the determinant is zero."""
        with self.assertRaises(ValueError):
            matrix_2x2_inversion([[1, 1], [2, 2]])

    def test_matrix_with_zero_elements(self):
        """It should raise a ValueError because the determinant is zero."""
        with self.assertRaises(ValueError):
            matrix_2x2_inversion([[0, 0], [0, 0]])

    # Defensive test cases
    def test_non_list_input(self):
        """It should raise a TypeError because the input is not a list of lists."""
        with self.assertRaises(TypeError):
            matrix_2x2_inversion("1, 2, 3, 4")

    def test_non_numeric_elements(self):
        """It should raise a TypeError because the input matrix contains non-numeric elements."""
        with self.assertRaises(TypeError):
            matrix_2x2_inversion([[1, 2], [3, "4"]])

    def test_non_2x2_matrix(self):
        """It should raise an AssertionError because the input matrix is not a 2x2 matrix."""
        with self.assertRaises(AssertionError):
            matrix_2x2_inversion([[1, 2, 3], [4, 5, 6]])

    def test_zero_determinant_matrix(self):
        """It should raise a ValueError because the determinant is zero."""
        with self.assertRaises(ValueError):
            matrix_2x2_inversion([[1, 1], [2, 2]])
