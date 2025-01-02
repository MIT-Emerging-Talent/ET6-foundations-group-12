#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating the percentage of one number relative to another.

Module contents:
    - calculate_percentage: calculates what percentage the first number is of the second.

Created on 26.12.2024
@author: Yevheniia Rudenko
"""


def calculate_percentage(numerator: float, denominator: float) -> float:
    """This function calculates the percentage by dividing numerator by denominator and then multiplying by 100.

    Parameters:
        numerator: float, the numerator value
        denominator: float, the denominator value

    Returns -> float: the percentage of `numerator` in `denominator`

    Raises:
        AssertionError: if any argument is not a number
        ZeroDivisionError: if `denominator` is zero

    >>> calculate_percentage(50, 200)
    25.0
    >>> calculate_percentage(5, 20)
    25.0
    >>> calculate_percentage(0, 100)
    0.0
    """
    assert isinstance(numerator, (int, float)), "numerator must be a number"
    assert isinstance(denominator, (int, float)), "denominator must be a number"
    if denominator == 0:
        raise ZeroDivisionError("denominator must not be zero")

    return (numerator / denominator) * 100
