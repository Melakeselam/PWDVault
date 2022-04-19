from configparser import ConfigParser
from pathlib import Path


class Configuration:
    def __init__(self,section:str) -> None:
        app_dir = Path(__file__).absolute().parent
        config_file_read = '../../resources/config.ini'
        config =ConfigParser()
        config.read(app_dir / config_file_read)
        config_sect = config[section]
        keys = list(config_sect)
        self.config_map ={key:config_sect[key] for key in keys}

    def get(self,key:str):
        return self.config_map[key]