#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for generating exponentiation of two numbers (inputs) "a base (float)" and "an exponent (int)"

Module contents:
    - Exponentiation: finds the exponents of two numbers; both integers and floats.

Created on 05.01.2025
@author: Zephaniah Okoye
"""


def exponentiation(base: float, exponent: int) -> float:
    """
    Compute the exponentiation of a base raised to a given exponent.

    The function calculates base^exponent, which is the base multiplied
    by itself exponent times. For example, 2^3 is 2 * 2 * 2 = 8.

    Parameters:
      base (float): The base number to be raised.
      exponent (int): The exponent to which the base is raised.

    Returns:
      float: The result of the base raised to the given exponent.

    Raises:
      TypeError: If the base is not a float or the exponent is not an int.

    Examples:
      >>> exponentiation(2, 3)
      8.0
      >>> exponentiation(5, 0)
      1.0
      >>> exponentiation(1.5, 2)
      2.25
      >>> exponentiation(2, -2)
      0.25
    """
    if not isinstance(base, (float, int)):
        raise TypeError("The base must be a float or int")
    if not isinstance(exponent, int):
        raise TypeError("The exponent must be an int")

    return base**exponent
