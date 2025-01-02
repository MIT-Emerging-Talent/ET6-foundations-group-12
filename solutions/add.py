#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for adding two numbers.

Module contents:
    -add: adds two numbers and returns the result.

Created on 28.12.2024
@author : Ridwan Ayinde

"""


def add(num1: float, num2: float) -> float:
    """Add two numbers.

    Parameters:
        num1:float, the first number
        num2:float, the second number

    Returns -> float: the sum of num1 and num2

    Raises:
        AssertionError: if any argument is not a number

    >>> add(4, 6)
    10.0
    >>> add(0, 0)
    0.0
    >>> add(7, -3)
    4.0
    >>> add(-5, -3)
    -8.0

    """
    # Validate inputs
    assert isinstance(num1, (int, float)), "num1 must be a number"
    assert isinstance(num2, (int, float)), "num2 must be a number"
    return float(num1 + num2)
