import logging


class Logs:
    def __init__(self, log_level=logging.INFO):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)  # Explicitly set the log level
        logging.basicConfig(level=log_level, format="%(message)s")

    def log_battle(self, message: str):
        self.logger.info(f"BATTLE LOG: {message}")

    # Additional logging methods for other game events can be added here
