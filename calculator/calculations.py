"""
This module contains the Calculation class for basic arithmetic operations.
"""
from calculator.operations import add, subtract, multiply, divide

class Calculation:
    """Class for performing basic arithmetic operations."""
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation  # Store the operation function

    def get_result(self):
        """Return the result"""
        return self.operation(self.a, self.b)
