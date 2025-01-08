def square(num: int | float) -> int | float:
    """
    Calculate the square of a number.

    Parameters:
    num (int | float): The number to be squared.

    Returns:
    int | float: The square of the input number, preserving int type if applicable.

    Examples:
    >>> square(2)
    4
    >>> square(-3)
    9
    >>> square(0)
    0
    >>> square(1.5)
    2.25
    """
    result = num**2
    return int(result) if isinstance(num, int) else float(result)
