import subprocess
import psutil
from tabulate import tabulate
from utils import print_title

# Disk space
# def get_disk_space() -> str:
#     return subprocess.run(['df', '-h'], capture_output=True, text=True, check=False).stdout

# def print_disk_info() -> None:
#     # Disk space
#     print_title('Disk Information')
#     print(get_disk_space())

def get_disk_space():
    partitions = psutil.disk_partitions()
    disk_space_info = []
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        disk_space_info.append({
            'device': partition.device,
            'mountpoint': partition.mountpoint,
            'total': usage.total / (1024**3),  # convert bytes to GB
            'used': usage.used / (1024**3),  # convert bytes to GB
            'free': usage.free / (1024**3),  # convert bytes to GB
            'percentage': usage.percent,
        })
    return disk_space_info

def print_disk_info():
    print_title('Disk Information')
    disk_space_info = get_disk_space()

    # Filter out any entries where the mountpoint starts with '/snap' or '/var/snap'
    filtered_disk_space_info = [info for info in disk_space_info if not (info['mountpoint'].startswith('/snap') or info['mountpoint'].startswith('/var/snap'))]

    # Prepare the data for tabulate
    table = [(info['device'], info['mountpoint'], f"{info['total']:.2f} GB", f"{info['used']:.2f} GB", f"{info['free']:.2f} GB", f"{info['percentage']:.2f} %") for info in filtered_disk_space_info]

    print(tabulate(table, headers=['Device', 'Mountpoint', 'Total', 'Used', 'Free', 'Percentage'], tablefmt='simple_grid'))