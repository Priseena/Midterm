import logging
import os
import pandas as pd
from app.commands import CsvCommand
from calculator import Calculator
from calculator.history_manager import HistoryManager

# Configure logging
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

def main():
    # Run CsvCommand to handle CSV data
    csv_command = CsvCommand()
    csv_command.execute()

    # Create instances of Calculator and HistoryManager
    calculator = Calculator()
    history_manager = HistoryManager()

    # Test addition
    result_add = calculator.add(3, 5)
    history_manager.add_record('add', 3, 5, result_add)
    print(f'Addition Result: {result_add}')

    # Test subtraction
    result_sub = calculator.subtract(10, 4)
    history_manager.add_record('subtract', 10, 4, result_sub)
    print(f'Subtraction Result: {result_sub}')
    
    # Test multiplication
    result_multiply = calculator.multiply(6, 7)
    history_manager.add_record('multiply', 6, 7, result_multiply)
    print(f'Multiplication Result: {result_multiply}')

    # Test division
    try:
        result_divide = calculator.divide(20, 5)
        history_manager.add_record('divide', 20, 5, result_divide)
        print(f'Division Result: {result_divide}')
    except ZeroDivisionError as e:
        print(f'Error: {e}')

    # View and print history
    print("Calculation History:")
    print(history_manager.history)

    # Print log messages to the console
    with open('app.log', 'r') as log_file:
        print("\nLog Messages:")
        print(log_file.read())

if __name__ == '__main__':
    main()
