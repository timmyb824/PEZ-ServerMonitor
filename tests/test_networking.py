import netifaces
import pytest
from unittest.mock import patch
from src.networking import get_network_info, get_network_activity, print_network_info

def test_get_network_info():
    with patch('netifaces.interfaces') as mock_interfaces:
        mock_interfaces.return_value = ['lo', 'eth0']

        with patch('netifaces.ifaddresses') as mock_ifaddresses:
            mock_ifaddresses.return_value = {netifaces.AF_INET: [{'addr': '192.168.1.1'}]}

            with patch('urllib.request.urlopen') as mock_urlopen:
                mock_urlopen.return_value.read.return_value.decode.return_value.strip.return_value = '8.8.8.8'

                ip_lan_dict, ip_wan = get_network_info()
                assert ip_lan_dict == {'eth0': '192.168.1.1'}
                assert ip_wan == ("WAN", '8.8.8.8')

def test_get_network_activity():
    with patch('psutil.net_io_counters') as mock_io_counters:
        mock_io_counters.return_value = {
            'eth0': type('', (), {'bytes_sent': 2048, 'bytes_recv': 1024}),
        }

        result = get_network_activity()
        assert result == {
            'eth0': {
                'bytes_sent': 2048,
                'bytes_recv': 1024,
            },
        }

# @patch('networking.get_network_info')
# @patch('networking.get_network_activity')
# @patch('tabulate.tabulate')
# def test_print_network_info(mock_tabulate, mock_get_network_activity, mock_get_network_info):
#     mock_get_network_info.return_value = (
#         {'eth0': '192.168.1.1'},
#         ("WAN", '8.8.8.8')
#     )
#     mock_get_network_activity.return_value = {
#         'eth0': {
#             'bytes_sent': 2048,
#             'bytes_recv': 1024,
#         },
#     }

#     print_network_info()

#     mock_tabulate.assert_called_once_with(
#         [['WAN', '8.8.8.8', '-', '-'], ['eth0', '192.168.1.1', 0.0, 0.0]],
#         headers=["Interface", "IP", "MB Sent", "MB Received"],
#         tablefmt="simple_grid"
#     )
