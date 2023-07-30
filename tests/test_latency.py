import pytest
import math
from unittest.mock import patch
from src.latency import check_ping, calculate_average_latency, perform_ping, print_latency_info  # replace 'src.latency' with actual module name

def test_check_ping():
    with patch('src.latency.ping', return_value=0.002):
        assert check_ping('localhost') == 2  # 0.002 seconds = 2 milliseconds

    with patch('src.latency.ping', return_value=None):
        assert check_ping('localhost') == 'Timed Out'

def test_calculate_average_latency():
    # Test when there are no "Timed Out" pings
    ping_results = [['host1', '10 ms'], ['host2', '20 ms'], ['host3', '30 ms']]
    assert calculate_average_latency(ping_results) == 20

    # Test when there are "Timed Out" pings
    ping_results = [['host1', 'Timed Out'], ['host2', '20 ms'], ['host3', '30 ms']]
    assert calculate_average_latency(ping_results) == 25

    # Test when all pings are "Timed Out"
    ping_results = [['host1', 'Timed Out'], ['host2', 'Timed Out'], ['host3', 'Timed Out']]
    assert math.isnan(calculate_average_latency(ping_results))

# This test can fail at random because the order of the results is not guaranteed when using ThreadPoolExecutor
# def test_perform_ping(mocker):
#     mock_check_ping = mocker.patch('src.latency.check_ping', side_effect=[1, 'Timed Out', 2])
#     ping_hosts = ['host1', 'host2', 'host3']
#     # assert perform_ping(ping_hosts) == [['host1', '1 ms'], ['host2', 'Timed Out'], ['host3', '2 ms']]
#     assert perform_ping(ping_hosts) == [['host3', '2 ms'], ['host1', '1 ms'], ['host2', 'Timed Out']]
#     assert mock_check_ping.call_count == 3

def test_perform_ping(mocker):
    mock_check_ping = mocker.patch('src.latency.check_ping', side_effect=[1, 'Timed Out', 2])
    ping_hosts = ['host1', 'host2', 'host3']
    expected_results = {('host1', '1 ms'), ('host2', 'Timed Out'), ('host3', '2 ms')}
    assert {tuple(x) for x in perform_ping(ping_hosts)} == expected_results
    assert mock_check_ping.call_count == 3

@patch('src.latency.parse_config_file')
@patch('src.latency.perform_ping')
@patch('src.latency.calculate_average_latency')
def test_print_latency_info(mock_calculate_average_latency, mock_perform_ping, mock_parse_config_file, capsys):
    # Mocking parse_config_file function to return some configuration
    mock_parse_config_file.return_value = {
        'ping_hosts': ['host1', 'host2', 'host3']
    }
    # Mocking perform_ping function to return some ping results
    mock_perform_ping.return_value = [['host1', '1 ms'], ['host2', 'Timed Out'], ['host3', '2 ms']]
    # Mocking calculate_average_latency function to return an average latency
    mock_calculate_average_latency.return_value = 1.5

    # Call the function to test
    print_latency_info('path/to/config_file.yaml')

    # Get the output sent to stdout
    captured = capsys.readouterr()
    assert 'Average Round-Trip Delay' in captured.out
    assert '1.5 ms' in captured.out
