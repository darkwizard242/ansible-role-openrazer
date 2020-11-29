import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = 'openrazer-meta'
PACKAGE_BINARY = '/usr/bin/openrazer-daemon'


def test_openrazer_package_installed(host):
    """
    Tests if openrazer is installed
    """
    assert host.package(PACKAGE).is_installed


def test_openrazer_binary_exists(host):
    """
    Tests if openrazer binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_openrazer_binary_file(host):
    """
    Tests if openrazer binary is file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_openrazer_binary_which(host):
    """
    Tests the output to confirm openrazer's binary location.
    """
    assert host.check_output('which openrazer-daemon') == PACKAGE_BINARY
