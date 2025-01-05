#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2024-12-27

Author: Lukmon Alao
"""

def find_maximum_value(values: list):
    """Returns the highest value from a list of numbers input
    
    takes a list of numbers and return a single number which is the highest value from the list.
    
    Parameters:
        values: list, the input values to process
        
    Returns -> number: the highest value from the list of numbers.
    
    Raises:
        AssertionError: if input is not a list and numerical
        
    Examples:
        >>> find_maximum_value([1, 2, 3, 4])
        4
        >>> find_maximum_value([2.24, 4, 5.23, 1])
        5.23
        >>> find_maximum_value([1.2, 3.4, 2.7, 0.5])
        3.4
    """
    #values = [input(print('enter a list of number to be processed'))]
  
    assert isinstance(values, list)
    ordered_list_of_values = sorted(values)
    max = ordered_list_of_values[-1]
    return max
