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
import os
from src.config_parser import parse_config_file #, FileNotFoundError, YamlError

dummy_yaml = """
services:
  - name: FTP Server
    port: 21
    host: localhost
  - name: SSH
    port: 22
    host: localhost
  - name: HTTP
    port: 80
    host: localhost
  - name: HTTPS
    port: 443
    host: localhost
  - name: MySQL Server
    port: 3306
    host: localhost
  - name: PostgreSQL Server
    port: 5432
    host: localhost
  - name: Zabbix-Agent
    port: 10050
    host: localhost
  - name: Prometheus
    port: 9090
    host: localhost

ping_hosts:
  - google.com
  - facebook.com
  - twitter.com
  - timothybryantjr.com
  - github.com
  - https://heimdall.local.timmybtech.com
  - adguardhome.timmybtech.com

    """

malformed_yaml = """
    dflsjfskfjsldkfjls
    """

def setup_function(function):
    # Write the YAML's to a file
    with open("dummy.yaml", "w") as f:
        f.write(dummy_yaml)
    with open("malformed.yaml", "w") as m:
        m.write(malformed_yaml)

def test_parse_config_file():
    # Test a valid config file
    config = parse_config_file("dummy.yaml")
    assert config is not None
    assert isinstance(config, dict)
    assert "services" in config
    assert "ping_hosts" in config

    # with pytest.raises(FileNotFoundError):
    #     parse_config_file("non-existent.yaml")

    # with pytest.raises(YamlError):
    #     parse_config_file("malformed.yaml")

def teardown_function(function):
    # Delete the dummy YAML files after test
    if os.path.exists("dummy.yaml"):
        os.remove("dummy.yaml")
    if os.path.exists("malformed.yaml"):
        os.remove("malformed.yaml")