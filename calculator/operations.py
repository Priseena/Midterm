"""
This module contains functions for basic arithmetic operations.
"""

def add(a,b):
    """
    Return the sum of the two numbers.
    """
    return a + b

def subtract(a,b):
    """
    Return the difference of the two numbers.
    """
    return a - b

def multiply(a,b):
    """
    Return the product of the two numbers.
    """
    return a * b

def divide(a,b):
    """
    Return the quotient of the two numbers.
    
    Raises:
        ZeroDivisionError: If the second number is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b
