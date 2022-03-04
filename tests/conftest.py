import pytest
import json
import jsonlines
from pathlib import Path

@pytest.fixture(name="mock_config_file_path")
def fixture_mock_config_file_path(tmp_path):
    config = {
        "user": "test@user",
        "token": "test_token",
        "openai_api_key": "test_api_key",
        "url": "test.url.com",
        "space": "test_space",
        "examples": ["Is this a test?", "Yes"],
        "examples_context": "This is a test.",
    }
    config_file_path = tmp_path.joinpath("test_config.yml")
    with open(config_file_path, "w") as outfile:
        json.dump(config, outfile)
    
    return config_file_path

@pytest.fixture(name="mock_raw_data_file_path")
def fixture_mock_raw_data_file_path(tmp_path):
    content = "this is some raw test data"
    raw_data_file_path = tmp_path.joinpath("confluence_pages.json")
    with open(raw_data_file_path, "w") as outfile:
        json.dump(content, outfile)
    
    return raw_data_file_path

@pytest.fixture(name="mock_interim_data_file_path")
def fixture_mock_interim_data_file_path(tmp_path):
    content = "this is some interim test data"
    interim_data_file_path = tmp_path.joinpath("confluence_pages.jsonl")
    with jsonlines.open(interim_data_file_path, "w") as outfile:
        outfile.write(content)
    
    return interim_data_file_path