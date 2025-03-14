import logging
from app.commands import CommandHandler

# Initialize a logger for the plugins
logger = logging.getLogger(__name__)

# Plugin definitions: Import command classes and set command names
try:
    from app.commands import DataCommand  # Handles data operations
    from app.commands import GreetCommand  # Handles greeting operations
except ImportError as e:
    logger.error(f"Failed to import one or more plugins: {e}")

# Command names for registration
COMMANDS = {
    "data": DataCommand,  # Command to handle data operations
    "greet": GreetCommand,  # Command to greet users
}

def register_plugins(command_handler: CommandHandler):
    """
    Registers all commands from the plugins directory with the command handler.
    :param command_handler: The instance of CommandHandler to register commands.
    """
    for command_name, command_class in COMMANDS.items():
        try:
            command_handler.register_command(command_name, command_class())
            logger.info(f"Registered plugin command: {command_name}")
        except Exception as e:
            logger.error(f"Failed to register command {command_name}: {e}")
