import yaml
from constants import ROOT_DIR

file_path = f"{ROOT_DIR}/config.yaml"

def parse_config_file(file_path: str) -> dict|None:
    """Parse the configuration file and return the content as a Python dictionary."""
    try:
        with open(file_path, 'r') as config_file:
            config = yaml.safe_load(config_file)
        return config
    except FileNotFoundError:
        print(f"Config file {file_path} not found.")
        exit(1)
    except yaml.YAMLError as exception:
        print(f"Error parsing config file: {exception}")
        exit(1)
    except Exception as exception:
        print(f"Unexpected error: {exception}")

