import json
from tqdm import tqdm
import jsonlines
from pathlib import Path
import data.raw as raw_data_path
import data.interim as interim_data_path

class DataTransformer:
    """DataTransformer module definition."""

    def __init__(self):
        """DataTransformer init module."""
        self.raw_data_path = Path(raw_data_path.__file__).parent
        self.interim_data_file_path = Path(interim_data_path.__file__).parent / "confluence_pages.jsonl"

    def json_merge_to_jsonl(self):
        """Merge all json files in data/raw to one jsonline file in data/interim."""
        raw_data_file_paths = [file for file in self.raw_data_path.iterdir() if file.suffix == ".json"]
        with jsonlines.open(self.interim_data_file_path, "a") as outfile:
            for raw_data_file_path in tqdm(raw_data_file_paths, desc="Merging JSON files"):
                entry = json.load(open(raw_data_file_path))
                outfile.write(entry)
