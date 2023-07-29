import yaml

def parse_config_file(yaml_file: str) -> dict|None:
    """Parse the configuration file and return the content as a Python dictionary.

    Args:
        yaml_file (str): The path to the config yaml file.
    """
    try:
        with open(yaml_file, 'r') as config_file:
            config = yaml.safe_load(config_file)
        return config
    except FileNotFoundError:
        print(f"Config file {yaml_file} not found.")
        exit(1)
    except yaml.YAMLError as exception:
        print(f"Error parsing config file: {exception}")
        exit(1)
    except Exception as exception:
        print(f"Unexpected error: {exception}")

