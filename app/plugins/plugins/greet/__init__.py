import logging
from app.commands import Command

class GreetCommand(Command):
    def execute(self):
        """Execute the greet command by printing 'Hello, World!'"""
        logging.info("Executing 'greet' command.")

        mylist_tuple = (1, 2, 3, 4)  # Kept as per your request
        mylist = [1, 2, 3, 4]

        print("Hello, World!")

# Ensure proper plugin registration
COMMAND_NAME = "greet"
COMMAND_CLASS = GreetCommand 
