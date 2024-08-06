from unittest.mock import Mock, patch

import pytest

from sysinformer.core.containers import (
    check_docker_or_podman,
    check_if_installed,
    get_running_containers,
    print_running_containers,
)
from sysinformer.utilities.exceptions import CommandNotFoundError


def test_check_if_installed_installed():
    with patch("subprocess.run"):
        assert check_if_installed("docker") is True


def test_check_if_installed_not_installed():
    with patch("subprocess.run", side_effect=CommandNotFoundError):
        check_if_installed("docker")


def test_check_docker_or_podman_docker_installed():
    with patch("sysinformer.core.containers.check_if_installed", return_value=True):
        assert check_docker_or_podman() == "docker"


def test_check_docker_or_podman_podman_installed():
    with patch(
        "sysinformer.core.containers.check_if_installed", side_effect=[False, True]
    ):
        assert check_docker_or_podman() == "podman"


# example of side_effect with a function
# def test_check_docker_or_podman_podman_installed():
#     def side_effect(cmd):
#         if cmd == 'docker':
#             raise CommandNotFoundError(f"Command '{cmd}' not found in the system's PATH.")
#         else:
#             return True

#     with patch('sysinformer.containers.check_if_installed', side_effect=side_effect):
#         assert check_docker_or_podman() == 'podman'

# another example of side_effect with a function
# def test_check_docker_or_podman_podman_installed():
#     mock_check_if_installed = Mock(side_effect=lambda cmd: cmd == 'podman')
#     with patch('sysinformer.containers.check_if_installed', new=mock_check_if_installed):
#         assert check_docker_or_podman() == 'podman'


def test_check_docker_or_podman_neither_installed():
    with patch("sysinformer.core.containers.check_if_installed", return_value=False):
        assert check_docker_or_podman() is None


@patch("subprocess.run")
def test_get_running_containers(mocked_run):
    mocked_run.return_value = Mock(
        stdout=b"12345\tmy_container\t8000->8000/tcp\tUp About a minute"
    )
    result = get_running_containers("docker")
    assert len(result) == 1
    assert result[0] == ["12345", "my_container", "8000:8000", "Up About a minute"]


@patch("subprocess.run", side_effect=Exception)
def test_get_running_containers_error(mocked_run):
    get_running_containers("docker")


@patch("sysinformer.core.containers.check_docker_or_podman", return_value="docker")
@patch("sysinformer.core.containers.get_running_containers")
@patch("builtins.print")
def test_print_running_containers(
    mocked_print, mocked_get_running_containers, mocked_check_docker_or_podman
):
    mocked_get_running_containers.return_value = [
        ["12345", "my_container", "8000:8000", "Up About a minute"]
    ]
    print_running_containers()
    assert mocked_print.called
