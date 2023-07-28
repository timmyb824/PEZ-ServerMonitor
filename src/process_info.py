import socket
from tabulate import tabulate
import psutil

# from constants import SERVICES_NAME, SERVICES_HOST
from utils import print_title
from config_parser import parse_config_file


# Services
def check_a_service(port: int, host: str) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))
    return result == 0

# def print_process_info() -> None:
#     # Services
#     print_title('Services Information')
#     for port, name in SERVICES_NAME.items():
#         # print(f"{name} (port {port}): {'Up' if check_a_service(port, SERVICES_HOST[port]) else 'Down'}")
#         print_bold_kv(name, f"{'Up' if check_a_service(port, SERVICES_HOST[port]) else 'Down'}")

# def print_process_info() -> None:
#     # Services
#     print_title('Services Information')

#     table = []
#     for port, name in SERVICES_NAME.items():
#         status = 'Up' if check_a_service(port, SERVICES_HOST[port]) else 'Down'
#         table.append([name, port, status])

#     headers = ["Service Name", "Port", "Status"]
#     print(tabulate(table, headers, tablefmt="simple_grid"))

def get_process_count():
    # Get the list of all process IDs currently running on the system
    all_processes = psutil.pids()

    # Return the count of running processes
    return len(all_processes)

def print_process_info() -> None:
    # Services
    print_title('Services Information')

    config = parse_config_file('config.yaml')
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