from ask_confluence.confluence_downloader import ConfluenceDownloader
from ask_confluence.data_transformer import DataTransformer
from ask_confluence.model_trainer import ModelTrainer

if __name__ == "__main__":
    ConfluenceDownloader().download_content_to_raw()
    DataTransformer().json_merge_to_jsonl()
    answer = ModelTrainer().get_answer("Who is the client?")
    print(answer)
