#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module for calculating the highest value from a list.

Module contents:
    - find_maximum_value: returns the highest value from a list

Created on 2024-12-26
Author: Lukmon Olamilekan Alao
"""


def find_maximum_value(values: list):
    """Returns the highest value from a list of numbers input

    takes a list of numbers and return a single number which is the highest value from the list.

    Parameters:
        values: list, the input values to process

    Returns -> number: the highest value from the list of numbers.

    Raises:
        TypeError: if input is not a list or a non-numerical data

    Examples:
        >>> find_maximum_value([1, 2, 3, 4])
        4
        >>> find_maximum_value([2.24, 4, 5.23, 1])
        5.23
        >>> find_maximum_value([1.2, 3.4, 2.7, 0.5])
        3.4
    """

    assert isinstance(values, list)
    assert all(
        isinstance(item, (int, float)) for item in values
    )  # "values must be an int or a float"
    ordered_list_of_values = sorted(values)
    highest = ordered_list_of_values[-1]
    return highest
