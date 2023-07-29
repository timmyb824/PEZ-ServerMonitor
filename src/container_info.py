import subprocess
import re
from tabulate import tabulate
from typing import Optional
from utils import print_title

def check_if_installed(command: str) -> bool:
    """
    Checks if a command (docker or podman) is installed on the system.

    Parameters:
    command (str): The command to check.

    Returns:
    bool: True if the command is installed, False otherwise.
    """
    try:
        subprocess.run([command, '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False
    except subprocess.CalledProcessError as e:
        print(f"Error running {command}: {str(e)}")
        return False
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return False

# For checking docker or podman
def check_docker_or_podman() -> Optional[str]:
    """
    Checks if Docker or Podman is installed on the system.

    Returns:
    str: "docker" if Docker is installed, "podman" if Podman is installed.
    None: If neither Docker nor Podman is installed.
    """
    if check_if_installed('docker'):
        return 'docker'
    elif check_if_installed('podman'):
        return 'podman'
    else:
        print("Neither Docker nor Podman is installed on your system.")
        return None

def get_running_containers(command: str) -> Optional[list[list[str]]]:
    """
    Retrieves a list of running containers.

    Parameters:
    command (str): The command to retrieve the containers (either Docker or Podman).

    Returns:
    List[List[str]]: A list of running containers, each represented as a list of attributes.
    None: If an error occurred while retrieving the containers.
    """
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
    except subprocess.CalledProcessError as exception:
        print(f"Error running {command} ps: {str(exception)}")
        return None
    except Exception as exception:
        print(f"Unexpected error: {str(exception)}")
        return None


def print_running_containers() -> None:
    """
    Prints the running Docker or Podman containers on the system.
    """
    if container_tool := check_docker_or_podman():
        containers = get_running_containers(container_tool)
        if containers is not None:
            print_title("Containers Information")
            print(f"{container_tool.capitalize()} containers running on your system:")
            print(tabulate(containers, headers=["ID", "Names", "PortMappings", "Status"], tablefmt="simple_grid"))
        else:
            print("Error retrieving running containers.")
