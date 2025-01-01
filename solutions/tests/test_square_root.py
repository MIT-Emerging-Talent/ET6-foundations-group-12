# The test case for the square root function of the Calculator
import unittest
from solutions.square_root import square_root


class TestSquareRootFunction(unittest.TestCase):
    """
    Unit tests for the `square_root` function.

    Methods:
    - test_square_root: Tests the square root of positive numbers, zero, and raises errors for negative numbers.
    """

    def test_square_root(self):
        """
        Test cases for the square root function.

        Verifies the function correctly calculates the square root of:
        - Positive numbers
        - Zero

        Ensures the function raises a ValueError for negative numbers.
        """
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(0), 0)
        self.assertAlmostEqual(square_root(2.25), 1.5)

        with self.assertRaises(ValueError):
            square_root(-4)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
