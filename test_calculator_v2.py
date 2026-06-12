import unittest
from calculator_v2 import Calculator

class TestCalculatorV2(unittest.TestCase):
    def test_add_funcionality(self):
        calc1 = Calculator(2, 3)
        result = calc1.calc_add()
        self.assertEqual(result, 5)

    def test_add_functionality_with_one_negative_number(self):
        calc1 = Calculator(10, -30)
        result = calc1.calc_add()
        self.assertEqual(result, -20)