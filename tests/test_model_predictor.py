from ask_confluence.model_predictor import ModelPredictor
from ask_confluence.config import Config
import data.interim as interim_data_path

class TestModelPredictor:

    @staticmethod
    def test_get_answer(monkeypatch, mocker, mock_interim_data_file_path, mock_config_file_path):
        def get_mock_config_file_path(self):
            return [mock_config_file_path]
        mock_file_id = {"id": "1234"}
        monkeypatch.setattr(Config, "_get_config_file_paths", get_mock_config_file_path)
        monkeypatch.setattr(interim_data_path, "__file__", mock_interim_data_file_path)
        file_create_mocker = mocker.patch(
            "ask_confluence.model_predictor.ModelPredictor._upload_file",
            return_value = mock_file_id
            )
        file_delete_mocker = mocker.patch("ask_confluence.model_predictor.openai.File.delete")
        answer_create_mocker = mocker.patch("ask_confluence.model_predictor.openai.Answer.create")

        ModelPredictor().get_answer("Is this a test?")
        file_create_mocker.assert_called_once()
        file_delete_mocker.assert_called_once()
        answer_create_mocker.call_args[1]["file"] == mock_file_id.get("id")
