import socket
from unittest.mock import patch

import pytest

from src.services import check_a_service, get_process_count, print_process_info


def test_check_a_service():
    # Test for service up
    with patch("socket.socket") as mock_socket:
        instance = mock_socket.return_value
        instance.connect_ex.return_value = 0
        assert check_a_service(80, "localhost")

        # Test for service down
        instance.connect_ex.return_value = 1
        assert not check_a_service(80, "localhost")

        # Test for invalid host
        instance.connect_ex.side_effect = socket.gaierror("Error")
        assert not check_a_service(80, "invalid")


def test_get_process_count():
    with patch("psutil.pids") as mock_pids:
        mock_pids.return_value = [1, 2, 3, 4, 5]
        assert get_process_count() == 5


# @patch('services.print_title')
# @patch('services.parse_config_file')
# @patch('services.check_a_service')
# @patch('tabulate.tabulate')
# def test_print_process_info(mock_tabulate, mock_check_a_service, mock_parse_config_file, mock_print_title):
#     mock_parse_config_file.return_value = {
#         'services': [
#             {'name': 'service1', 'port': 80, 'host': 'localhost'},
#             {'name': 'service2', 'port': 81, 'host': 'localhost'},
#         ],
#     }
#     mock_check_a_service.side_effect = [True, False]
#     print_process_info('config.yaml')
#     mock_print_title.assert_called_once_with('Services Information')
#     mock_tabulate.assert_called_once_with(
#         [
#             ['service1', 80, '\x1b[92mUp\x1b[0m'],
#             ['service2', 81, '\x1b[91mDown\x1b[0m'],
#         ],
#         ["Service Name", "Port", "Status"],
#         tablefmt="simple_grid"
#     )
