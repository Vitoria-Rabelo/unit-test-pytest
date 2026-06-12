import unittest
import calculator

class Test_Calculator(unittest.TestCase):
    def test_add_functionalty(self):
        result = calculator.calc_add(1, 2)
        self.assertEqual(result, 3)

    def test_add_funcionality_two_negative_numbers(self):
        result = calculator.calc_add(-1, -2)
        self.assertEqual(result, -3)
