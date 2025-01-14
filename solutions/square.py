#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for computing the square value of  a given number.

Module contents:
    - square: Computes the absolute value of a given number.

Created on 12-31-2024

@author: Ayomide Ayodele
"""


def square(num: int | float) -> int | float:
    """
    Calculate the square of a number.

    Parameters:
    num (int | float): The number to be squared.

    Returns:
    int | float: The square of the input number, preserving int type if applicable.

    Examples:
    >>> square(2)
    4
    >>> square(-3)
    9
    >>> square(0)
    0
    >>> square(1.5)
    2.25
    """
    if not isinstance(num, (int, float)):
        raise TypeError(f"The input: {num} must be an int or float")
    result = num**2
    return int(result) if isinstance(num, int) else float(result)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
