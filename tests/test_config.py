import json
from ask_confluence.config import Config

class TestConfig:

    @staticmethod
    def test_create_config(monkeypatch, mock_config_file_path):
        def get_mock_config_file_path(self):
            return [mock_config_file_path]
        monkeypatch.setattr(Config, "_get_config_file_paths", get_mock_config_file_path)
        expected_config = json.load(open(mock_config_file_path))
        config = Config()
        assert config._config == expected_config
    
    @staticmethod
    def test_set_parameters(monkeypatch, mock_config_file_path):
        def get_mock_config_file_path(self):
            return [mock_config_file_path]
        monkeypatch.setattr(Config, "_get_config_file_paths", get_mock_config_file_path)
        expected_parameters = json.load(open(mock_config_file_path)).keys()
        config = Config()
        for parameter in expected_parameters:
            assert parameter in config.parameters