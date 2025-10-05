# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Addition Tests ---
    def test_addition_positive_numbers(self):
        """Test addition of positive numbers."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 15), 25)

    def test_addition_negative_numbers(self):
        """Test addition with negative numbers."""
        self.assertEqual(self.calc.add(-2, -3), -5)
        self.assertEqual(self.calc.add(-5, 10), 5)

    def test_addition_with_zero(self):
        """Test addition involving zero."""
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(7, 0), 7)

    # --- Subtraction Tests ---
    def test_subtraction_positive_numbers(self):
        """Test subtraction of positive numbers."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(5, 10), -5)

    def test_subtraction_negative_numbers(self):
        """Test subtraction with negative numbers."""
        self.assertEqual(self.calc.subtract(-5, -5), 0)
        self.assertEqual(self.calc.subtract(-10, 5), -15)

    def test_subtraction_with_zero(self):
        """Test subtraction involving zero."""
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(7, 0), 7)

    # --- Multiplication Tests ---
    def test_multiplication_positive_numbers(self):
        """Test multiplication of positive numbers."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(5, 5), 25)

    def test_multiplication_negative_numbers(self):
        """Test multiplication with negative numbers."""
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_multiplication_with_zero(self):
        """Test multiplication involving zero."""
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(50, 0), 0)

    # --- Division Tests ---
    def test_division_positive_numbers(self):
        """Test division of positive numbers."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)

    def test_division_negative_numbers(self):
        """Test division involving negative numbers."""
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_division_by_zero(self):
        """Test that dividing by zero returns None."""
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_division_with_zero_numerator(self):
        """Test division when numerator is zero."""
        self.assertEqual(self.calc.divide(0, 5), 0)

# Entry point for running the tests
if __name__ == "__main__":
    unittest.main()
