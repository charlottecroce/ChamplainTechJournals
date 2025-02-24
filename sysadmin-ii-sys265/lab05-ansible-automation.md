# Automation with Ansible
Demonisioning: web01, nmon-01, docker-01 😢
___
## New Machines
### controller-charlotte - Ubuntu
configure with netplan
```
network:
  ethernets:
    ens160:
      dhcp4: no
      addresses:
        - 10.0.5.90/24
      routes:
        - to: default
          via: 10.0.5.2
      nameservers:
        addresses:
          - 10.0.5.5
  version: 2
```
#### to reset DNS
```
dhclient -r
dhclient
```
### ansible1-charlotte - CentOS
configure with nmtui
- IP: 10.0.5.91
- DG: 10.0.5.2
- DNS: 10.0.5.5
### ansible2-charlotte - CentOS
configure with nmtui
- IP: 10.0.5.92
- DG: 10.0.5.2
- DNS: 10.0.5.5

## Initial Configuration
- on all machines, create a sudo account named deployer (use same password across all systems)
- install ansible on controller
```
sudo apt install ansible sshpass python3-paramiko
```
- Configure sudo access:
  - create `/etc/sudoers.d/sys265` on all systems
  - add the following line to allow passwordless sudo for deployer:
   ```
   deployer ALL=(ALL) NOPASSWD:ALL
   ```

> [!Note]
> Although it is not uncommon to update `/etc/sudoers` directly, it is far easier to script the addition of a file to `/etc/sudoers.d`


## SSH Key Setup
As the deployer user on controller:
- Create RSA keypair with passphrase:
```
ssh-keygen -t rsa
```
- copy pukey to ansible1 and ansible2
```
ssh-copy-id deployer@ansible1-charlotte
ssh-copy-id deployer@ansible2-charlotte
```
-configure `ssh-agent` to avoid typing passphrase for 4 hours
```
eval(ssh-agent) # test to see if ssh-agent is running, and if not,run it
ssh-add -t 14400
```
## Ansible Configuration
in `deployer@controller:/home/deployer/`
- make directory structure
```
mkdir -p ansible/roles
cd ansible/
```
- create inventory and test conection
```
echo ansible1-charlotte >> inventory.txt
echo ansible2-charlotte >> inventory.txt
cat inventory.txt
```
```
ansible all -m ping -i inventory.txt
```

- add webmin tag to `inventory.txt` and test

```
ansible1-charlotte
[webmin]
ansible2-charlotte
```

```
deployer@controller-charlotte:~/ansible$ ansible webmin -m ping -i inventory.txt
ansible2-charlotte | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/libexec/platform-python"
    },
    "changed": false,
    "ping": "pong"
}
```

## webmin installation
- install webmin role
```
ansible-galaxy install semuadmin.webmin -p roles/
```
- create `webmin.yml` playbook to handle repository setup, installation, and firewall configuration
```
- name: webmin sys265
  hosts: webmin
  become: true    # Run all tasks with sudo/root privileges
  vars:
    install_utilities: false
    firewalld_enable: true

  pre_tasks: # before role execution. we need the repo/key before executing webmin installation role
    - name: add webmin repo and GPG key
      yum_repository:
        name: webmin
        description: Webmin Distribution Neutral
        baseurl: http://download.webmin.com/download/yum
        enabled: true
        gpgcheck: true
        gpgkey: http://www.webmin.com/jcameron-key.asc

   # update YUM cache to recognize new repository
    - name: clean and update YUM cache
      yum:
        update_cache: yes

  roles:
    - semuadmin.webmin    # apply the webmin installation role

  handlers: # will run when a task has notify:name parameter
    - name: reload firewall # runs after adding firewall rule
      command: firewall-cmd --reload

  tasks:
    # open port 10000 in firewall for webmin web interface
    - name: add firewall rule
      firewalld:
        port: 10000/tcp
        permanent: true
        state: enabled
      notify: reload firewall

    - name: install webmin
      yum:
        name: webmin
        state: present # will only install if not already

    - name: enable and start webmin service
      systemd:
        name: webmin
        enabled: true
        state: started
        daemon_reload: yes # reload systemd to recognize new service
```
- run playbook
```
ansible-playbook -i inventory.txt roles/webmin.yml
```
- change webmin root password
```
 sudo /usr/libexec/webmin/changepass.pl /etc/webmin root newpassword
```


## apache isntallation
- edit inventory.txt
```
[apache]
ansible1-charlotte
[webmin]
ansible2-charlotte
```
- install apache role
```
ansible-galaxy install geerlingguy.apache -p roles/
```
- create `apache.yml` file
```
- name: apache sys265
  hosts: apache
  become: true    # Run all tasks with sudo/root privileges
  vars:
    install_utilities: false
    firewalld_enable: true
    ansible_os_family: RedHat
    ansible_distribution: CentOS # required because role searches for Rocky config files
  roles:
    - geerlingguy.apache    # apply the apache installation role

  handlers: # will run when a task has notify:name parameter
    - name: reload firewall # runs after adding firewall rule
      command: firewall-cmd --reload

  tasks:
    # open port 443 in firewall for apache web interface
    - name: add firewall rule
      firewalld:
        port: "{{ item }}"
        permanent: true
        immediate: true
        state: enabled
      loop:
        - 80/tcp
        - 443/tcp
      notify: reload firewall

    - name: install apache
      yum:
        name: httpd
        state: present # will only install if not already

    - name: enable and start apache service
      systemd:
        name: httpd
        enabled: true
        state: started
        daemon_reload: yes # reload systemd to recognize new service

```
- run playbook
```
ansible-playbook -i inventory.txt roles/webmin.yml
```

# Ansible on Windows
## OpenSSH Server Setup

>[!Caution]
> DO NOT INSTALL 32 BIT VERSION

### Install OpenSSH
Run these commands in PowerShell as Administrator:
```
wget https://github.com/PowerShell/Win32-OpenSSH/releases/download/v9.8.1.0p1-Preview/OpenSSH-Win64.zip -O 'C:\Program Files\OpenSSH.zip'
Expand-Archive -Path 'C:\Program Files\OpenSSH.zip' -DestinationPath 'C:\Program Files\OpenSSH'
rm 'C:\Program Files\OpenSSH.zip'
powershell.exe -ExecutionPolicy Bypass -File 'C:\Program Files\OpenSSH\OpenSSH-Win64\install-sshd.ps1'
```
### Configure OpenSSH
- start service
```
Start-Service sshd
Set-Service -Name sshd -StartupType 'Automatic'
Get-Service -Name sshd # check if running
```
- add firewall rule
```
New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH Server' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
Get-NetFirewallRule | Where-Object DisplayName -Like '*ssh*'
```
- set PowerShell as default SSH shell
```
Set-ItemProperty "HKLM:\Software\Microsoft\Powershell\1\ShellIds" -Name ConsolePrompting -Value $true
New-ItemProperty -Path HKLM:\SOFTWARE\OpenSSH -Name DefaultShell -Value "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -PropertyType String -Force
```
- add `charlotte.croce-adm` to the **Remote Management Users** groups
- Add/uncomment the following lines in C:\ProgramData\ssh\sshd_config
  - `StrictModes no` is sometimes needed on Windows systems because Windows permissions don't map perfectly to the UNIX-style permissions that OpenSSH expects
```
AllowUsers charlotte\charlotte.croce-adm
StrictModes no
```
## Ansible Setup
### Inventory Setup
- add windows machines to `inventory.txt`
```
[windows]
mgmt01-charlotte
wks01-charlotte
[windows:vars]
ansible_shell_type=powershell
```
- create ansible.cfg in ansible directory, to skip host key checking
```
[defaults]
host_key_checking = false
```
- test connection
```
ansible windows -i inventory.txt -m win_ping -u charlotte.croce-adm@charlotte.local --ask-pass
```

## Software deployment using win_chocolatey
- create playbook `roles/windows_software.yml`
```
- name: install windows applications
  hosts: windows
  tasks:
    - name: install firefox and 7zip
      win_chocolatey:
        name:
        - firefox
        - 7zip
        state: present
```
- run playbook
```
ansible-playbook -i inventory.txt roles/windows_software.yml -u charlotte.croce-adm@charlotte.local --ask-pass
```
- If you encounter .NET Framework errors, install version 4.8 (in my case I needed version 4.8, it will probably be a different version in the future)
```
Invoke-WebRequest -Uri "https://go.microsoft.com/fwlink/?linkid=2088631" -OutFile "C:\dotNetFx48.exe"
Start-Process -FilePath "C:\dotNetFx48.exe" -ArgumentList "/quiet /norestart" -Wait
Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full" -Name Release # verify installation
```
> [!Note]:
> Installation may take several minutes. System restart required after installation.

- list packages installed with chocolatey
```
'C:\ProgramData\chocolatey\bin\choco.exe' list
```

