# import unittest
# from src.disks import get_disk_space

# class TestGetDiskSpace(unittest.TestCase):
#     def test_returns_list_of_dicts(self):
#         result = get_disk_space()
#         self.assertIsInstance(result, list)
#         for item in result:
#             self.assertIsInstance(item, dict)

from unittest.mock import patch

import psutil
import pytest

from src.core.disks import get_disk_space, print_disk_info


@patch("psutil.disk_usage")
@patch("psutil.disk_partitions")
def test_get_disk_space(mock_disk_partitions, mock_disk_usage):
    mock_disk_partitions.return_value = [
        psutil._common.sdiskpart(
            device="/dev/sda1",
            mountpoint="/",
            fstype="ext4",
            opts="rw,relatime",
            maxfile=4096,
            maxpath=4096,
        )
    ]
    mock_disk_usage.return_value = psutil._common.sdiskusage(
        total=100, used=50, free=50, percent=50
    )

    expected_output = [
        {
            "device": "/dev/sda1",
            "mountpoint": "/",
            "total": 9.313225746154785e-08,
            "used": 4.6566128730773926e-08,
            "free": 4.6566128730773926e-08,
            "percentage": 50,
        }
    ]

    assert get_disk_space() == expected_output


@patch("src.core.disks.get_disk_space")
def test_print_disk_info(mock_get_disk_space, capsys):
    mock_get_disk_space.return_value = [
        {
            "device": "/dev/sda1",
            "mountpoint": "/",
            "total": 9.313225746154785e-08,
            "used": 4.656612873077393e-08,
            "free": 4.656612873077393e-08,
            "percentage": 50,
        }
    ]

    expected_output = "\x1b[92m\n=== DISK INFORMATION ===\x1b[0m\n┌───────────┬──────────────┬─────────┬─────────┬─────────┬──────────────┐\n│ Device    │ Mountpoint   │ Total   │ Used    │ Free    │ Percentage   │\n├───────────┼──────────────┼─────────┼─────────┼─────────┼──────────────┤\n│ /dev/sda1 │ /            │ 0.00 GB │ 0.00 GB │ 0.00 GB │ 50.00 %      │\n└───────────┴──────────────┴─────────┴─────────┴─────────┴──────────────┘\n"

    #     expected_output = '''
    # \x1b[92m
    # === DISK INFORMATION ===\x1b[0m
    # ┌───────────┬──────────────┬─────────┬─────────┬─────────┬──────────────┐
    # │ Device    │ Mountpoint   │ Total   │ Used    │ Free    │ Percentage   │
    # ├───────────┼──────────────┼─────────┼─────────┼─────────┼──────────────┤
    # │ /dev/sda1 │ /            │ 0.00 GB │ 0.00 GB │ 0.00 GB │ 50.00 %      │
    # └───────────┴──────────────┴─────────┴─────────┴─────────┴──────────────┘
    # '''

    print_disk_info()
    captured = capsys.readouterr()

    assert captured.out == expected_output


# Example of removing color codes from string
# In this code, the regular expression \x1b.*?m is used to match the escape sequences for the color codes,
# and the re.sub function replaces these matches with an empty string, effectively removing them from the output.

# import re

# def test_print_disk_info(capsys):
#     with patch('utils.print_title') as mock_print_title:
#         with patch('src.disk.get_disk_space') as mock_get_disk_space:
#             mock_get_disk_space.return_value = mock_disk_info
#             print_disk_info()
#     captured = capsys.readouterr()

#     # Remove color codes
#     actual_output = re.sub('\x1b.*?m', '', captured.out)
#     expected_output = '\n\n=== DISK INFORMATION ===\n┌───────────┬──────────────┬─────────┬─────────┬─────────┬──────────────┐\n│ Device    │ Mountpoint   │ Total   │ Used    │ Free    │ Percentage   │\n├───────────┼──────────────┼─────────┼─────────┼─────────┼──────────────┤\n│ /dev/sda1 │ /            │ 0.00 GB │ 0.00 GB │ 0.00 GB │ 50.00 %      │\n└───────────┴──────────────┴─────────┴─────────┴─────────┴──────────────┘\n'
#     assert actual_output == expected_output
