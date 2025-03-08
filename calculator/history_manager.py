"""
This module manages the calculation history using Pandas.
"""
import pandas as pd
import os

class HistoryManager:
    """Class to manage calculation history using Pandas."""
    def __init__(self):
        self.history = pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])

    def add_record(self, operation, operand1, operand2, result):
        """Add a new record to history."""
        new_record = pd.DataFrame([{
            "operation": operation,
            "operand1": operand1,
            "operand2": operand2,
            "result": result
        }])
        self.history = pd.concat([self.history, new_record], ignore_index=True)

    def save_history(self, filename="history.csv"):
        """Save history to a CSV file."""
        self.history.to_csv(filename, index=False)

    def load_history(self, filename="history.csv"):
        """Load history from a CSV file if it exists."""
        if os.path.exists(filename):
            self.history = pd.read_csv(filename)

    def clear_history(self):
        """Clear all history records."""
        self.history = pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])

    def delete_history(self, filename="history.csv"):
        """Delete history CSV file if it exists."""
        if os.path.exists(filename):
            os.remove(filename)
