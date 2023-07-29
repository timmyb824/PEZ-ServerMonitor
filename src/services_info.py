import socket
from tabulate import tabulate
import psutil
from utils import print_title
from config_parser import parse_config_file, ConfigFileNotFoundException, YAMLParseError, UnexpectedError

def check_a_service(port: int, host: str) -> bool:
    """
    Checks if a service running on a particular port of the host is up or down.

    Args:
        port (int): The port number of the service.
        host (str): The host on which the service is running.

    Returns:
        bool: True if the service is up, False otherwise.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        result = sock.connect_ex((host, port))
    except socket.gaierror as e:
        print(f"Invalid host/address {host}. Error: {e}")
        return False
    finally:
        sock.close()
    return result == 0

def get_process_count() -> int:
    """
    Gets the count of running processes in the system.

    Returns:
        int: The count of running processes in the system.
    """
    all_processes = psutil.pids()
    return len(all_processes)

def print_process_info(config_file: str) -> None:
    """
    Prints the information about all the services defined in the 'config.yaml' file.

    Args:
        config_file (str): The path to the config file.
    """
    print_title('Services Information')

    try:
        config = parse_config_file(config_file)
    except FileNotFoundError as exception:
        print("Error: config yaml not found.")
        return
    except ConfigFileNotFoundException as exception:
        print("Error: config yaml not found.")
        return
    except YAMLParseError:
        print("Error: Failed to parse config yaml.")
        return
    except UnexpectedError as exception:
        print(f"Unexpected error: {exception}")
        return


    services = config['services']

    table = []
    for service in services:
        name = service['name']
        port = service['port']
        host = service['host']
        status = 'Up' if check_a_service(port, host) else 'Down'
        colored_status = f"\033[92m{status}\033[0m" if status == 'Up' else f"\033[91m{status}\033[0m"
        table.append([name, port, colored_status])

    headers = ["Service Name", "Port", "Status"]
    print(tabulate(table, headers, tablefmt="simple_grid"))
