def square_root(num: int | float) -> int | float:
    """
    Calculate the square root of a number.

    Parameters:
    num (int | float): The number to find the square root of. Must be non-negative.

    Returns:
    int | float: The square root of the input number. Returns an int if the result is a whole number, otherwise a float.

    Raises:
    ValueError: If the input number is negative.

    Examples:
    >>> square_root(4)
    2
    >>> square_root(0)
    0
    >>> square_root(2.25)
    1.5
    >>> square_root(10)
    3.1622776601683795
    >>> square_root(-4)  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ValueError: Cannot calculate the square root of a negative number.
    """
    if num < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")

    result = num**0.5
    return int(result) if result.is_integer() else result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
