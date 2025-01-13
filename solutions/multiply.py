#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module for multiplication of two numbers.

Module contents:
    multiply: Multiplies two numbers (int or float) and returns the result.

Created on 06.01.2025
@author : Simi-Solola
"""


def multiply(a: float, b: float) -> float:
    """
    Multiplies two numbers (int or float) and returns the result.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The result of multiplying `a` and `b`. Returns an `int` if both inputs are integers,
                  otherwise returns a `float`.

    Raises:
    AssertionError: If `a` or `b` is not an int or float.

    Examples:
    >>> multiply(3, 4)
    12
    >>> multiply(2.5, 4)
    10.0
    >>> multiply(-2, 3.5)
    -7.0
    >>> multiply(0, 5)
    0
    """
    # Defensive assertions to ensure valid input types
    assert isinstance(a, (int, float)), "a must be an int or float"
    assert isinstance(b, (int, float)), "b must be an int or float"

    result = a * b
    # Return an int if both inputs are integers, else return a float
    return int(result) if isinstance(a, int) and isinstance(b, int) else float(result)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
