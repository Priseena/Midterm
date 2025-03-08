import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, filename='calculator.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Calculator:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Calculator, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def add(self, a, b):
        result = a + b
        logger.info(f'Add: {a} + {b} = {result}')
        return result

    def subtract(self, a, b):
        result = a - b
        logger.info(f'Subtract: {a} - {b} = {result}')
        return result

    def multiply(self, a, b):
        result = a * b
        logger.info(f'Multiply: {a} * {b} = {result}')
        return result

    def divide(self, a, b):
        if b == 0:
            logger.error('Divide by zero error')
            raise ZeroDivisionError("Cannot divide by zero!")
        result = a / b
        logger.info(f'Divide: {a} / {b} = {result}')
        return result

class HistoryManager:
    def __init__(self):
        self.history = pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])

    def add_record(self, operation, operand1, operand2, result):
        new_record = {"operation": operation, "operand1": operand1, "operand2": operand2, "result": result}
        self.history = self.history.append(new_record, ignore_index=True)

    def save_history(self, filename="history.csv"):
        self.history.to_csv(filename, index=False)

    def load_history(self, filename="history.csv"):
        self.history = pd.read_csv(filename)

    def clear_history(self):
        self.history = pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])

    def delete_history(self, filename="history.csv"):
        import os
        if os.path.exists(filename):
            os.remove(filename)
