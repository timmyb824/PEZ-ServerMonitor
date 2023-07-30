import pytest
from unittest.mock import patch, mock_open
from src.memory import calculate_memory_usage, get_memory_info, print_memory_info

def test_calculate_memory_usage():
    total, free, used_percentage = calculate_memory_usage(1024, 512, 256, 256)
    assert total == 1
    assert free == 1
    assert used_percentage == 0

    total, free, used_percentage = calculate_memory_usage(2048, 1024, 512, 256)
    assert total == 2
    assert free == 1
    assert used_percentage == 50.0

@patch('builtins.open', new_callable=mock_open, read_data='MemTotal: 8192 kB\nMemFree: 2048 kB\nBuffers: 1024 kB\nCached: 1024 kB\nSwapTotal: 8192 kB\nSwapFree: 4096 kB\n')
def test_get_memory_info(mock_file):
    mem_total, mem_free, mem_used_percentage, swap_total, swap_free, swap_used_percentage = get_memory_info()
    assert mem_total == 8
    assert mem_free == 4
    assert mem_used_percentage == 50
    assert swap_total == 8
    assert swap_free == 4
    assert swap_used_percentage == 50

@patch('builtins.open', new_callable=mock_open, read_data='MemTotal: 8192 kB\nMemFree: 2048 kB\n')
def test_get_memory_info_missing_keys(mock_file):
    mem_total, mem_free, mem_used_percentage, swap_total, swap_free, swap_used_percentage = get_memory_info()
    assert mem_total == 0
    assert mem_free == 0
    assert mem_used_percentage == 0
    assert swap_total == 0
    assert swap_free == 0
    assert swap_used_percentage == 0

# @patch('memory.get_memory_info')
# @patch('utils.print_title')
# @patch('tabulate.tabulate')
# def test_print_memory_info(mock_tabulate, mock_print_title, mock_get_memory_info):
#     mock_get_memory_info.return_value = (8192, 2048, 75, 4096, 1024, 75)
#     print_memory_info()
#     mock_print_title.assert_called_once_with("Memory Information")
#     mock_tabulate.assert_called_once_with([
#         ['Memory', '2048MB', '8192MB', '75.00%'],
#         ['Swap', '1024MB', '4096MB', '75.00%'],
#     ], ['Type', 'Free', 'Total', 'Usage'], tablefmt="simple_grid")
