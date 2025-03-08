import pandas as pd

class HistoryManager:
    def __init__(self):
        # Initialize an empty DataFrame with columns for the operation, operands, and result
        self.history = pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])

    def add_record(self, operation, operand1, operand2, result):
        # Create a new record as a dictionary
        new_record = {"operation": operation, "operand1": operand1, "operand2": operand2, "result": result}
        # Append the new record to the history DataFrame
        self.history = self.history.append(new_record, ignore_index=True)

    def save_history(self, filename="history.csv"):
        # Save the history DataFrame to a CSV file
        self.history.to_csv(filename, index=False)

    def load_history(self, filename="history.csv"):
        # Load the history DataFrame from a CSV file
        self.history = pd.read_csv(filename)

    def clear_history(self):
        # Clear the history DataFrame by reinitializing it
        self.history = pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])

    def delete_history(self, filename="history.csv"):
        import os
        # Delete the CSV file containing the history
        if os.path.exists(filename):
            os.remove(filename)
