from unittest.mock import patch, Mock, call
from src.processes import get_processes, rearrange_order, print_memory_usage_info, print_cpu_usage_info

@patch('psutil.process_iter')
@patch('time.sleep')  # we patch sleep to avoid waiting during tests
def test_get_processes(mock_sleep, mock_process_iter):
    process = Mock()
    process.info = {'pid': 123, 'name': 'test', 'memory_percent': 1.5}
    process.cpu_percent.return_value = 0.5
    mock_process_iter.return_value = [process]

    top_memory, top_cpu = get_processes()

    # Verify the sleep was called to allow cpu_percent to update
    mock_sleep.assert_called_once_with(1)

    assert top_memory == top_cpu == [{'pid': 123, 'name': 'test', 'memory_percent': 1.5, 'cpu_percent': 0.5}]

def test_rearrange_order():
    input_data = [{'memory_percent': 1.5, 'cpu_percent': 0.5, 'pid': 123, 'name': 'test'}]
    expected_output = [{'pid': 123, 'name': 'test', 'cpu_percent': 0.5, 'memory_percent': 1.5}]
    assert rearrange_order(input_data) == expected_output

# @patch('processes.get_processes')
# @patch('processes.rearrange_order', side_effect=lambda x: x)  # just return the same value
# @patch('processes.bold', side_effect=lambda x: x)  # just return the same value
# @patch('tabulate.tabulate', return_value='table')
# def test_print_memory_usage_info(mock_tabulate, mock_bold, mock_rearrange_order, mock_get_processes):
#     processes = [{'pid': 123, 'name': 'test', 'memory_percent': 1.5, 'cpu_percent': 0.5}]
#     mock_get_processes.return_value = (processes, [])

#     with patch('builtins.print') as mock_print:
#         print_memory_usage_info()
#         mock_print.assert_has_calls([
#             call('\nTop 5 Processes by Memory Usage:'),
#             call('table'),
#         ])

#     mock_tabulate.assert_called_once_with(processes, headers='keys', tablefmt='simple_grid')

# @patch('processes.get_processes')
# @patch('processes.rearrange_order', side_effect=lambda x: x)  # just return the same value
# @patch('processes.bold', side_effect=lambda x: x)  # just return the same value
# @patch('tabulate.tabulate', return_value='table')
# def test_print_cpu_usage_info(mock_tabulate, mock_bold, mock_rearrange_order, mock_get_processes):
#     processes = [{'pid': 123, 'name': 'test', 'memory_percent': 1.5, 'cpu_percent': 0.5}]
#     mock_get_processes.return_value = ([], processes)

#     with patch('builtins.print') as mock_print:
#         print_cpu_usage_info()
#         mock_print.assert_has_calls([
#             call('\nTop 5 Processes by CPU Usage:'),
#             call('table'),
#         ])

#     mock_tabulate.assert_called_once_with(processes, headers='keys', tablefmt='simple_grid')
