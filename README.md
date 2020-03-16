[![Build Status](https://travis-ci.org/stdevel/ansible-omd.svg?branch=master)](https://travis-ci.org/stdevel/ansible-omd)

omd
===

This role installs and configures [OMD (*Open Monitoring Distribution*)](https://omdistro.org).

Requirements
------------

The system needs access to the internet. Also, you will need a Linux installation supported by OMD:
- CentOS / Red Hat Enterprise Linux
  - 7
  - 8
- Fedora
  - 27
  - 28
  - 29
  - 30
- SUSE Linux Enterprise Server 12
  - SP2
  - SP3
- Debian
  - 9 (*Stretch*)
  - 10 (*Buster*)
  - 11 (*Bullseye*)
 - Ubuntu
   - 16.04 (*Xenial Xerus*)
   - 18.04 (*Bionic Beaver*)
   - 18.10 (*Cosmic Cuttlefish*)
   - 19.04 (*Disco Dingo*)
   - 19.10 (*Eoan Ermine*)

Role Variables
--------------

| Variable | Default | Description |
| -------- | ------- | ----------- |
| `repo_flavor` | `stable` | Use `stable` or `testing` repository (*nightly builds*) |
| `package_omd` | `omd-3.20-labs-edition` | OMD package version to choose |

The variable `sites` contains a dict specifying sites and their appropriate configuration to create. Refer to the following table for possible variables:

| Variable | Description |
| -------- | ----------- |
| `name` | Site name |
| `core` | Site core (*`icinga2`, `naemon` and for 2.x versions also `icinga` and `nagios`*) |
| `default_gui` | Default GUI (*`thruk`, `grafana` and for 2.x versions also `nagios` and `check_mk`*) |
| `thruk_cookie_auth` | Flag whether Thruk cookie authorization should be used |
| `remove_nagios_protection` | Flag whether insecure Nagios CGIs should be disabled (*only for 2.x versions*) |

By default, an Icinga2 site is created:
```
omd_sites:
  - name: icinga2
    core: icinga2
    default_gui: thruk
    thruk_cookie_auth: false
    remove_nagios_protection: false 
```

Dependencies
------------

No dependencies.

Example Playbook
----------------

Refer to the following example:

```
    - hosts: servers
      roles:
         - stdevel.omd
```

Set variables if required, e.g.:
```
---
- hosts: bacinga.giertz.loc
  remote_user: root
  roles:
    - role: stdevel.omd
      package_omd: 'omd-2.90-labs-edition'
```


License
-------

GPL 3.0

Author Information
------------------

Christian Stankowic (info@cstan.io)
