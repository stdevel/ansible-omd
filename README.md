[![Build Status](https://travis-ci.org/stdevel/ansible-omd.svg?branch=master)](https://travis-ci.org/stdevel/ansible-omd)

# omd

This role installs and configures [OMD (*Open Monitoring Distribution*)](https://omdistro.org).

## Requirements

The system needs access to the internet. Also, you will need a Linux installation supported by OMD:

- CentOS / Red Hat Enterprise Linux
  - 7
  - 8
- Fedora
  - 32
- SUSE Linux Enterprise Server 12
  - SP2
  - SP3
- Debian
  - 9 (*Stretch*)
  - 10 (*Buster*)
  - 11 (*Bullseye*)
- Ubuntu
  - 18.04 (*Bionic Beaver*)
  - 20.04 (*Focal Fossa*)

Also make sure to have [EPEL](https://fedoraproject.org/wiki/EPEL) enabled for CentOS or Red Hat Enterprise Linux systems!

## Role Variables

| Variable | Default | Description |
| -------- | ------- | ----------- |
| `omd_repo_flavor` | `stable` | Use `stable` or `testing` repository (*nightly builds*) |
| `omd_version` | `4.00` | OMD package version to choose |

The variable `sites` contains a dict specifying sites and their appropriate configuration to create. Refer to the following table for possible variables:

| Variable | Description |
| -------- | ----------- |
| `name` | Site name |
| `core` | Site core (*`icinga2`, `naemon` and for 2.x versions also `icinga` and `nagios`*) |
| `default_gui` | Default GUI (*`thruk`, `grafana` and for 2.x versions also `nagios` and `check_mk`*) |
| `thruk_cookie_auth` | Flag whether Thruk cookie authorization should be used |
| `remove_nagios_protection` | Flag whether insecure Nagios CGIs should be disabled (*only for 2.x versions*) |
| `admin_password` | `omdadmin` default password (*default: `omd`*) |

By default, an Icinga2 site is created:

```yaml
omd_sites:
  - name: icinga2
    core: icinga2
    default_gui: thruk
    thruk_cookie_auth: false
    remove_nagios_protection: false
    admin_password: omd
```

## Dependencies

No dependencies.

## Example Playbook

Refer to the following example:

```yaml
    - hosts: servers
      roles:
         - stdevel.omd
```

Set variables if required, e.g.:

```yaml
---
- hosts: bacinga.giertz.loc
  remote_user: root
  roles:
    - role: stdevel.omd
      package_omd: '4.00'
```

Keep in mind enabling EPEL on RHEL/CentOS systems:

```yaml
---
- hosts: bluecap.giertz.loc
  remote_user: root
  roles:
    - role: geerlingguy.repo-epel
    - role: stdevel.omd
      omd_version: '3.30'
```

## License

GPL 3.0

## Author Information

Christian Stankowic (info@cstan.io)
