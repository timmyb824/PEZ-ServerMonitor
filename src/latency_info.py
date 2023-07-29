import math
from tabulate import tabulate
from ping3 import ping, verbose_ping
from utils import print_title, print_bold_kv
from config_parser import parse_config_file
from concurrent.futures import ThreadPoolExecutor, as_completed

def check_ping(host: str) -> str:
    """
    Checks the latency of the host.

    Args:
        host (str): Host to be pinged.

    Returns:
        str: The latency result.
    """
    try:
        latency = ping(host)  # ping returns delay in seconds, None if timed out
        if latency is None:
            return 'Timed Out'
        latency *= 1000  # Convert seconds to milliseconds
        return round(latency, 2)
    except Exception as e:
        return f"Error: {e}"

def calculate_average_latency(ping_results: list) -> float:
    """
    Calculates the average latency from a list of results.

    Args:
        ping_results (list): List of ping results.

    Returns:
        float: The average latency.
    """
    count = len(ping_results)

    total_latency = sum(
        float(delay.replace(" ms", ""))
        for host, delay in ping_results
        if delay != "Timed Out"
    )
    avg_latency = total_latency / count if count != 0 else float('NaN')
    return round(avg_latency, 2)

def print_latency_info(config_file: str) -> None:
    """
    Prints latency information.

    Args:
    config_file (str): The path to the config file.
    """
    try:
        # Ping
        config = parse_config_file(config_file)
        ping_hosts = config['ping_hosts']

        ping_results = []
        with ThreadPoolExecutor(max_workers=len(ping_hosts)) as executor:
            future_to_host = {executor.submit(check_ping, host): host for host in ping_hosts}
            for future in as_completed(future_to_host):
                host = future_to_host[future]
                try:
                    ping_time = future.result()
                except Exception as exc:
                    print('%r generated an exception: %s' % (host, exc))
                else:
                    if ping_time != "Timed Out":
                        ping_results.append([host, f"{ping_time} ms"])
                    else:
                        ping_results.append([host, ping_time])

        average_latency = calculate_average_latency(ping_results)

        print_title("Latency Information")
        print_bold_kv("Average Round-Trip Delay", f"{'N/A' if math.isnan(average_latency) else average_latency} ms")
        print(tabulate(ping_results, headers=["Host", "Round-Trip Delay"], tablefmt="simple_grid"))
    except FileNotFoundError:
        print("Error: config yaml not found.")
