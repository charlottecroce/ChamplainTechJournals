# Lab 6.1: Port Forwarding and Jump Boxes

## RW01 -> WEB
security issue:  rw01 knows the internal routing for our DMZ and used this information to create a static route from SEC350-WAN to the DMZ.  A better alternative is to mask the presence of the DMZ altogether with NAT destination rules.

- remove static ip route from rw01 to DMZ
```
sudo ip route del 172.16.50.0/29
```

## WAN to DMZ NAT
We've worked with NAT **source** rules when dealing with traffic from inside the network going out to the WAN.  Now we are going to add a NAT **destination** rule (aka port forwarding) so that any port 80 traffic coming to our firewall's WAN/eth0 interface will be forwarded on to web01. 
```
set nat destination rule 10 description "HTTP->WEB01"
set nat destination rule 10 inbound-interface eth0
set nat destination rule 10 destination port 80
set nat destination rule 10 protocol tcp
set nat destination rule 10 translation address 172.16.50.3
```

## Jump server
- log01 is back! but it's a jump server now
- IP Address: 172.16.50.4/29
- hostname: jump-charlotte


- Adjust the firewall rules from LAN-TO-DMZ  such that mgmt01 can ssh into any server on the DMZ.


- Make sure that fw01 is only listening for SSH on the LAN interface (172.16.150.2) and not on all interfaces (0.0.0.0/0)
![image](https://github.com/user-attachments/assets/76304685-062f-41df-ac18-092174428aa2)

sudo systemctl restart ssh



On rw01, create a dedicated keypair that will only be used for ssh access to jump. make sure to name the keypair something other than the default and add a comment indicating its purpose.  Make sure to add a passphrase when prompted.

```
ssh-keygen -t rsa -b 4096 -C "ssh to jump"
name of file: jump-charlotte
```
(this is a public key! it's okay to share, unlike private keys)
```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDLLKDg5fIw8CINt5IOY3vZ6XiudxKn0sXZ1hTWbugfKQ9NZjfSCbboxIlVpyqAwnFzf+3oJcPpnlVLjXpugJe6ghfuLsO/1fdqFQ5/PBcQbJXFvdIH93MJ78sBUhT+SbhHLas6KjShSOhNz5fRYOMOTpCtB7eQhk5q3gqTEvmDejgWZPphyAQJCnB0hw+J76jl3t68Q+FtD57RWhWhp/0ZQPfjY+hnJOfLaD+Zs0tsxvYXqDuPhRt2J2xUHF8LgaqZYkosIllfcX//tmEnQ90nU+zLu3jje8Pqy4mfjGsV8wZ+ug7ModwJwR2ToieqoiyOnDq1ytG0r5sKjeM5RTX6tJTOl8ltr7E51u0bajjym0ZL4kT0W82Eld/DV4+BzbEB6yCSWWVwo/eKoqkGBIHpIibzkjPGCQ4O0tq3s+04DpOpucDqk0J+Yphdj/qmK/mYFLU0xKZnIJl8otyItyVhV2zTIn64PQ3gEE8z0O4GjEJEfhkJ29ydtXXDFIpCfSirmfH7HbXlwgUmxHJqnCBqZ8eKb/n52ekaD0SIOPQE76RmR540cus3mvo3t30Ak79NBSjEh82k2rP42eVx/GhF/o3u8DdCF3xA46dzqt1HMvOpnOjdvbldP076VKkxV/px9nE7mJZysxei8SisrSbwn7vxLem4LrDsAIxfsGcULw== ssh to jump
```


create a passwordless user called `charlotte-jump` on jump.  Copy over the public component of the jump keypair you just created on rw01 to the new user's `.ssh/authorized_keys` file. 

```
useradd -m -d /home/charlotte-jump -s /bin/bash charlotte-jump
sudo sed -i 's/PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config

# create .ssh directory, give perms to user
mkdir -p /home/charlotte-jump/.ssh
chmod 700 /home/charlotte-jump/.ssh

echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDLLKDg5fIw8CINt5IOY3vZ6XiudxKn0sXZ1hTWbugfKQ9NZjfSCbboxIlVpyqAwnFzf+3oJcPpnlVLjXpugJe6ghfuLsO/1fdqFQ5/PBcQbJXFvdIH93MJ78sBUhT+SbhHLas6KjShSOhNz5fRYOMOTpCtB7eQhk5q3gqTEvmDejgWZPphyAQJCnB0hw+J76jl3t68Q+FtD57RWhWhp/0ZQPfjY+hnJOfLaD+Zs0tsxvYXqDuPhRt2J2xUHF8LgaqZYkosIllfcX//tmEnQ90nU+zLu3jje8Pqy4mfjGsV8wZ+ug7ModwJwR2ToieqoiyOnDq1ytG0r5sKjeM5RTX6tJTOl8ltr7E51u0bajjym0ZL4kT0W82Eld/DV4+BzbEB6yCSWWVwo/eKoqkGBIHpIibzkjPGCQ4O0tq3s+04DpOpucDqk0J+Yphdj/qmK/mYFLU0xKZnIJl8otyItyVhV2zTIn64PQ3gEE8z0O4GjEJEfhkJ29ydtXXDFIpCfSirmfH7HbXlwgUmxHJqnCBqZ8eKb/n52ekaD0SIOPQE76RmR540cus3mvo3t30Ak79NBSjEh82k2rP42eVx/GhF/o3u8DdCF3xA46dzqt1HMvOpnOjdvbldP076VKkxV/px9nE7mJZysxei8SisrSbwn7vxLem4LrDsAIxfsGcULw== ssh to jump" >> /home/charlotte-jump/.ssh/authorized_keys

# set perms, set new user as directory owner
chmod 600 /home/charlotte-jump/.ssh/authorized_keys
chown -R charlotte-jump:charlotte-jump /home/charlotte-jump/.ssh

systemctl restart sshd
```

## install wazuh agent on jump
on mgmt01
```
wget https://packages.wazuh.com/4.x/yum/wazuh-agent-4.7.3-1.x86_64.rpm
scp wazuh-agent-4.7.3-1.x86_64.rpm charlotte@172.16.50.4:~
```

on jump
```
scp wazuh-agent-4.7.3-1.x86_64.rpm charlotte@172.16.50.4:~
sudo WAZUH_MANAGER='172.16.200.10' WAZUH_AGENT_GROUP='linux' WAZUH_AGENT_NAME='jump-charlotte' rpm -ihv wazuh-agent-4.7.3-1.x86_64.rpm
sudo systemctl daemon-reload
sudo systemctl enable wazuh-agent
sudo systemctl start wazuh-agent
```
![image](https://github.com/user-attachments/assets/500def07-6fb1-4fb5-82a8-4c4f433e3861)


