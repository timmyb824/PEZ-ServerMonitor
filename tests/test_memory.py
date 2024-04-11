import pytest

from src.core.memory import (  # get_memory_info,; get_memory_info_macos,
    calculate_memory_usage,
)


# Test for calculate_memory_usage
@pytest.mark.parametrize(
    "total, free, buffers, cached, expected",
    [
        (1024, 512, 100, 100, (1, 0, 100.0)),  # ID: basic-half-used
        (2048, 1024, 200, 200, (2, 1, 50.0)),  # ID: double-size-half-used
        (1024, 1024, 0, 0, (1, 1, 0.0)),  # ID: all-free
        (0, 0, 0, 0, (0, 0, 0)),  # ID: no-memory
        (1024, 0, 1024, 1024, (1, 2, -100.0)),  # ID: negative-free
    ],
)
def test_calculate_memory_usage(total, free, buffers, cached, expected):
    # Act
    result = calculate_memory_usage(total, free, buffers, cached)

    # Assert
    assert result == expected


# Test for parse_vm_stat_output
@pytest.mark.parametrize(
    "output, expected",
    [
        (
            "Mach Virtual Memory Statistics: (page size of 4096 bytes)\nPages free:       100.\nPages active:     200.\n",
            {"Pages free": 100},
        ),  # ID: basic
        ("", {}),  # ID: empty-output
        (
            "Mach Virtual Memory Statistics: (page size of 4096 bytes)\n",
            {},
        ),  # ID: header-only
    ],
)

# Mocking platform.system for get_memory_info tests
@pytest.fixture
def mock_platform_system(mocker):
    return mocker.patch("platform.system")


# Mocking subprocess.check_output for get_memory_info_macos tests
@pytest.fixture
def mock_subprocess_check_output(mocker):
    return mocker.patch("subprocess.check_output")
