import yaml
from yaml.loader import FullLoader
from pathlib import Path
import configs

class Config:
    def __init__(self):
        self.config_file_paths = self._get_config_file_paths()
        self._config = self._create_config()
        self._set_parameters()

    def _get_config_file_paths(self):
        config_path = Path(configs.__file__).parent
        return [config for config in config_path.iterdir() if (config.is_file() and config.suffix == ".yml")]
    
    def _create_config(self):
        config = {}
        for config_file_path in self.config_file_paths:
            with open(config_file_path) as config_file:
                config.update(yaml.load(config_file, Loader=FullLoader))
        return config

    def _set_parameters(self):
        self.parameters = {}
        for key, value in self._config.items():
            self.parameters[key] = value
