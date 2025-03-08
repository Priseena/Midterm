import os
import pkgutil
import importlib
import sys
import logging
import logging.config
from dotenv import load_dotenv
from app.commands import CommandHandler, Command

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

    def configure_logging(self):
        """Configure logging for the application."""
        logging_conf_path = "logging.conf"
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(
                level=logging.INFO,
                format="%(asctime)s - %(levelname)s - %(message)s",
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
