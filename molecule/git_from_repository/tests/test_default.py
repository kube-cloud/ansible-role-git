import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_git_installed(host):

    # Excected git location
    expected_git_location = '/usr/bin/git'

    # find git version
    assert host.run('git --version').rc == 0

    # Locate git
    git_location = host.run('which git').stdout.split('\n')[0]

    # Assert on git location
    assert expected_git_location == git_location
