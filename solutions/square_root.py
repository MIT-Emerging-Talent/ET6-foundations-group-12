def square_root(num):
    """
    Calculate the square root of a number.

    Parameters:
    number (float): The number to find the square root of. Must be non-negative.

    Returns:
    float: The square root of the input number.

    Raises:
    ValueError: If the input number is negative.
    """
    if num < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return num**0.5
