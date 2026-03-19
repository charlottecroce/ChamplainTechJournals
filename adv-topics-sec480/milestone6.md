# Milestone 6 - Blue Network and Intro To Ansible

## installing ansible
```
sudo apt install software-properties-common
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt install ansible -y
```

## issues
- vyos machine didn't have an IP when first created, and while we want to assign IP via ansible we need to be able to access the machine, so we had to manually setup DHCP on eth0 to get an IP.
- ansible uses ssh, and you need to first connect via ssh directly, and enable ssh on vyos
```
set service ssh port 22
service ssh enable
service ssh start
```
