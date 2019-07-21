import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_git_installed(host):

    # git expected version major
    git_major = '2'

    # git expected version minor
    git_minor = '20'

    # git expected version patch
    git_patch = '0'

    # git expected version
    expected_git_version = git_major + '.' + git_minor + '.' + git_patch

    # Excected git location
    expected_git_location = '/usr/bin/git'

    # find git version
    git_version = host.run('git --version').stdout\
                      .split('\n')[0]\
                      .split(' ')[2]

    # Assert version are the same
    assert expected_git_version == git_version

    # Locate git
    git_location = host.run('which git').stdout.split('\n')[0]

    # Assert on git location
    assert expected_git_location == git_location
