import yaml
from constants import ROOT_DIR

file_path = f"{ROOT_DIR}/config.yaml"

def parse_config_file(file_path: str) -> dict:
    """Parse the configuration file and return the content as a Python dictionary."""
    with open(file_path, 'r') as config_file:
        config = yaml.safe_load(config_file)
    return config
