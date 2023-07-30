# original working version
# import yaml

# def parse_config_file(yaml_file: str) -> dict|None:
#     """Parse the configuration file and return the content as a Python dictionary.

#     Args:
#         yaml_file (str): The path to the config yaml file.
#     """
#     try:
#         with open(yaml_file, 'r') as config_file:
#             config = yaml.safe_load(config_file)
#         return config
#     except FileNotFoundError:
#         print(f"Config file {yaml_file} not found.")
#         exit(1)
#     except yaml.YAMLError as exception:
#         print(f"Error parsing config file: {exception}")
#         exit(1)
#     except Exception as exception:
#         print(f"Unexpected error: {exception}")

#########

## move exception handling to classes
# import yaml

# # in config_parser.py
# class FileNotFoundError(Exception):
#     pass

# class YamlError(Exception):
#     pass

# def parse_config_file(file_path: str) -> dict|None:
#     """Parse the configuration file and return the content as a Python dictionary.

#     Args:
#         yaml_file (str): The path to the config yaml file.
#     """
#     try:
#         with open(file_path, 'r') as config_file:
#             config = yaml.safe_load(config_file)
#         return config
#     except FileNotFoundError:
#         raise FileNotFoundError(f"Config file {file_path} not found.")
#     except yaml.YAMLError as exception:
#         raise YamlError(f"Error parsing config file: {exception}")
#     except Exception as exception:
#         print(f"Unexpected error: {exception}")
#         raise

#########

# move exception handling to classes version 2
import yaml
from exceptions import ConfigFileNotFoundException, YAMLParseError, UnexpectedError

def parse_config_file(yaml_file: str) -> dict|None:
    """Parse the configuration file and return the content as a Python dictionary.

    Args:
        yaml_file (str): The path to the config yaml file.

    Raises:
        ConfigFileNotFoundException: If the config file is not found.
        YAMLParseError: If there is an error parsing the YAML file.
        UnexpectedError: If any other unexpected error occurs.
    """
    try:
        with open(yaml_file, 'r') as config_file:
            config = yaml.safe_load(config_file)
        return config
    except FileNotFoundError as exception:
        raise ConfigFileNotFoundException(f"Config file {yaml_file} not found.") from exception
    except yaml.YAMLError as exception:
        raise YAMLParseError(f"Error parsing config file: {exception}") from exception
    except Exception as exception:
        raise UnexpectedError(f"Unexpected error: {exception}") from exception
