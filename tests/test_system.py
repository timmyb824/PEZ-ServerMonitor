import collections
import time
from unittest.mock import mock_open, patch

import pytest

from src.core.system import get_system_info


@patch("platform.system")
@patch("platform.node")
@patch("platform.uname")
@patch("platform.machine")
@patch("os.stat")
@patch("os.listdir")
@patch("distro.name")
@patch("platform.freedesktop_os_release")
def test_get_system_info(
    mock_freedesktop,
    mock_name,
    mock_listdir,
    mock_stat,
    mock_machine,
    mock_uname,
    mock_node,
    mock_system,
):
    mock_system.return_value = "Linux"
    mock_name.return_value = "Ubuntu"
    mock_freedesktop.return_value = {"VERSION": "20.04"}
    mock_node.return_value = "test-host"

    # Create a named tuple with a `release` attribute
    Uname = collections.namedtuple("Uname", "release")
    mock_uname.return_value = Uname(release="test-release")

    mock_machine.return_value = "test-machine"
    mock_stat.return_value.st_ctime = 50 * 365 * 24 * 3600
    mock_listdir.return_value = ["user1", "user2", "user3"]

    expected_result = (
        "Linux",
        "Ubuntu",
        "20.04",
        "test-host",
        "0 days, 0 hours, 0 minutes",
        "2023-01-01 00:00:00",
        "test-release",
        "test-machine",
        3,
        "2023-01-01 00:00:00",
    )

    with patch(
        "time.time", return_value=50 * 365 * 24 * 3600
    ):  # Returns the number of seconds in 50 years
        with patch("time.localtime", return_value=time.gmtime(0)):
            with patch("time.strftime", return_value="2023-01-01 00:00:00"):
                result = get_system_info()
    assert result == expected_result


@patch("os.stat")
def test_get_system_info_no_proc(mock_stat):
    mock_stat.side_effect = FileNotFoundError
    get_system_info()


@patch("os.listdir")
def test_get_system_info_no_home(mock_listdir):
    mock_listdir.side_effect = FileNotFoundError
    get_system_info()
