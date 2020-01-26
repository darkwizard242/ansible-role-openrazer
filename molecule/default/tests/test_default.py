import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_openrazer_package_installed(host):
    assert host.package("openrazer-meta").is_installed


def test_openrazer_binary_exists(host):
    assert host.file('/usr/bin/openrazer-daemon').exists


def test_openrazer_binary_file(host):
    assert host.file('/usr/bin/openrazer-daemon').is_file


def test_openrazer_binary_which(host):
    assert host.check_output('which openrazer-daemon') == \
    '/usr/bin/openrazer-daemon'
