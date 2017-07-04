import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_packages(host):

    for pkg in ['qemu-kvm', 'bridge-utils', 'qemu-utils', 'libguestfs-tools', 'uml-utilities', 'ethtool','unzip']:
        host.package(pkg).is_installed

def test_simplestack_installed(host):
    f = host.file('/usr/local/bin/simplestack')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o755
