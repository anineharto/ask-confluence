from ask_confluence.confluence_downloader import ConfluenceDownloader
from ask_confluence.config import Config
import data.raw as raw_data_path

class TestConfluenceDownloader:

    @staticmethod
    def test_download_content_to_raw(monkeypatch, mocker, mock_raw_data_file_path, mock_config_file_path):
        def get_mock_config_file_path(self):
            return [mock_config_file_path]
        monkeypatch.setattr(Config, "_get_config_file_paths", get_mock_config_file_path)
        monkeypatch.setattr(raw_data_path, "__file__", mock_raw_data_file_path)
        confluence_mocker = mocker.patch("ask_confluence.confluence_downloader.Confluence")
        session_mocker = mocker.patch("ask_confluence.confluence_downloader.requests.Session")
        page_ids_mocker = mocker.patch(
            "ask_confluence.confluence_downloader.Confluence.get_all_pages_from_space",
            return_value=[{"id": "1234"}]
        )
        page_id_content_mocker = mocker.patch(
            "ask_confluence.confluence_downloader.Confluence.get_page_by_id.get.get.get",
            return_value="test content"
            )
        
        confluence_mocker.return_value.get_all_pages_from_space = page_ids_mocker
        confluence_mocker.return_value.get_page_by_id.return_value.get.return_value.get.return_value.get = page_id_content_mocker
        
        ConfluenceDownloader().download_content_to_raw()
        confluence_mocker.assert_called_once()
        session_mocker.assert_called_once()
        page_ids_mocker.assert_called_once()
        page_id_content_mocker.assert_called_once()
