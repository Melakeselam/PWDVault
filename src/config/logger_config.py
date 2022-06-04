import logging
from pathlib import Path

from src.config.configuration import Configuration

level_map = dict(notset = logging.NOTSET,
    debug = logging.DEBUG,
    info = logging.INFO,
    warning = logging.WARNING,
    error = logging.ERROR,
    critical = logging.CRITICAL)

class Log:
    def __init__(self, logging_env_var:Configuration, is_non_prod:bool = False) -> None:
        app_dir = Path(__file__).absolute().parent
        destination_file = logging_env_var.get('destination')
        level = logging_env_var.get('level')
        log_format = logging_env_var.get('format')
        log_file_mode = logging_env_var.get('filemode') 
        if not log_file_mode:
            log_file_mode = 'a'
        if is_non_prod:
            print(f'Current Logging Level: {level.upper()}')
        logging.basicConfig(filename = app_dir / destination_file, level = level_map[level], format= log_format, filemode=log_file_mode)
        self._logger = logging.getLogger()

    def logger(self):
        return self._logger
