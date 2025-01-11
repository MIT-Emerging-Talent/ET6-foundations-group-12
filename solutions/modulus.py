def modulus(a: float, b: float) -> float:
    """
    Calculates the remainder when one number is divided by another.

    Parameters:
    a (float): The numerator (the number to be divided).
    b (float): The denominator (the number to divide by, must be non-zero).

    Returns:
    float: The remainder when 'a' is divided by 'b'.

    Raises:
    ValueError: If the denominator 'b' is zero.
    TypeError: If 'a' or 'b' is not a float or int.

    Examples:
    >>> modulus(10, 3)
    1
    >>> modulus(-10, 3)
    -1
    >>> modulus(10, -3)
    1
    >>> modulus(-10, -3)
    -1
    >>> modulus(10.5, 3)
    1.5
    >>> modulus(0, 3)
    0.0
    >>> modulus(10, 0)  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ValueError: Denominator cannot be zero.
    >>> modulus("10", 3)  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    TypeError: Both numerator and denominator must be numbers.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both numerator and denominator must be numbers.")

    if b == 0:
        raise ValueError("Denominator cannot be zero.")

    remainder = a % b

    # Adjust the result to match the dividend's sign
    if (a < 0 and remainder > 0) or (a > 0 and remainder < 0):
        remainder -= b

    return remainder
