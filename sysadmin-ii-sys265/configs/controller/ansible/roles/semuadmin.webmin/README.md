Role Name
=========

## THIS REPO IS NO LONGER BEING ACTIVELY MAINTAINED OR SUPPORTED.

### IF ANYONE ELSE WANTS TO TAKE ON THE MAINTENANCE AND SUPPORT, FEEL FREE TO FORK IT.

[Ansible role](https://galaxy.ansible.com/semuadmin/webmin) to deploy Webmin web-based linux administration utility, running as a 
systemd service.

Webmin service will be available on https://hostip:10000.

Default login will be the userid and password of the installer user.

You may get a browser warning about Webmin's default self-sign SSL certificate.

System will reboot after installation.


Requirements
------------

- Installation requires sudo privileges.
- Systemd for services control.
- Firewalld for firewall control (if required).
- Python for Ansible provisioning (note that some minimal distributions do not include python out of the box).

Role Variables
--------------

- `install_utilities`: false.  Set to True to install various utility packages used by Webmin management functions (wget, git, ntpdate, sntp, smartmontools).
Note that some minimal distributions do not support all these tools out of the box and may require interactive installation.

- `enable_firewalld`: false.  Set to True to open port 10000 via firewalld (assumes firewalld is installed and running).

- `uninstall_webmin` : false.  Set to true to uninstall Webmin.

Dependencies
------------

None.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml

    - name: Provision webmin role
      hosts: all
      become: true
      become_user: root
      
      vars:
         enable_firewalld: true
         install_utilities: true

      roles:
      - semuadmin.webmin
```
     
License
-------

BSD 3-Clause
