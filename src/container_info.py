import subprocess
import re
from tabulate import tabulate
from typing import Optional
from utils import print_title

def check_if_installed(command: str) -> bool:
    try:
        subprocess.run([command, '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        # print(f"{command} is not installed on your system.")
        return False
    except subprocess.CalledProcessError as e:
        if 'permission denied' in str(e).lower():
            print(f"You don't have sufficient permissions to run {command}. Please run this program as a superuser.")
        else:
            print(f"{command} encountered an error.")
        return False

# For checking docker or podman
def check_docker_or_podman() -> Optional[str]:
    if check_if_installed('docker'):
        return 'docker'
    elif check_if_installed('podman'):
        return 'podman'
    else:
        print("Neither Docker nor Podman is installed on your system.")
        return None

def get_running_containers(command: str):
    try:
        result = subprocess.run([command, 'ps', '--format', '{{.ID}}\t{{.Names}}\t{{.Ports}}\t{{.RunningFor}}'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Convert the output into a list of lists
        output = result.stdout.decode().splitlines()
        containers = []
        for line in output:
            split_line = re.split(r'\t|\s{2,}', line.strip())  # Split based on 2 or more spaces or a tab
            # Manually assemble the fields
            cid = split_line[0]
            names = split_line[1]
            if port_mappings := re.findall(r'(\d+)->(\d+)/tcp', split_line[2]):
                # Only consider the first port mapping
                source, target = port_mappings[0]
                ports = f'{source}:{target}'
            else:
                ports = 'N/A'
            # The status field should be the last item in the split_line list
            status = split_line[-1]
            # Append the fields as a list to the containers list
            containers.append([cid, names, ports, status])
        return containers
    except subprocess.CalledProcessError:
        return []


def print_running_containers():
    if container_tool := check_docker_or_podman():
        containers = get_running_containers(container_tool)
        print_title("Containers Information")
        print(f"{container_tool.capitalize()} containers running on your system:")
        print(tabulate(containers, headers=["ID", "Names", "PortMappings", "Status"], tablefmt="simple_grid"))

# if container_tool := check_docker_or_podman():
#     print_running_containers()
# else:
#     print("Unable to proceed without Docker or Podman.")