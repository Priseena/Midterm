"""
This module contains unit tests for the calculations functions.
"""

from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations.
    """
    @staticmethod
    def add(a, b):
        """
        Return the sum of the two numbers.
        """
        calculation = Calculation(a, b, add)
        return calculation.get_result()

    @staticmethod
    def subtract(a, b):
        """
        Return the difference of the two numbers.
        """
        calculation = Calculation(a, b, subtract)
        return calculation.get_result()

    @staticmethod
    def multiply(a, b):
        """
        Return the product of the two numbers.
        """
        calculation = Calculation(a, b, multiply)
        return calculation.get_result()

    @staticmethod
    def divide(a, b):
        """
        Return the quotient of the two numbers.
        """
        calculation = Calculation(a, b, divide)
        return calculation.get_result()