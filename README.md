# Ansible Linux based Git role

![Python](https://img.shields.io/pypi/pyversions/testinfra.svg?style=flat)
![Licence](https://img.shields.io/github/license/kube-cloud/ansible-role-git.svg?style=flat)
[![Travis Build](https://img.shields.io/travis/kube-cloud/ansible-role-git.svg?style=flat)](https://travis-ci.com/kube-cloud/ansible-role-git)
[![Galaxy Role Downloads](https://img.shields.io/ansible/role/d/42169.svg?style=flat)](https://galaxy.ansible.com/jetune/git)

Ansible role used to install Git on Linux based Operating System.
Installation ca be done from repository or from source

<a href="https://www.kube-cloud.com/"><img width="300" src="https://kube-cloud.com/images/branding/logo/kubecloud-logo-single_writing_horizontal_color_300x112px.png" /></a>
<a href="https://www.redhat.com/fr/technologies/management/ansible"><img width="200" src="https://getvectorlogo.com/wp-content/uploads/2019/01/red-hat-ansible-vector-logo.png" /></a>
<a href="https://git-scm.com//"><img width="250" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Git-logo.svg/1280px-Git-logo.svg.png" /></a>

# Supported Version

* Git 1.9.x/2.x.y

# Supported OS

* CentOS 6/7
* RedHat 6/7
* Ubuntu Xenial/Bionic
* Debian Jessie/Strech

# Role variables

* install_from_source: Specify whether installation is made from sour or from repository. Default value is `true`
* v_major: Used in case of installation from source and define the GIT major version to install.
* v_minor: Used in case of installation from source and define the GIT minor version to install.
* v_patch: Used in case of installation from source and define the GIT patch version to install.
* from_github: Used in case of installation from source and define whether the sources are downloaded from 
github or kernel repository. Default is `true`.
* required_packages: Used in case of installation from source and define the package needed to be installed before build GIT from source. default are 
`['make', 'dh-autoreconf', 'curl-devel', 'expat-devel', 'gettext-devel', 'openssl-devel', 'perl-devel', 'zlib-devel', 'asciidoc', 'xmlto', 'docbook2X', 'gnu-getopt']`
* force_install: Used in case of installation from source and define whether or not force install in case of GIT already installed. Default value is `true`
* install_doc: Used in case of installation from source and define whether or not build and install documentation. default value is `false`
* install_doc: Used in case of installation from source and define whether or not build and install documentation
* packages: Used in case of installation from repository (not from source) and define the list of package to be installed. default is `git-all`.
* additionnal_repos: Used in case of installation from repository (not from source) and define the RedHat based additionnal repositories to enable when install GIT packages.
default is Empty

# Usage

* Install Role ``` ansible-galaxy install jetune.git ```
* use in your playbook : case of install from repository
```
---
- hosts: all

  roles:
   - role: jetune.git
     vars:
      install_from_source: false
      git_additionnal_repos: ""
      packages:
       - git-all
       - git-svn

```
* use in your playbook : case of install from source
```
---
- hosts: all

  roles:
   - role: jetune.git
     vars:
      v_major: 2
      v_minor: 20
      v_patch: 0
      install_from_source: true
      from_github: true
      install_doc: false
      force_install: true

```
