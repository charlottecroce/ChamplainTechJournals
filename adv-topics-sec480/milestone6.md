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



# milestone 6 part 2
at this point the ESXi has expired. this journal shows how to reset the trial period.
https://github.com/seraphimgerber/SEC-480-Advanced-Topics-in-Cyber-Security/wiki/Extending-ESXi-Host-Trial-License

to setup the ansible playbook, we need a vyos template. create the firewall manually, then we will copy the configuration to add as a .j2 file
```
set interfaces ethernet eth0 address '10.0.17.200/24'
set interfaces ethernet eth1 address '10.0.15.2/24'

set nat source rule 10 outbound-interface 'eth0'
set nat source rule 10 source address '10.0.5.0/24'
set nat source rule 10 translation address 'masquerade'

set protocols static route 0.0.0.0/0 next-hop 10.0.17.2

set service dns forwarding allow-from '10.0.5.0/24'
set service dns forwarding listen-address '10.0.5.2'
set service dns forwarding system

set service ssh port '22'
set system name-server '10.0.17.4'
```

- once you export configuration of setup machines, paste it into config.boot.j2. replace all the hardcoded variables with the variable name in blue-5-fw-vars.txt
- write ansible playbook (vyos-config.yml) to copy template configuration to boot file, then restart vyos
