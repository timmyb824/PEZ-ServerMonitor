from tabulate import tabulate
from utils import print_title

# Memory
def get_memory_info() -> tuple[int, int, float, int, int, float]:
    mem_info = {
        i.split()[0].rstrip(':'): int(i.split()[1])
        for i in open('/proc/meminfo').readlines()
    }
    mem_total = mem_info['MemTotal'] // 1024
    mem_free = (mem_info['MemFree'] + mem_info['Buffers'] + mem_info['Cached']) // 1024
    mem_used_percentage = ((mem_total - mem_free) / mem_total) * 100
    swap_total = mem_info['SwapTotal'] // 1024
    swap_free = mem_info['SwapFree'] // 1024
    swap_used_percentage = ((swap_total - swap_free) / swap_total) * 100
    return mem_total, mem_free, mem_used_percentage, swap_total, swap_free, swap_used_percentage

def print_memory_info():
    # Memory
    mem_total, mem_free, mem_used_percentage, swap_total, swap_free, swap_used_percentage = get_memory_info()

    table = [
        ['Memory', f'{mem_free}MB', f'{mem_total}MB', f'{mem_used_percentage:.2f}%'],
        ['Swap', f'{swap_free}MB', f'{swap_total}MB', f'{swap_used_percentage:.2f}%'],
    ]

    headers = ["Type", "Free", "Total", "Usage"]

    print_title("Memory Information")
    print(tabulate(table, headers, tablefmt="simple_grid"))
