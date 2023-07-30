import psutil
import pytest
from unittest.mock import patch, mock_open, MagicMock
from src.cpu import get_cpu_info, get_cpu_usage, get_load_average, get_process_count, get_system_temperature, print_cpu_info

def test_get_cpu_info():
    cpu_info_text = '\n'.join([
        'processor   : 0',
        'model name  : Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz',
        'cpu MHz     : 2600.0000',
        'cache size  : 256 KB',
        'bogomips    : 5199.99',
        'processor   : 1',
        'model name  : Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz',
        'cpu MHz     : 2600.0000',
        'cache size  : 256 KB',
        'bogomips    : 5199.99',
    ])
    with patch('builtins.open', new_callable=mock_open, read_data=cpu_info_text) as mock_file:
        cpu_nb, cpu_info, cpu_freq, cpu_cache, cpu_bogomips = get_cpu_info()
        assert cpu_nb == 2  # this test assumes there are 2 processor entries in /proc/cpuinfo
        assert cpu_info == 'Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz'  # this should match the model name from /proc/cpuinfo
        assert cpu_freq == '2600.0000'  # this should match the MHz from /proc/cpuinfo
        assert cpu_cache == '256 KB'  # this should match the cache size from /proc/cpuinfo
        assert cpu_bogomips == '5199.99'  # this should match the bogomips from /proc/cpuinfo
        mock_file.assert_called_once_with('/proc/cpuinfo')


@patch('psutil.cpu_percent')
def test_get_cpu_usage(mock_cpu_percent):
    mock_cpu_percent.return_value = 20.0
    assert get_cpu_usage() == 20.0

@patch('os.getloadavg')
def test_get_load_average(mock_getloadavg):
    mock_getloadavg.return_value = (1.0, 5.0, 15.0)
    assert get_load_average() == (1.0, 5.0, 15.0)

@patch('psutil.pids')
def test_get_process_count(mock_pids):
    mock_pids.return_value = [1, 2, 3]
    assert get_process_count() == 3

@patch('psutil.sensors_temperatures')
def test_get_system_temperature(mock_sensors_temperatures):
    # Create mock sensor reading
    mock_sensor_reading = [MagicMock(current=34.0, label='Package id 0')]
    # Set the return value of the mocked function
    mock_sensors_temperatures.return_value = {'coretemp': mock_sensor_reading}
    assert get_system_temperature() == ("34.0°C", True)

def test_print_cpu_info(capsys):
    with patch('src.cpu.get_cpu_info') as mock_get_cpu_info, \
         patch('src.cpu.get_cpu_usage') as mock_get_cpu_usage, \
         patch('src.cpu.get_system_temperature') as mock_get_system_temperature, \
         patch('src.cpu.get_process_count') as mock_get_process_count, \
         patch('src.cpu.get_load_average') as mock_get_load_average:

        mock_get_cpu_info.return_value = (4, 'Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz', '2600.0000', '256 KB', '5199.99')
        mock_get_cpu_usage.return_value = 5.3
        mock_get_system_temperature.return_value = ('50.0°C', True)
        mock_get_process_count.return_value = 139
        mock_get_load_average.return_value = (1.12, 0.94, 0.88)
        print_cpu_info()
        out, err = capsys.readouterr()
        assert "CPU INFORMATION" in out
        assert "Number\x1b[0m: 4" in out
        assert "Model\x1b[0m: Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz" in out
        assert "Frequency\x1b[0m: 2600.0000 MHz" in out
        assert "Cache L2\x1b[0m: 256 KB" in out
        assert "Bogomips\x1b[0m: 5199.9" in out
        assert "CPU Usage\x1b[0m: 5.3%" in out
        assert "CPU Temperature\x1b[0m: 50.0°C" in out
        assert "Process Count\x1b[0m: 139" in out
        assert "Load average (1m)\x1b[0m: 1.12" in out
        assert "Load average (5m)\x1b[0m: 0.94" in out
        assert "Load average (15m)\x1b[0m: 0.88" in out
