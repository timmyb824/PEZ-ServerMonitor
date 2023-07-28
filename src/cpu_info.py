import os
import psutil
from utils import print_title, print_bold_kv

# CPU
def get_cpu_info() -> tuple[int, str, str|int, str, str]:
    with open('/proc/cpuinfo') as f:
        cpuinfo = f.readlines()

    cpu_nb = len([line for line in cpuinfo if line.startswith('processor')])
    cpu_info = [line.split(': ')[1].strip() for line in cpuinfo if line.startswith('model name')][0]
    cpu_freq = [line.split(': ')[1].strip() for line in cpuinfo if line.startswith('cpu MHz')][0]

    if not cpu_freq:
        with open('/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq', "r", encoding="UTF-8") as f:
            cpu_freq = int(f.read().strip()) // 1000

    cpu_cache = [line.split(': ')[1].strip() for line in cpuinfo if line.startswith('cache size')][0]
    cpu_bogomips = [line.split(': ')[1].strip() for line in cpuinfo if line.startswith('bogomips')][0]
    return cpu_nb, cpu_info, cpu_freq, cpu_cache, cpu_bogomips

def get_cpu_usage() -> float:
    # Get the current CPU usage
    return psutil.cpu_percent()

# Load Average
def get_load_average() -> tuple[float, float, float]:
    return os.getloadavg()

def get_process_count() -> int:
    # Get the list of all process IDs currently running on the system
    all_processes = psutil.pids()

    # Return the count of running processes
    return len(all_processes)

def get_system_temperature() -> str:
    if not (temps := psutil.sensors_temperatures()):
        return "Unable to get system temperature."
    if 'coretemp' in temps:  # 'coretemp' for Linux
        cputemp = temps['coretemp']
        for item in cputemp:
            if item.label == 'Package id 0':  # get the first CPU package temp
                return f"{item.current}{chr(176)}C"

def print_cpu_info() -> None:
    # CPU
    cpu_nb, cpu_info, cpu_freq, cpu_cache, cpu_bogomips = get_cpu_info()
    print_title('CPU Information')
    print_bold_kv('Number', str(cpu_nb))
    print_bold_kv('Model', cpu_info)
    print_bold_kv("Frequency", f"{cpu_freq} MHz")
    print_bold_kv("Cache L2", cpu_cache)
    print_bold_kv("Bogomips", cpu_bogomips)

    # CPU Usage
    print_bold_kv("CPU Usage", f"{get_cpu_usage()}%")

    cpu_temp = get_system_temperature()
    print_bold_kv("CPU Temperature", cpu_temp)

    process_count = get_process_count()
    print_bold_kv("Process Count", f"{process_count}")

    # Load Average
    load_1, load_5, load_15 = get_load_average()
    print_bold_kv("Load average (1m)", f"{round(load_1, 2)}")
    print_bold_kv("Load average (5m)", f"{round(load_5, 2)}")
    print_bold_kv("Load average (15m)", f"{round(load_15, 2)}")