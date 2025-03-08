import unittest
from calculator import Calculator
from history import HistoryManager

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calculator = Calculator()
        self.history_manager = HistoryManager()

    def test_addition(self):
        '''Test addition function works '''    
        result = self.calculator.add(2, 2)
        self.assertEqual(result, 4)
        self.history_manager.add_record('add', 2, 2, result)
        self.assertEqual(len(self.history_manager.history), 1)

    def test_subtraction(self):
        '''Test subtraction function works '''    
        result = self.calculator.subtract(2, 2)
        self.assertEqual(result, 0)
        self.history_manager.add_record('subtract', 2, 2, result)
        self.assertEqual(len(self.history_manager.history), 2)

    def test_multiply(self):
        '''Test multiplication function works '''    
        result = self.calculator.multiply(2, 2)
        self.assertEqual(result, 4)
        self.history_manager.add_record('multiply', 2, 2, result)
        self.assertEqual(len(self.history_manager.history), 3)

    def test_divide(self):
        '''Test division function works '''    
        result = self.calculator.divide(2, 2)
        self.assertEqual(result, 1)
        self.history_manager.add_record('divide', 2, 2, result)
        self.assertEqual(len(self.history_manager.history), 4)
        with self.assertRaises(ValueError):
            self.calculator.divide(1, 0)

if __name__ == '__main__':
    unittest.main()
