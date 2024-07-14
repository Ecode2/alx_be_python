import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-2, -5), -7)
        # Add more assertions to thoroughly test the add method.

    def test_subtract(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(4, 2), 2)
        self.assertEqual(self.calc.subtract(4, 4), 0)
        self.assertEqual(self.calc.subtract(-4, -2), -2)

    def test_multiply(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(4, 2), 8)
        self.assertEqual(self.calc.multiply(-4, 2), -8)
        self.assertEqual(self.calc.multiply(-4, -2), 8)

    def test_divide(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(4, 2), 2)
        self.assertEqual(self.calc.divide(2, 2), 1)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(4, 0), None)
        self.assertIsNone(self.calc.divide(2, 0))

# Remember to write additional test methods for subtract, multiply, and divide.