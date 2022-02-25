from ask_confluence.confluence_downloader import ConfluenceDownloader
from ask_confluence.data_transformer import DataTransformer
from ask_confluence.model_predictor import ModelPredictor

if __name__ == "__main__":
    ConfluenceDownloader().download_content_to_raw()
    DataTransformer().json_merge_to_jsonl()
    question = input("Please enter a question: ")
    answer = ModelPredictor().get_answer(question)
    print(answer)
