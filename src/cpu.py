import os
import psutil
import platform
from typing import Union
from utils import print_title, print_bold_kv

def get_cpu_info() -> tuple[int, str, Union[str, int], str, str]:
    """
    Gets CPU information.

    Returns:
    tuple: A tuple containing the number of CPUs, CPU info, frequency, cache size, and bogomips.
    """
    try:
        with open('/proc/cpuinfo') as f:
            cpuinfo = f.readlines()

        cpu_nb = len([line for line in cpuinfo if line.startswith('processor')])
        cpu_info = next(line.split(': ')[1].strip() for line in cpuinfo if line.startswith('model name'))
        cpu_freq = next((line.split(': ')[1].strip() for line in cpuinfo if line.startswith('cpu MHz')), None)

        if cpu_freq is None:
            with open('/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq', "r", encoding="UTF-8") as f:
                cpu_freq = int(f.read().strip()) // 1000

        cpu_cache = next(line.split(': ')[1].strip() for line in cpuinfo if line.startswith('cache size'))
        cpu_bogomips = next(line.split(': ')[1].strip() for line in cpuinfo if line.startswith('bogomips'))

        return cpu_nb, cpu_info, cpu_freq, cpu_cache, cpu_bogomips
    except IOError as exception:
        print(f"Error reading CPU info: {exception}")
        return 0, 'UNKNOWN', '0', 'UNKNOWN', 'UNKNOWN'


def get_cpu_usage() -> float:
    """
    Gets the current CPU usage.

    Returns:
    float: The CPU usage percentage.
    """
    try:
        return psutil.cpu_percent()
    except psutil.Error as exception:
        print(f"Error reading CPU usage: {exception}")
        return 0.0

def get_load_average() -> tuple[float, float, float]:
    """
    Gets the system's load average.

    Returns:
    tuple: A tuple containing the 1, 5, and 15 minute load averages.
    """
    return os.getloadavg()

def get_process_count() -> int:
    """
    Gets the number of running processes.

    Returns:
    int: The number of running processes.
    """
    try:
        return len(psutil.pids())
    except psutil.Error as exception:
        print(f"Error reading process count: {exception}")
        return 0

def get_system_temperature() -> tuple[str, bool]:
    """
    Gets the system's CPU temperature.

    Returns:
    tuple: A tuple containing the CPU temperature and a boolean indicating whether the temperature could be fetched.
    """
    os_type = platform.system()
    if os_type != 'Linux':
        return f"Temperature check only supported on Linux. Current OS: {os_type}", False

    try:
        temps = psutil.sensors_temperatures()
        if 'coretemp' in temps:
            cputemp = temps['coretemp']
            for item in cputemp:
                if item.label == 'Package id 0':
                    return f"{item.current}°C", True
        return "Unable to get system temperature.", False
    except psutil.Error as exception:
        print(f"Error reading system temperature: {exception}")
        return "Unable to get system temperature.", False


def print_cpu_info() -> None:
    """
    Prints the CPU information, CPU usage, load average, and system temperature.
    """
    cpu_nb, cpu_info, cpu_freq, cpu_cache, cpu_bogomips = get_cpu_info()
    print_title('CPU Information')
    print_bold_kv('Number', str(cpu_nb))
    print_bold_kv('Model', cpu_info)
    print_bold_kv("Frequency", f"{cpu_freq} MHz")
    print_bold_kv("Cache L2", cpu_cache)
    print_bold_kv("Bogomips", cpu_bogomips)
    print_bold_kv("CPU Usage", f"{get_cpu_usage()}%")

    cpu_temp, _ = get_system_temperature() # replaced status with _
    print_bold_kv("CPU Temperature", cpu_temp)

    process_count = get_process_count()
    print_bold_kv("Process Count", f"{process_count}")

    load_1, load_5, load_15 = get_load_average()
    print_bold_kv("Load average (1m)", f"{round(load_1, 2)}")
    print_bold_kv("Load average (5m)", f"{round(load_5, 2)}")
    print_bold_kv("Load average (15m)", f"{round(load_15, 2)}")
