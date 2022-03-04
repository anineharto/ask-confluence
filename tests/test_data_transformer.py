import data.raw as raw_data_path
import data.interim as interim_data_path
from ask_confluence.config import Config
from ask_confluence.data_transformer import DataTransformer

class TestDataTransformer:

    @staticmethod
    def test_json_merge_to_jsonl(monkeypatch, mock_raw_data_file_path, mock_interim_data_file_path, mock_config_file_path):
        def get_mock_config_file_path(self):
            return [mock_config_file_path]
        monkeypatch.setattr(Config, "_get_config_file_paths", get_mock_config_file_path)
        monkeypatch.setattr(raw_data_path, "__file__", mock_raw_data_file_path)
        monkeypatch.setattr(interim_data_path, "__file__", mock_interim_data_file_path)

        mock_interim_data_file_path.unlink()
        assert not mock_interim_data_file_path.is_file()
        DataTransformer().json_merge_to_jsonl()
        assert mock_interim_data_file_path.is_file()

