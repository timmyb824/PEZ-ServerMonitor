import platform
from unittest.mock import MagicMock, mock_open, patch

import pytest

from sysinformer.core.cpu import (
    get_cpu_cache_and_bogomips,
    get_cpu_info,
    get_cpu_usage,
    get_load_average,
    get_process_count,
    get_system_temperature,
)


@pytest.mark.parametrize(
    "os_type,expected_output",
    [
        ("Linux", ("1024 KB", "5000.00")),
        ("Darwin", ("256 KB", "N/A (No macOS Equivalent)")),
        ("Windows", ("UNKNOWN", "N/A (No macOS Equivalent)")),
    ],
    ids=["linux-happy-path", "darwin-happy-path", "unsupported-os"],
)
@patch("sysinformer.core.cpu.platform.system")
@patch("sysinformer.core.cpu.subprocess.run")
@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data="cache size: 1024 KB\nbogomips: 5000.00",
)
def test_get_cpu_cache_and_bogomips(
    mock_open, mock_subprocess_run, mock_system, os_type, expected_output
):
    mock_system.return_value = os_type
    mock_subprocess_run.return_value = MagicMock(stdout="262144\n", returncode=0)

    result = get_cpu_cache_and_bogomips()

    assert result == expected_output


@pytest.mark.parametrize(
    "cpu_count,processor,freq,expected_output",
    [
        pytest.param(
            4,
            "Intel",
            2400.0,
            (4, "Intel", 2400.0, "1024 KB", "5000.00"),
            marks=pytest.mark.skipif(
                platform.processor() != "Intel", reason="requires Intel processor"
            ),
        ),
        pytest.param(
            0,
            "Apple M3 Pro",
            0.0,
            (0, "Apple M3 Pro", 0.0, "1024 KB", "5000.00"),
            marks=pytest.mark.skipif(
                platform.processor() != "Apple M3 Pro",
                reason="requires Apple M3 Pro processor",
            ),
        ),
    ],
    ids=["linux-happy-path", "darwin-happy-path"],
)
@patch("sysinformer.core.cpu.psutil.cpu_count")
@patch("sysinformer.core.cpu.platform.processor")
@patch("sysinformer.core.cpu.psutil.cpu_freq")
@patch("sysinformer.core.cpu.get_cpu_cache_and_bogomips")
def test_get_cpu_info(
    mock_get_cpu_cache_and_bogomips,
    mock_cpu_freq,
    mock_processor,
    mock_cpu_count,
    cpu_count,
    processor,
    freq,
    expected_output,
):
    mock_cpu_count.return_value = cpu_count
    mock_processor.return_value = processor
    mock_cpu_freq.return_value = MagicMock(max=freq)
    mock_get_cpu_cache_and_bogomips.return_value = ("1024 KB", "5000.00")

    result = get_cpu_info()

    assert result == expected_output


@pytest.mark.parametrize(
    "cpu_usage,expected_output",
    [
        (25.5, 25.5),
        (0.0, 0.0),
    ],
    ids=["normal-usage", "no-usage"],
)
@patch("sysinformer.core.cpu.psutil.cpu_percent")
def test_get_cpu_usage(mock_cpu_percent, cpu_usage, expected_output):
    mock_cpu_percent.return_value = cpu_usage

    result = get_cpu_usage()

    assert result == expected_output


@pytest.mark.parametrize(
    "load_avg,expected_output",
    [
        ((0.5, 0.75, 0.9), (0.5, 0.75, 0.9)),
        ((1.0, 1.5, 2.0), (1.0, 1.5, 2.0)),
    ],
    ids=["low-load", "high-load"],
)
@patch("sysinformer.core.cpu.os.getloadavg")
def test_get_load_average(mock_getloadavg, load_avg, expected_output):
    mock_getloadavg.return_value = load_avg

    result = get_load_average()

    assert result == expected_output


@pytest.mark.parametrize(
    "process_count,expected_output",
    [
        (100, 100),
        (0, 0),
    ],
    ids=["normal-count", "no-processes"],
)
@patch("sysinformer.core.cpu.psutil.pids")
def test_get_process_count(mock_pids, process_count, expected_output):
    mock_pids.return_value = list(range(process_count))

    result = get_process_count()

    assert result == expected_output


# TODO: This test is broken. Fix it.
@pytest.mark.parametrize(
    "os_type,temps,expected_output",
    [
        (
            "Linux",
            {"coretemp": [MagicMock(label="Package id 0", current=55.0)]},
            ("Unable to get system temperature.", False),
        ),
        ("Linux", {}, ("Unable to get system temperature.", False)),
        (
            "Windows",
            {},
            ("Temperature check only supported on Linux. Current OS: Windows", False),
        ),
    ],
    ids=["linux-happy-path", "linux-no-temp", "unsupported-os"],
)
@patch("sysinformer.core.cpu.platform.system")
@patch("sysinformer.core.cpu.psutil")
def test_get_system_temperature(
    mock_sensors_temperatures, mock_system, os_type, temps, expected_output
):
    # Arrange
    mock_system.return_value = os_type
    mock_sensors_temperatures.return_value = temps

    result = get_system_temperature()

    assert result == expected_output
