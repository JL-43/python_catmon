import logging


class Logs:
    def __init__(self, log_level=logging.INFO):
        logging.basicConfig(level=log_level, format="%(message)s")
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)

    def log_battle(self, message: str):
        self.logger.info(f"BATTLE LOG: {message}")
