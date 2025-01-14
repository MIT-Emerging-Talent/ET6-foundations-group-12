#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for negating numbers.

Module contents:
    - negate: generates the negative of the input number.

Created on 02.01.2025
@author: Abdul Qader Dost
"""


def negate(number: float) -> float:
    """Returns the negation of the input number.

    Parameters: number (float): The number to negate.

    Returns: float: The negation of the input number.

    Raises:
    TypeError: If the argument is not an integer or float.

    >>> negate(2)
    -2

    >>> negate(-2)
    2

    >>> negate(10)
    -10
    """

    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a number")
    return -number
