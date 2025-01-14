#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

"""
A module for subtracting two numbers.

Module contents:
    subtract: subtract one number from another and returns the result.

Created on 31.12.2024
@author : Ridwan Ayinde

"""


def subtract(num1: float, num2: float) -> float:
    """
    Subtract one number from the other.

    Parameters:
        num1:float, the first number
        num2:float, the second number

    Returns -> float : the subtraction of b from a

    Raises:
        AssertionError: if any argument is not a number

    >>> subtract (10, 5)
    5.0
    >>> subtract (-5, 5)
    -10.0
    >>> subtract (-5, -2)
    -3.0
    >>> subtract (-2, -2)
    0.0

    """

    # Validate inputs
    assert isinstance(num1, (int, float)), "a must be a number"
    assert isinstance(num2, (int, float)), " b must be a number"
    return float(num1 - num2)
