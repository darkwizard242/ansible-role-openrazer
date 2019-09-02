import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


OPENRAZER_BINARY_PATH = '/usr/bin/openrazer-daemon'
OPENRAZER_PACKAGE = 'openrazer-meta'


def test_openrazer_package_installed(host):
    host.package("OPENRAZER_PACKAGE").is_installed


def test_openrazer_binary_exists(host):
    host.file('OPENRAZER_BINARY_PATH').exists


def test_openrazer_binary_file(host):
    host.file('OPENRAZER_BINARY_PATH').is_file


def test_openrazer_binary_whereis(host):
    host.check_output('which openrazer-daemon') == OPENRAZER_BINARY_PATH
