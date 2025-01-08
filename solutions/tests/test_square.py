import unittest
from solutions.square import square


class TestSquareFunction(unittest.TestCase):
    """
    Unit tests for the square function.
    Methods:
    - test_square_positive_integer: Tests the square of a positive integer.
    - test_square_negative_integer: Tests the square of a negative integer.
    - test_square_zero: Tests the square of zero.
    - test_square_positive_float: Tests the square of a positive float.
    """

    def test_square_positive_integer(self):
        """
        Test if square function correctly squares a positive integer.
        Verifies the function correctly calculates the square of:
        - Positive numbers
        """
        self.assertEqual(square(2), 4)

    def test_square_negative_integer(self):
        """
        Test if square function correctly squares a negative integer.
        Verifies the function correctly calculates the square of:
        - Negative numbers
        """
        self.assertEqual(square(-3), 9)

    def test_square_zero(self):
        """
        Test if square function correctly squares zero.
        Verifies the function correctly calculates the square of:
        - Zero
        """
        self.assertEqual(square(0), 0)

    def test_square_positive_float(self):
        """
        Test if square function correctly squares a positive float.
        Verifies the function correctly calculates the square of:
        - Positive Decimal Numbers
        """
        self.assertAlmostEqual(square(1.5), 2.25)

    def test_square_negative_float(self):
        """
        Test if square function correctly squares a negative float.
        Verifies the function correctly calculates the square of:
        - Negatve Decimal Numbers
        """
        self.assertAlmostEqual(square(-2.5), 6.25)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
