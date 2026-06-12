import unittest
from calculator_v2 import Calculator

class TestCalculatorV2(unittest.TestCase):
    """
    Tests for the base functionality of the calculator class
    """
    def test_add_funcionality(self):
        """
        Test case to test add functionality with two positive numbers
        """
        calc1 = Calculator(2, 3)
        result = calc1.calc_add()
        self.assertEqual(result, 5)

    def test_add_functionality_with_one_negative_number(self):
        """
        Test case to test add functionality with two negative numbers
        """
        calc1 = Calculator(10, -30)
        result = calc1.calc_add()
        self.assertEqual(result, -20)