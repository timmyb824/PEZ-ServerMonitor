import platform
import subprocess
from unittest.mock import MagicMock, patch

import pytest

from sysinformer.core.system import (
    get_last_boot_time,
    get_system_uptime,
    get_user_count_unix,
)


# Test for macOS
@pytest.mark.skipif(
    platform.system() != "Darwin", reason="Test only applicable on macOS"
)
def test_get_last_boot_time_macos():
    with patch("subprocess.run") as mocked_run:
        mocked_run.return_value = subprocess.CompletedProcess(
            args=["sysctl", "-n", "kern.boottime"],
            returncode=0,
            stdout="sec = 1640995200\n",
        )
        assert get_last_boot_time() == "2021-12-31 19:00:00"


# Test for Linux
@pytest.mark.skipif(
    platform.system() != "Linux", reason="Test only applicable on Linux"
)
def test_get_last_boot_time_linux():
    with patch("subprocess.run") as mocked_run:
        mocked_run.return_value = subprocess.CompletedProcess(
            args=["uptime", "-s"], returncode=0, stdout="2024-04-10 12:34:56\n"
        )
        assert get_last_boot_time() == "2024-04-10 12:34:56"


@pytest.mark.skipif(platform.system() != "Linux", reason="Running on non-Linux system")
def test_get_system_uptime_linux():
    with patch("platform.system", return_value="Linux"), patch(
        "os.stat", return_value=MagicMock(st_ctime=1000)
    ), patch("time.time", return_value=2000):
        assert get_system_uptime() == "0 days, 0 hours, 16 minutes"

    with patch("platform.system", return_value="Linux"), patch(
        "os.stat", side_effect=Exception("Error")
    ):
        assert get_system_uptime() == "Error in obtaining uptime"


@pytest.mark.skipif(
    platform.system() != "Darwin", reason="Running on non-Darwin system"
)
def test_get_system_uptime_darwin():
    with patch("platform.system", return_value="Darwin"), patch(
        "subprocess.run", return_value=MagicMock(stdout="10:00 up 1 day, 2:00")
    ):
        assert get_system_uptime() == "10:00 up 1 day,  2:00"

    with patch("platform.system", return_value="Darwin"), patch(
        "subprocess.run", side_effect=subprocess.CalledProcessError(1, "uptime")
    ):
        assert get_system_uptime() == "Error in obtaining uptime"


# Test get_user_count_unix
@pytest.mark.parametrize(
    "path,dirs,expected",
    [
        ("/Users", ["user1", "Shared", "user2"], 2),  # ID: normal-case
        ("/invalid/path", [], 0),  # ID: invalid-path
    ],
    ids=["normal-case", "invalid-path"],
)
def test_get_user_count_unix(path, dirs, expected):
    with patch("os.listdir") as mocked_listdir, patch("os.path.isdir") as mocked_isdir:
        mocked_listdir.return_value = dirs
        mocked_isdir.side_effect = lambda x: x != "/invalid/path"

        # Act
        result = get_user_count_unix(path)

        # Assert
        assert result == expected


# TODO: Add test back for get_system_info

