from pathlib import Path
import time
import openai
from ask_confluence.config import Config
import data.interim as interim_data_path

class ModelTrainer:
    # ModelTrainer takes all confluence pages located in /data directory
    # and feeds them into the openai model.

    def __init__(self):
        self.__config = Config()
        self.interim_data_file_path = Path(interim_data_path.__file__).parent / "confluence_pages.jsonl"
    
    def _upload_file(self):
        file_id = openai.File.create(file=open(self.interim_data_file_path), purpose="answers").get("id")
        time.sleep(5) # Issue with OpenAI returning file id before the processing is complete
        return file_id
    
    def _delete_file(self, file_id):
        openai.File.delete(file_id)
    
    def get_answer(self, question):
        openai.api_key = self.__config.parameters["openai_api_key"]
        file_id = self._upload_file()
        answer = openai.Answer.create(
            search_model="ada",
            model="curie",
            question=question,
            file=file_id,
            examples_context=self.__config.parameters["examples_context"],
            examples=self.__config.parameters["examples"],
            max_tokens=5,
        ).get("answers")
        self._delete_file(file_id=file_id)
        return answer
