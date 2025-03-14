import logging
from abc import ABC, abstractmethod
import pandas as pd

# Configure Singleton Logger
class SingletonLogger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonLogger, cls).__new__(cls)
            logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w',
                                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            cls._instance.logger = logging.getLogger("SingletonLogger")
        return cls._instance

logger = SingletonLogger().logger

# Define the base abstract class Command
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# CsvCommand - Handling CSV-related tasks (using Facade for Pandas operations)
class CsvCommand(Command):
    def execute(self):
        logger.info("Executing CsvCommand: Handling CSV data...")
        # Simulate a DataFrame operation using a Facade-like structure
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        logger.info("Original DataFrame:")
        logger.info(f"\n{df}")

        filtered_df = df[df['A'] > 1]
        logger.info("Filtered DataFrame (A > 1):")
        logger.info(f"\n{filtered_df}")

        summary = df.describe()
        logger.info("Summary Statistics:")
        logger.info(f"\n{summary}")

        print("CsvCommand executed: Check logs for details.")
        logger.info("CsvCommand executed successfully.")

# DataCommand - Handling dictionary, set, list, and tuple operations
class DataCommand(Command):
    def execute(self):
        logger.info("Executing DataCommand: Processing structured data...")
        my_list = ['apple', 'banana', 'cherry']
        logger.info(f'List: {my_list}')
        my_tuple = (1, 2, 3, 4)
        logger.info(f'Tuple: {my_tuple}')
        my_set = {1, 2, 3, 4}
        logger.info(f'Set: {my_set}')
        states_abbreviations = {'CA': 'California', 'TX': 'Texas'}
        logger.info(f'Dictionary: {states_abbreviations}')
        print("DataCommand executed: Check logs for details.")
        logger.info("DataCommand executed successfully.")

# GreetCommand - Simple greeting output
class GreetCommand(Command):
    def execute(self):
        logger.info("Executing 'greet' command.")
        print("Hello, World!")
        logger.info("GreetCommand executed successfully.")

# Calculator strategies for Strategy Pattern
class AdditionStrategy:
    def execute(self, a, b):
        return a + b

class SubtractionStrategy:
    def execute(self, a, b):
        return a - b

class Calculator(Command):
    def __init__(self, strategy):
        self.strategy = strategy

    def calculate(self, a, b):
        logger.info(f"Performing calculation: {self.strategy.__class__.__name__} with inputs {a} and {b}")
        return self.strategy.execute(a, b)

    def execute(self):
        logger.info("Executing Calculator command: Strategy-based operation.")

# Factory Method for Commands
class CommandFactory:
    @staticmethod
    def create_command(command_type: str):
        if command_type == "csv":
            return CsvCommand()
        elif command_type == "data":
            return DataCommand()
        elif command_type == "greet":
            return GreetCommand()
        elif command_type == "calculator_add":
            return Calculator(AdditionStrategy())
        elif command_type == "calculator_sub":
            return Calculator(SubtractionStrategy())
        else:
            raise ValueError(f"Unknown command type: {command_type}")

# CommandHandler class for managing commands
class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command
        logger.info(f"Registered command: {command_name}")

    def execute_command(self, command_name: str):
        if command_name in self.commands:
            logger.info(f"Executing command: {command_name}")
            try:
                self.commands[command_name].execute()
                logger.info(f"Command {command_name} executed successfully.")
            except Exception as e:
                logger.error(f"Error executing {command_name}: {e}")
        else:
            logger.warning(f"No such command: {command_name}")
            print(f"No such command: {command_name}")
