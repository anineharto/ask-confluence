from ask_confluence.confluence_downloader import ConfluenceDownloader
from ask_confluence.data_transformer import DataTransformer
from ask_confluence.model_predictor import ModelPredictor

def data_pipeline():
    """Run full pipeline to download data from confluence, transform, and get prediction."""
    ConfluenceDownloader().download_content_to_raw()
    DataTransformer().json_merge_to_jsonl()

def predict_pipeline():
    """Get prediction from previously downloaded and transformed data."""
    question = input("Please enter a question: ")
    answer = ModelPredictor().get_answer(question)
    print(answer)

if __name__ == "__main__":
    data_pipeline()
    predict_pipeline()
