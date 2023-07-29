import unittest
from src.disk_info import get_disk_space

class TestGetDiskSpace(unittest.TestCase):
    def test_returns_list_of_dicts(self):
        result = get_disk_space()
        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, dict)
