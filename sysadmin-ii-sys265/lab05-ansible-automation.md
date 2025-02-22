# Automation with Ansible

Demonisioning: web01, nmon-01, docker-01 😢
___
## New Machines
### controller-charlotte - Ubuntu
![image](https://github.com/user-attachments/assets/536fa018-b4aa-4f51-8a29-329a367f7e74)
#### to reset DNS
`dhclient -r`
`dhclient`
### ansible1-charlotte - CentOS
setup with nmtui: 10.0.5.91
### ansible2-charlotte - CentOS
setup with nmtui: 10.0.5.92

- on each machine, create a sudo account named deployer (have the same password for all of them)

## installing ansible
sudo apt install ansible sshpass python3-paramiko

Create /etc/sudoers.d/sys265 on all Linux systems.
💣 Although it is not uncommon to update /etc/sudoers directly, it is far easier to script the addition of a file to /etc/sudoers.d.  The following line allows the deployer sudo user to elevate without a password.

![image](https://github.com/user-attachments/assets/0bc22606-bdd2-405b-bd14-70d0e308fb38)

As the deployer user on controller, create an RSA keypair with a passphrase protected private key and using ssh-copy-id, add deployer@controller's public key to the deployer accounts on ansible1 and ansible2.

`ssh-add -t 14400` - for 4 hours, you won't need to retype the key passphrase

💡ssh-agent allows you to decrypt your private key, in this case for 4 hours so that you only have to type your passphrase once every four hours. The eval command will test to see if ssh-agent is running, and if not, it will run it.

in deployer@controller home dir
 mkdir -p ansible/roles
   cd ansible/
   echo ansible1-charlotte >> inventory.txt
   echo ansible2-charlotte >> inventory.txt
   cat inventory.txt
  ansible all -m ping -i inventory.txt

![image](https://github.com/user-attachments/assets/e66fec43-6a85-4935-8aa6-d371db1ac2be)

![Uploading image.png…]()

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

install webadmin

 ansible-galaxy install semuadmin.webmin -p roles/


Create a playbook called webmin.yml within the roles directory that has the displayed content. Don't use tabs, use two spaces for indentation. 
