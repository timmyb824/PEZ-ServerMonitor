import pytest
from unittest.mock import patch, MagicMock
from src.core.system import get_last_boot_time_macos, get_system_uptime, get_user_count_unix, get_system_info

# Test get_last_boot_time_macos
@pytest.mark.parametrize("output,expected", [
    ("{ sec = 1625097600, usec = 0 }", 1625097600.0),  # ID: valid-output
    ("", 0.0),  # ID: empty-output
    ("invalid output", 0.0),  # ID: invalid-output
], ids=["valid-output", "empty-output", "invalid-output"])
def test_get_last_boot_time_macos(output, expected):
    with patch("subprocess.run") as mocked_run:
        mocked_run.return_value = MagicMock(stdout=output)

        # Act
        result = get_last_boot_time_macos()

        # Assert
        assert result == expected

# Test get_system_uptime
@pytest.mark.parametrize("output,expected", [
    ("13:05  up 3 days, 18:53, 5 users", "13:05  up 3 days,  18:53"),  # ID: normal-case
    ("", ""),  # ID: empty-output
    ("uptime: unexpected output", "uptime: unexpected output"),  # ID: unexpected-output
], ids=["normal-case", "empty-output", "unexpected-output"])
def test_get_system_uptime(output, expected):
    with patch("subprocess.run") as mocked_run:
        mocked_run.return_value = MagicMock(stdout=output)

        # Act
        result = get_system_uptime()

        # Assert
        assert result == expected

# Test get_user_count_unix
@pytest.mark.parametrize("path,dirs,expected", [
    ("/Users", ["user1", "Shared", "user2"], 2),  # ID: normal-case
    ("/invalid/path", [], 0),  # ID: invalid-path
], ids=["normal-case", "invalid-path"])
def test_get_user_count_unix(path, dirs, expected):
    with patch("os.listdir") as mocked_listdir, patch("os.path.isdir") as mocked_isdir:
        mocked_listdir.return_value = dirs
        mocked_isdir.side_effect = lambda x: x != "/invalid/path"

        # Act
        result = get_user_count_unix(path)

        # Assert
        assert result == expected

# TODO: test is currently missing uptime and last_boot_time
@pytest.mark.parametrize("os_type,expected_keys", [
    ("Linux", ["os_type", "hostname", "kernel_info", "architecture", "dist", "dist_version", "users_nb", "current_date"]),  # ID: linux
    ("Darwin", ["os_type", "hostname", "kernel_info", "architecture", "dist", "dist_version", "users_nb", "current_date"]),  # ID: darwin
], ids=["linux", "darwin"])
def test_get_system_info(os_type, expected_keys):

    with patch("platform.system", return_value=os_type), \
         patch("platform.node", return_value="test_hostname"), \
         patch("platform.uname", return_value=MagicMock(release="test_release")), \
         patch("platform.machine", return_value="test_machine"), \
         patch("platform.mac_ver", return_value=("10.15.1", "", "")), \
         patch("os.listdir"), \
         patch("os.path.isdir", return_value=True), \
         patch("time.time", return_value=1625097600), \
         patch("distro.name", return_value="Ubuntu"), \
         patch("distro.version", return_value="20.04"):

        # Act
        result = get_system_info()

        # Assert
        for key in expected_keys:
            assert key in result



