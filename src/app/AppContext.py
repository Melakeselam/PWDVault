import logging
from src.config.configuration import Configuration
from src.config.logger_config import Log
from src.persistence.persistence import Persistence


class AppContext:
    def __init__(self) -> None:
        self._app_config = Configuration('application')
        self._db_config = Configuration('database')
        self._logging_config = Configuration('local_logging')
        self._persistence = Persistence(self._app_config, self._db_config)
        is_non_prod = True if self._app_config.get('environment') in ['dev','stage'] else False
        self._logger:logging.Logger = Log(self._logging_config, is_non_prod).logger()
    
    def app_config(self):
        return self._app_config

    def db_config(self):
        return self._db_config

    def persistence(self):
        return self._persistence

    def logger(self):
        return self._logger