import logging
import os
from app.commands import CommandHandler, CommandFactory
from calculator import Calculator
from calculator.history_manager import HistoryManager

# Singleton Logger for Logging Configuration
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

def main():
    logger.info("Starting the application...")

    # Initialize CommandHandler
    command_handler = CommandHandler()

    # Register commands using the Factory Pattern
    logger.info("Registering commands using the Command Factory...")
    command_handler.register_command("csv", CommandFactory.create_command("csv"))
    command_handler.register_command("data", CommandFactory.create_command("data"))
    command_handler.register_command("greet", CommandFactory.create_command("greet"))
    command_handler.register_command("add_calc", CommandFactory.create_command("calculator_add"))
    command_handler.register_command("sub_calc", CommandFactory.create_command("calculator_sub"))
    logger.info("Commands registered successfully.")

    # Execute commands
    logger.info("Executing 'csv' command...")
    command_handler.execute_command("csv")

    logger.info("Executing 'data' command...")
    command_handler.execute_command("data")

    logger.info("Executing 'greet' command...")
    command_handler.execute_command("greet")

    # Test calculator commands using Strategy Pattern
    logger.info("Executing calculator commands with strategies...")
    command_handler.execute_command("add_calc")
    command_handler.execute_command("sub_calc")

    # Calculator and HistoryManager for direct calculations
    calculator = Calculator()
    history_manager = HistoryManager()

    # Additional Calculations
    logger.info("Performing additional calculations...")
    # Addition
    result_add = calculator.add(3, 5)
    history_manager.add_record('add', 3, 5, result_add)
    print(f'Addition Result: {result_add}')
    logger.info(f"Addition performed: 3 + 5 = {result_add}")

    # Subtraction
    result_sub = calculator.subtract(10, 4)
    history_manager.add_record('subtract', 10, 4, result_sub)
    print(f'Subtraction Result: {result_sub}')
    logger.info(f"Subtraction performed: 10 - 4 = {result_sub}")

    # Multiplication
    result_multiply = calculator.multiply(6, 7)
    history_manager.add_record('multiply', 6, 7, result_multiply)
    print(f'Multiplication Result: {result_multiply}')
    logger.info(f"Multiplication performed: 6 * 7 = {result_multiply}")

    # Division with exception handling
    try:
        result_divide = calculator.divide(20, 5)
        history_manager.add_record('divide', 20, 5, result_divide)
        print(f'Division Result: {result_divide}')
        logger.info(f"Division performed: 20 / 5 = {result_divide}")
    except ZeroDivisionError as e:
        print(f'Error: {e}')
        logger.error(f"Error during division: {e}")

    # View and print history
    logger.info("Printing calculation history...")
    print("Calculation History:")
    print(history_manager.history)

    # Print log messages to the console
    with open('app.log', 'r') as log_file:
        print("\nLog Messages:")
        print(log_file.read())

    logger.info("Application execution complete.")

if __name__ == '__main__':
    main()
