import logging
from abc import ABC, abstractmethod

# Configure logging
logger = logging.getLogger(__name__)

# Define the base abstract class Command
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# CsvCommand - Handling CSV-related tasks
class CsvCommand(Command):
    def execute(self):
        logger.info("Executing CsvCommand: Handling CSV data...")
        print("Executing CsvCommand: Handling CSV data...")
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
        logger.info("DataCommand executed successfully.")

# GreetCommand - Simple greeting output
class GreetCommand(Command):
    def execute(self):
        logger.info("Executing 'greet' command.")
        print("Hello, World!")

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
