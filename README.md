ansible-omd
===========

This role installs and configures [OMD (*Open Monitoring Distribution*)](https://omdistro.org).

Requirements
------------

The system needs access to the internet. Also, you will need a Linux installation supported by OMD:
- CentOS 7 / 8
- RHEL 7 / 8
- Debian 9 / 10 / 11
- Fedora 27 / 28 / 29 / 30
- SLES 12 SP2 / SP3
- Ubuntu 16.04 / 18.04 / 18.10 / 19.04 / 19.10

Role Variables
--------------

| Variable | Default | Description |
| -------- | ------- | ----------- |
| `package_omd` | `omd-3.20-labs-edition` | OMD package version to choose |

Dependencies
------------

No dependencies.

Example Playbook
----------------

Refer to the following example:

```
    - hosts: servers
      roles:
         - stdevel.ansible_omd
```

Set variables if required, e.g.:
```
---
- hosts: bacinga.giertz.loc
  remote_user: root
  roles:
    - { role: stdevel.ansible_omd, package_omd: 'omd-2.90-labs-edition' }
```


License
-------

GPL 3.0

Author Information
------------------

Christian Stankowic (info@cstan.io)
