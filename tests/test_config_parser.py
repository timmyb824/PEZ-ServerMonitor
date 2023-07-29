# import unittest
# from src.constants import ROOT_DIR
# from src.config_parser import parse_config_file

# class TestParseConfigFile(unittest.TestCase):
#     def test_parse_config_file(self):
#         file_path = f"{ROOT_DIR}/../config.yaml"
#         expected_config = {
#             "services": [
#                 {
#                     "name": "FTP Server",
#                     "port": 21,
#                     "host": "localhost"
#                 },
#                 {
#                     "name": "SSH",
#                     "port": 22,
#                     "host": "localhost"
#                 },
#                 {
#                     "name": "HTTP",
#                     "port": 80,
#                     "host": "localhost"
#                 },
#                 {
#                     "name": "HTTPS",
#                     "port": 443,
#                     "host": "localhost"
#                 },
#                 {
#                     "name": "MySQL Server",
#                     "port": 3306,
#                     "host": "localhost"
#                 },
#                 {
#                     "name": "PostgreSQL Server",
#                     "port": 5432,
#                     "host": "localhost"
#                 },
#                 {
#                     "name": "Zabbix-Agent",
#                     "port": 10050,
#                     "host": "localhost"
#                 },
#                 {
#                     "name": "Prometheus",
#                     "port": 9090,
#                     "host": "localhost"
#                 }
#             ],
#             "ping_hosts": [
#                 "google.com",
#                 "facebook.com",
#                 "twitter.com",
#                 "timothybryantjr.com",
#                 "github.com",
#                 "https://heimdall.local.timmybtech.com",
#                 "adguardhome.timmybtech.com"
#             ]
#         }

#         config = parse_config_file(file_path)

#         self.assertEqual(config, expected_config)

import pytest
from src.config_parser import parse_config_file

def test_parse_config_file():
    # Test a valid config file
    config = parse_config_file("./configs/config.yaml")
    assert config is not None
    assert isinstance(config, dict)
    assert "services" in config
    assert "ping_hosts" in config

    # Test a non-existent file path
    with pytest.raises(SystemExit):
        parse_config_file("./configs/non-existent.yaml")

    # Test a malformed config file
    with pytest.raises(SystemExit):
        parse_config_file("./configs/malformed_config.yaml")