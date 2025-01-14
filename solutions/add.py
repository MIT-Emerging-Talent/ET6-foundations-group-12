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
    """Add two numbers and returns their sum.

    Parameters:
        num1:(int, float), the first number to be added
        num2:(int, float), the second number to be added

    Returns -> float: the sum of num1 and num2

    Raises:
        AssertionError: if num1 or num2 is not an integer or float

    >>> add(4, 6)
    10.0
    >>> add(0, 0)
    0.0
    >>> add(7, -3)
    4.0
    >>> add(-5, -3)
    -8.0

    >>> add(7, -3)
    4.0
    >>> add(-5, -3)
    -8.0

    """
    # Validate inputs
    assert isinstance(num1, (int, float)), "num1 must be a int or float"
    assert isinstance(num2, (int, float)), "num2 must be a int or float"
    return float(num1 + num2)
