#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module for calculating the inverse of a matrix that has two rows
and two columns.

Module contents:
    - matrix_2x2_inversion: returns the inverse of a 2x2 matrix.

Created on 2024-12-26
Author: Awaab98
"""


def matrix_2x2_inversion(matrix: list[list[float]]) -> list[list[float]]:
    """
    Calculates the inverse of a 2x2 matrix.

    The function calculates the inverse of a 2x2 matrix. The input matrix
    must be an invertible 2x2 matrix (i.e., the determinant is not zero).


    Parameters:
        matrix: list, a list of lists representing a 2x2 matrix in which
        every element is either int of float.

    Returns:
        list: a list of lists representing the inverse of the input matrix.

    Raises:
        TypeError: if the input matrix is not a list of lists.
        TypeError: if one of the elements of the input matrix is not int or float.
        AssertionError: if the input matrix is not a 2x2 matrix.
        ValueError: if the determinant of input matrix is zero.


    Examples:
    >>> matrix_2x2_inversion([[1, 2], [3, 4]])
    [[-2.0, 1.0], [1.5, -0.5]]
    >>> matrix_2x2_inversion([[1.0, 2.0], [3.0, 4.0]])
    [[-2.0, 1.0], [1.5, -0.5]]
    >>> matrix_2x2_inversion([[1, 2.0], [3, 4]])
    [[-2.0, 1.0], [1.5, -0.5]]
    """

    # Check if the input matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("Input matrix must be a list of lists.")

    # Check if the elements of the input matrix are either int or float
    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("Elements of input matrix must be either int or float.")

    # Check if the input matrix is a 2x2 matrix
    if len(matrix) != 2 or not all(len(row) == 2 for row in matrix):
        raise AssertionError("Input matrix must be a 2x2 matrix.")

    # Calculate the determinant
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # If determinant is 0, the matrix is not invertible
    if determinant == 0:
        raise ValueError("Matrix is not invertible because determinant is zero.")

    # Calculate the inverse using the 2x2 matrix formula
    inverse = [
        [matrix[1][1] / determinant, -matrix[0][1] / determinant],
        [-matrix[1][0] / determinant, matrix[0][0] / determinant],
    ]

    return inverse
