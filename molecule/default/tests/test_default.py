import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_packages(host):

    for pkg in ['qemu-kvm', 'bridge-utils', 'qemu-utils', 'libguestfs-tools', 'uml-utilities', 'ethtool', 'unzip', 'vlan']:
        host.package(pkg).is_installed

def test_simplestack_installed(host):
    f = host.file('/usr/local/bin/simplestack')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o755

def test_stack_setup_in_kvm_group(host):
    u = host.user('stack')

    assert 'kvm' in u.groups

def test_vlan_interface(host):
    f = host.file('/etc/network/interfaces.d/enp0s25.102')
    
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o644
    assert f.content_string == 'auto enp0s25.102\niface enp0s25.102 inet static\n  address 34.33.33.1\n  netmask 255.255.255.0'

    

