import os
import pkgutil
import importlib
import sys
import logging
import logging.config
from dotenv import load_dotenv
from app.commands import CommandHandler, CsvCommand, GreetCommand, DataCommand
from app.calculator.calculator.operations import add, subtract, multiply, divide

class CalculatorCommand:
    def execute(self, operation_data):
        try:
            # Split the input into operation and operands
            operation, num1, num2 = operation_data.split()
            num1, num2 = float(num1), float(num2)

            # Perform the arithmetic operation
            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 == 0:
                    return "Error: Division by zero is not allowed."
                result = num1 / num2
            else:
                return f"No such operation: {operation}"

            return f"Result: {result}"

        except ValueError:
            return "Invalid format. Use commands like 'add 2 2'."      
class App:
    def __init__(self):
        """Initialize the application, configure logging, and load plugins."""
        os.makedirs("logs", exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault("ENVIRONMENT", "PRODUCTION")

        self.command_handler = CommandHandler()
        self.load_plugins()  # Automatically load plugins
        self.register_builtin_commands()  # Manually register missing commands

    def configure_logging(self):
        """Configure logging for the application."""
        logging_conf_path = "logging.conf"
        log_filename = "logs/app.log"

        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(
                level=logging.INFO,
                format="%(asctime)s - %(levelname)s - %(message)s",
                handlers=[
                    logging.FileHandler(log_filename),
                    logging.StreamHandler(sys.stdout)
                ]
            )
        logging.info("Logging configured.")

    def load_environment_variables(self):
        """Load environment variables into settings."""
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, key: str, default=None):
        """Retrieve an environment variable, returning a default if not found."""
        return self.settings.get(key, default)

    def load_plugins(self):
        """Dynamically load all command plugins from the `app/plugins/` directory."""
        plugins_path = os.path.join(os.path.dirname(__file__), "plugins")
        if not os.path.exists(plugins_path):
            logging.warning("Plugins directory not found.")
            return

        logging.info("Loading plugins...")
        for _, module_name, _ in pkgutil.iter_modules([plugins_path]):
            module_path = f"app.plugins.{module_name}"
            try:
                module = importlib.import_module(module_path)
                if hasattr(module, "COMMAND_NAME") and hasattr(module, "COMMAND_CLASS"):
                    command_name = module.COMMAND_NAME
                    command_class = module.COMMAND_CLASS
                    self.command_handler.register_command(command_name, command_class())
                    logging.info(f"Registered command: {command_name}")
            except Exception as e:
                logging.error(f"Failed to load plugin {module_name}: {e}")

    def register_builtin_commands(self):
        """Manually register core commands in case they are not plugins."""
        self.command_handler.register_command("csv", CsvCommand())
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("data", DataCommand())
        self.command_handler.register_command("add", CalculatorCommand())
        self.command_handler.register_command("subtract", CalculatorCommand())
        self.command_handler.register_command("multiply", CalculatorCommand())
        self.command_handler.register_command("divide", CalculatorCommand())
        logging.info("Builtin commands registered: csv, greet, data,add, subtract, multiply, divide")

    def start(self):
        """Start the REPL loop to accept user commands."""
        logging.info("Starting REPL...")
        while True:
            try:
                user_input = input(">>> ").strip().lower()
                if user_input == "exit":
                    logging.info("Exiting application.")
                    exit(0)
                elif user_input in self.command_handler.commands:
                    self.command_handler.execute_command(user_input)
                else:
                    print(f"No such command: {user_input}")
            except Exception as e:
                logging.error(f"Error in REPL: {e}")
