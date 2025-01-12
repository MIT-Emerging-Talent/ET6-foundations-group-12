#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for generating the Mode numbers

Module contents:
    - mode_of numbers: finds the mode(s) of a list of numbers.

Created on 12/01/2025
@author: Deborah Oyibo
"""
from collections import Counter

def mode_of_numbers(numbers: list[int]) -> list[int]:
    """Returns the mode(s) of a list of numbers.
    
    The mode is the number that appears most frequently in the list.
    If there are multiple modes, all of them are returned in a list.
    If there is no mode (i.e., all elements appear once), an empty list is returned.
    
    Parameters:
        numbers: A list of integers or floats.
        
    Returns:
        A list of integers (or floats) representing the mode(s) of the input list.
        
    Raises:
        AssertionError: If the input is not a list or if the list contains non-numeric values.
    
    >>> mode_of_numbers([1, 2, 2, 3, 4])
    [2]
    
    >>> mode_of_numbers([1, 2, 2, 3, 3, 4])
    [2, 3]
    
    >>> mode_of_numbers([1, 2, 3, 4])
    []
    
    >>> mode_of_numbers([])
    []
    
    >>> mode_of_numbers([5, 5, 5, 5])
    [5]
    """

    # Check if the input is a list
    assert isinstance(numbers, list), "Input must be a list."
    
    # Check if all elements in the list are numbers (integers or floats)
    assert all(isinstance(num, (int, float)) for num in numbers), "All elements in the list must be numbers."

    # Handle the case for an empty list
    if not numbers:
        return []

    # Count the frequency of each element using Counter
    count = Counter(numbers)

    # Get the highest frequency
    max_frequency = max(count.values())

    # Find all numbers that have the highest frequency
    modes = [num for num, freq in count.items() if freq == max_frequency]

    return modes