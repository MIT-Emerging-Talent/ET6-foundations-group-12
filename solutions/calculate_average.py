#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating the average of two numbers.

Module contents:
    - calculate_average: calculates the average of two numbers.

Created on 26.12.2024
@author: Yevheniia Rudenko
"""


def calculate_average(the_first_number: float, the_second_number: float) -> float:
    """Calculate the average of two numbers.

    Parameters:
        the_first_number: float, the first number
        the_second_number: float, the second number

    Returns:
        float: the average of the two numbers

    Raises:
        TypeError: if any argument is not a number

    Examples:
        >>> calculate_average(4, 6)
        5.0
        >>> calculate_average(10, 20)
        15.0
        >>> calculate_average(-3, 3)
        0.0
    """
    if not isinstance(the_first_number, (int, float)):
        raise TypeError(
            f"the_first_number must be a number, got {type(the_first_number).__name__}"
        )
    if not isinstance(the_second_number, (int, float)):
        raise TypeError(
            f"the_second_number must be a number, got {type(the_second_number).__name__}"
        )

    return (the_first_number + the_second_number) / 2
