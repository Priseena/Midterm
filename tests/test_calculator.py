import unittest
from app.calculator.calculator.calculations import Calculation
from app.calculator.calculator.operations import add, subtract, multiply, divide
from app.calculator.calculator.history_manager import HistoryManager

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        self.history_manager = HistoryManager()

    def test_addition(self):
        """Test addition function works"""    
        calc = Calculation(2, 2, add)
        result = calc.get_result()
        self.assertEqual(result, 4)

    def test_subtraction(self):
        """Test subtraction function works"""    
        calc = Calculation(2, 2, subtract)
        result = calc.get_result()
        self.assertEqual(result, 0)

    def test_multiply(self):
        """Test multiplication function works"""    
        calc = Calculation(2, 2, multiply)
        result = calc.get_result()
        self.assertEqual(result, 4)

    def test_divide(self):
        """Test division function works"""    
        calc = Calculation(2, 2, divide)
        result = calc.get_result()
        self.assertEqual(result, 1)

        with self.assertRaises(ZeroDivisionError):
            Calculation(1, 0, divide).get_result()

if __name__ == '__main__':
    unittest.main()
