"""
created 2024-12-28

@author: Lukmon Alao
"""

def find_minimum_value(values: list):
    """Returns the lowest value from a list of numbers input
    
    takes a list of numbers and return a single number which is the lowest value from the list.
    
    Parameters:
        values: list, the input values to process
        
    Returns -> number: the lowest value from the list of numbers.
    
    Raises:
        AssertionError: if input is not a list and numerical
        
    Examples:
        >>> find_minimum_value([1, 2, 3, 4])
        1
        >>> find_minimum_value([2.24, 4, 5.23, 1])
        1
        >>> find_minimum_value([1.2, 3.4, 2.7, 0.5])
        0.5
    """
    assert isinstance(values, list)  #verifies that 'values' is a list 
    ordered_list_of_values = sorted(values) #returns the list in ascending order
    min = ordered_list_of_values[0]  #gives the minimum value from the ordered list
    return min
