"""
A module for calculating the minimum value from a list of values.

Module contents:
    - find_minimum_value: returns the lowest value in a list

Created on 2024-12-28
Author: Lukmon Olamilekan Alao
"""


def find_minimum_value(values: list):
    """Returns the lowest value from a list of numbers input

    takes a list of numbers and return a single number which is the lowest value from the list.

    Parameters:
        values: list, the input values to process

    Returns -> number: the lowest value from the list of numbers.

    Raises:
        AssertionError: if input is not a list and non-numeric input data

    Examples:
        >>> find_minimum_value([1, 2, 3, 4])
        1
        >>> find_minimum_value([2.24, 4, 5.23, 1])
        1
        >>> find_minimum_value([1.2, 3.4, 2.7, 0.5])
        0.5
    """

    # trunk-ignore(bandit/B101)
    assert isinstance(values, list)  # verifies that 'values' is a list

    # trunk-ignore(bandit/B101)
    assert all(
        isinstance(item, (int, float)) for item in values
    )  # "values must be an int or a float"
    ordered_list_of_values = sorted(values)  # returns the list in ascending order
    lowest = ordered_list_of_values[0]  # gives the minimum value from the ordered list
    return lowest
