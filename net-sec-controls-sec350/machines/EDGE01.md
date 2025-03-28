# EDGE01 Configuration

## Initial Setup
- Change password:
```
configure
set system login user vyos authentication plaintext-password password123!
commit
save
```
- Change hostname:
```
configure
set system host-name edge01-charlotte
commit
save
```

## Interface Configuration
```
configure
set interfaces ethernet eth0 description SEC350-WAN
set interfaces ethernet eth1 description CHARLOTTE-DMZ
set interfaces ethernet eth2 description CHARLOTTE-LAN
set interfaces ethernet eth0 address 10.0.17.151/24
set interfaces ethernet eth1 address 172.16.50.2/29
set interfaces ethernet eth2 address 172.16.150.2/24
commit
save
```
## Gateway and DNS Configuration
```
configure
set protocols static route 0.0.0.0/0 next-hop 10.0.17.2
set system name-server 10.0.17.2
commit
save
```
## NAT Configuration
```
configure
# DMZ to WAN NAT
set nat source rule 10 description "NAT FROM DMZ to WAN"
set nat source rule 10 outbound-interface eth0
set nat source rule 10 source address 172.16.50.0/29
set nat source rule 10 translation address masquerade

# LAN to WAN NAT
set nat source rule 20 description "NAT FROM LAN to WAN"
set nat source rule 20 outbound-interface eth0
set nat source rule 20 source address 172.16.150.0/24
set nat source rule 20 translation address masquerade

# MGMT to WAN NAT
set nat source rule 30 description "NAT FROM MGMT to WAN"
set nat source rule 30 outbound-interface eth0
set nat source rule 30 source address 172.16.200.0/28
set nat source rule 30 translation address masquerade

# Port Forwarding for HTTP
set nat destination rule 10 description "HTTP->NGINX01"
set nat destination rule 10 inbound-interface eth0
set nat destination rule 10 destination port 80
set nat destination rule 10 protocol tcp
set nat destination rule 10 translation address 172.16.50.3

commit
save
```
## DNS Forwarding Configuration
```
configure
# DMZ DNS Forwarding
set service dns forwarding listen-address 172.16.50.2
set service dns forwarding allow-from 172.16.50.0/29

# LAN DNS Forwarding
set service dns forwarding listen-address 172.16.150.2
set service dns forwarding allow-from 172.16.150.0/24

set service dns forwarding system
commit
save
```

## Zone Configuration
```
configure
set zone-policy zone WAN interface eth0
set zone-policy zone DMZ interface eth1
set zone-policy zone LAN interface eth2
commit
save
```

## Firewall Configuration
```
configure
# Create Zone-Based Firewalls

# WAN-to-DMZ
set firewall name WAN-to-DMZ default-action drop
set firewall name WAN-to-DMZ enable-default-log
set firewall name WAN-to-DMZ rule 1 action accept
set firewall name WAN-to-DMZ rule 1 state established enable
set firewall name WAN-to-DMZ rule 10 description "allow HTTP from WAN to DMZ"
set firewall name WAN-to-DMZ rule 10 action accept
set firewall name WAN-to-DMZ rule 10 destination address 172.16.50.3
set firewall name WAN-to-DMZ rule 10 destination port 80
set firewall name WAN-to-DMZ rule 10 protocol tcp

# DMZ-to-WAN
set firewall name DMZ-to-WAN default-action drop
set firewall name DMZ-to-WAN enable-default-log
set firewall name DMZ-to-WAN rule 1 action accept
set firewall name DMZ-to-WAN rule 1 state established enable

# LAN-to-DMZ
set firewall name LAN-to-DMZ default-action drop
set firewall name LAN-to-DMZ enable-default-log
set firewall name LAN-to-DMZ rule 1 action accept
set firewall name LAN-to-DMZ rule 1 state established enable
set firewall name LAN-to-DMZ rule 10 description "Allow HTTP from LAN to DMZ"
set firewall name LAN-to-DMZ rule 10 action accept
set firewall name LAN-to-DMZ rule 10 destination address 172.16.50.3
set firewall name LAN-to-DMZ rule 10 destination port 80
set firewall name LAN-to-DMZ rule 10 protocol tcp
set firewall name LAN-to-DMZ rule 20 description "Allow SSH from MGMT-01 to DMZ"
set firewall name LAN-to-DMZ rule 20 action accept
set firewall name LAN-to-DMZ rule 20 destination port 22
set firewall name LAN-to-DMZ rule 20 protocol tcp
set firewall name LAN-to-DMZ rule 20 source address 172.16.150.10

# DMZ-to-LAN
set firewall name DMZ-to-LAN default-action drop
set firewall name DMZ-to-LAN enable-default-log
set firewall name DMZ-to-LAN rule 1 action accept
set firewall name DMZ-to-LAN rule 1 state established enable
set firewall name DMZ-to-LAN rule 10 description "wazuh agent communication with server"
set firewall name DMZ-to-LAN rule 10 action accept
set firewall name DMZ-to-LAN rule 10 destination address 172.16.200.10
set firewall name DMZ-to-LAN rule 10 destination port 1514,1515
set firewall name DMZ-to-LAN rule 10 protocol tcp

# LAN-to-WAN
set firewall name LAN-to-WAN default-action drop
set firewall name LAN-to-WAN enable-default-log
set firewall name LAN-to-WAN rule 1 action accept

# WAN-to-LAN
set firewall name WAN-to-LAN default-action drop
set firewall name WAN-to-LAN enable-default-log
set firewall name WAN-to-LAN rule 1 action accept
set firewall name WAN-to-LAN rule 1 state established enable

# Apply Zone Policies
set zone-policy zone DMZ from LAN firewall name LAN-to-DMZ
set zone-policy zone DMZ from WAN firewall name WAN-to-DMZ
set zone-policy zone LAN from DMZ firewall name DMZ-to-LAN
set zone-policy zone LAN from WAN firewall name WAN-to-LAN
set zone-policy zone WAN from DMZ firewall name DMZ-to-WAN
set zone-policy zone WAN from LAN firewall name LAN-to-WAN

commit
save
```
## Rip Configuration
```
configure
set protocols rip interface eth2
set protocols rip network '172.16.50.0/29'
commit
save
```

## SSH Configuration
```
# Restrict SSH access to LAN interface only
configure
set service ssh listen-address 172.16.150.2
commit
save
```
