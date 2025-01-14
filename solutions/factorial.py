#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating the factorial of a number.

Module contents:
    - factorial: Calculate the factorial of a number.

Created on 01-03-2024

@author: Abdul Qader Dost
"""


def factorial(number: int) -> int:
    """The factorial function computes the factorial of a given
    non-negative integer. The factorial of a number (n!) is the
    result of multiplying all whole numbers from 1 up to number.
    For example, the factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120.

    Parameters:
      number: int, A non-negative integer whose factorial is to be computed.

    Returns -> int, Returns the factorial of the input number.

    Raises:
      ValueError: If the input is a negative integer.
      TypeError: If the input is not an integer.


    >>> factorial(1)
    1

    >>> factorial(2)
    2

    >>> factorial(3)
    6

    >>> factorial(4)
    24
    """
    # the number should be an integer
    if not isinstance(number, int):
        raise TypeError("The input must be an int or float")

    if number < 0:
        raise ValueError("The input must be a non-negative integer.")

    # Base Case 1
    if number == 0:
        return 1

    return number * factorial(number - 1)
