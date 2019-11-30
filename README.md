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

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

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
    - { role: stdevel.ansible_omd, pv_uyuni: '/dev/vdb' }
```


License
-------

GPL 3.0

Author Information
------------------

Christian Stankowic (info@cstan.io)
