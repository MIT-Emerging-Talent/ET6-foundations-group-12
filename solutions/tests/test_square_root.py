import unittest
from solutions.square_root import square_root


class TestSquareRootFunction(unittest.TestCase):
    """
    Unit tests for the square_root function.
    Methods:
    - test_square_root: Tests the square root of positive numbers, zero, and raises errors for negative numbers.
    """

    def test_square_root_of_positive_number(self):
        """
        Test square root of a positive number.
        Verifies that the square root of a positive number is calculated correctly.
        """
        self.assertEqual(square_root(4), 2)

    def test_square_root_of_zero(self):
        """
        Test square root of zero.
        Verifies that the square root of zero is 0.
        """
        self.assertEqual(square_root(0), 0)

    def test_square_root_of_decimal(self):
        """
        Test square root of a decimal number.
        Verifies that the square root of a decimal number is calculated correctly.
        """
        self.assertAlmostEqual(square_root(2.25), 1.5)

    def test_square_root_of_negative_number(self):
        """
        Test square root of a negative number (should raise ValueError).
        Verifies that the function raises a ValueError for negative numbers.
        """
        with self.assertRaises(ValueError):
            square_root(-4)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
