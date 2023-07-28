import argparse
from cpu_info import print_cpu_info
from disk_info import print_disk_info
from mem_info import print_memory_info
from network_info import print_network_info
from latency_info import print_latency_info
from process_info import print_process_info
from system_info import print_system_info
from container_info import print_running_containers

def parse_args():
    parser = argparse.ArgumentParser(description='System information tool.')
    parser.add_argument('-a', '--all', action='store_true', help='Show all information')
    parser.add_argument('-s', '--system', action='store_true', help='Show only system information')
    parser.add_argument('-c', '--cpu', action='store_true', help='Show only CPU information')
    parser.add_argument('-m', '--memory', action='store_true', help='Show only memory information')
    parser.add_argument('-d', '--disk', action='store_true', help='Show only disk information')
    parser.add_argument('-n', '--network', action='store_true', help='Show only network and latency information')
    parser.add_argument('-ps', '--processes', action='store_true', help='Show only services information')
    parser.add_argument('-dp', '--containers', action='store_true', help='Show only container (docker or podman) information')
    return parser.parse_args()

def main(args) -> None:
    # All information
    if args.all:
        print_all_info()
    elif args.system:
        print_system_info()
    elif args.cpu:
        print_cpu_info()
    elif args.memory:
        print_memory_info()
    elif args.disk:
        print_disk_info()
    elif args.network:
        print_network_info()
        print_latency_info()
    elif args.processes:
        print_process_info()
    elif args.containers:
        print_running_containers()
    else:
        print("No arguments given. Use -h or --help for help.")

def print_all_info():
    print_system_info()
    print_cpu_info()
    print_memory_info()
    print_disk_info()
    print_network_info()
    print_latency_info()
    print_process_info()
    print_running_containers()

if __name__ == '__main__':
    args = parse_args()
    main(args)
