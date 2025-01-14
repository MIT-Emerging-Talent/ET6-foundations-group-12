#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for computing absolute value of  a given number.

Module contents:
    - absolute_value: Computes the absolute value of a given number.

Created on 12-27-2024

@author: Abdul Qader Dost
"""


def absolute_value(number: float) -> float:
    """The absolute_value function computes the absolute value of a given number.
    The absolute value of a number is its distance from zero, regardless of its sign.
    For example, the absolute value of both -5 and 5 is 5. This function works for
    both integer and floating numbers.

    Parameters:
      number: int, float, A number whose absolute value is to be computed.

    Returns -> float, Returns the absolute value of the input number.

    Raises:
      TypeError: If the input is not a number (int or float).

    >>> absolute_value(0)
    0

    >>> absolute_value(10)
    10

    >>> absolute_value(-10)
    10
    """
    # the number should be an integer or float
    if not isinstance(number, (int, float)):
        raise TypeError(f"The input: {number} must be an int or float")

    # Return the absolute value
    return number if number >= 0 else -number
