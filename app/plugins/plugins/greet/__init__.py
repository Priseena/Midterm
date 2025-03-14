import logging
from app.commands import Command

class GreetCommand(Command):
    def execute(self, *args):
        """Execute the greet command by printing 'Hello, World!'"""
        logging.info("Executing 'greet' command.")
        print("Hello, World!")

# Plugin registration
COMMAND_NAME = "greet"
COMMAND_CLASS = GreetCommand
