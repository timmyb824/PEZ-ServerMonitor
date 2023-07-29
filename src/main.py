import argparse
from cpu_info import print_cpu_info
from disk_info import print_disk_info
from mem_info import print_memory_info
from network_info import print_network_info
from latency_info import print_latency_info
from services_info import print_process_info
from system_info import print_system_info
from container_info import print_running_containers
from processes_info import print_memory_usage_info, print_cpu_usage_info
from constants import ROOT_DIR

def parse_args():
    """
    Parses command-line arguments.

    Returns:
        Namespace: Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(description='System information tool.')
    parser.add_argument('-a', '--all', action='store_true', help='Show all information')
    parser.add_argument('-s', '--system', action='store_true', help='Show only system information')
    parser.add_argument('-c', '--cpu', action='store_true', help='Show only CPU information')
    parser.add_argument('-m', '--memory', action='store_true', help='Show only memory information')
    parser.add_argument('-d', '--disk', action='store_true', help='Show only disk information')
    parser.add_argument('-n', '--network', action='store_true', help='Show only network and latency information')
    parser.add_argument('-ps', '--processes', action='store_true', help='Show only services information')
    parser.add_argument('-dp', '--containers', action='store_true', help='Show only container (docker or podman) information')
    parser.add_argument('-cf', '--config', default=f"{ROOT_DIR}/config.yaml", help='The path to the config file')

    return parser.parse_args()

def main(args) -> None:
    """
    Main function which triggers based on the arguments provided.

    Args:
        args (Namespace): Parsed command-line arguments.
    """
    try:

        # Parse config file (default config is used if no config file is provided)
        config_file = args.config

        # All information
        if args.all:
            print_all_info(config_file)
        elif args.system:
            print_system_info()
        elif args.cpu:
            print_cpu_info()
            print_cpu_usage_info()
        elif args.memory:
            print_memory_info()
            print_memory_usage_info()
        elif args.disk:
            print_disk_info()
        elif args.network:
            print_network_info()
            print_latency_info(config_file)
        elif args.processes:
            print_process_info(config_file)
        elif args.containers:
            print_running_containers()
        else:
            print("No arguments given. Use -h or --help for help.")
    except Exception as exception:
        print(f"An error occurred: {exception}")

def print_all_info(config_file: str):
    """
    Prints all system-related information.

    Args:
        config_file (str): The path to the config file.
    """
    print_system_info()
    print_cpu_info()
    print_cpu_usage_info()
    print_memory_info()
    print_memory_usage_info()
    print_disk_info()
    print_network_info()
    print_latency_info(config_file)
    print_process_info(config_file)
    print_running_containers()

if __name__ == '__main__':
    args = parse_args()
    main(args)
