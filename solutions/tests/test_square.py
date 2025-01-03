# The test case for the Square function of our calculator
import unittest
from solutions.square import square


class TestSquareFunction(unittest.TestCase):
    """
    Unit tests for the `square` function.

    Methods:
    - test_square: Tests the square of positive, negative, zero, and float numbers.
    """

    def test_square(self):
        """
        Test cases for the square function.

        Verifies the function correctly calculates the square of:
        - Positive numbers
        - Negative numbers
        - Zero
        - Floating-point numbers
        """
        self.assertEqual(square(2), 4)
        self.assertEqual(square(-3), 9)
        self.assertEqual(square(0), 0)
        self.assertAlmostEqual(square(1.5), 2.25)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
