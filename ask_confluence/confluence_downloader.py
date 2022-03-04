from atlassian import Confluence
import requests
from ask_confluence.config import Config
import data.raw as raw_data_path
from pathlib import Path
import re
import json
from tqdm import tqdm

class ConfluenceDownloader:
    """ConfluenceDownloader class definition."""

    def __init__(self):
        """Init ConfluenceDownloader module."""
        self.__config = Config()
        self.confluence = Confluence(url=self.__config.parameters["url"], session=self._get_session())
        self.raw_data_path = Path(raw_data_path.__file__).parent
    
    def _get_session(self):
        """Get session object for Confluence request.

        How to generate token: https://developer.atlassian.com/cloud/confluence/basic-auth-for-rest-apis/#supplying-basic-auth-headers

        Returns:
            request.Session: Session object with default authorization.
        """
        session = requests.Session()
        session.headers['Authorization'] = f'Basic {self.__config.parameters["token"]}'
        return session
    
    def _get_page_ids_in_space(self):
        """Get all Confluence page IDs that exist in Confluence space set in config.

        Returns:
            list(str): List of all page IDs.
        """
        pages = self.confluence.get_all_pages_from_space(self.__config.parameters["space"])
        return [page.get("id") for page in pages]
    
    def _get_content_by_id(self, page_id):
        """Get all content from a given Confluence page ID.

        Args:
            page_id (str): ID of Confluence page.

        Returns:
            str: All content in given Confluence page ID.
        """
        content = self.confluence.get_page_by_id(page_id=page_id, expand='body.storage').get('body').get('storage').get('value')
        content_without_symbols = re.sub('<[^<]+?>', ' ', content)
        return content_without_symbols
    
    def download_content_to_raw(self):
        """Download content from all pages in Confluence space given from config to data/raw."""
        page_ids = self._get_page_ids_in_space()
        for page_id in tqdm(page_ids, desc="Downloading Confluence pages"):
            raw_data_file_path = self.raw_data_path.joinpath(page_id + ".json")
            content = {"text": self._get_content_by_id(page_id=page_id)}
            with open(raw_data_file_path, "w", encoding="utf-8") as outfile:
                    json.dump(content, outfile)
