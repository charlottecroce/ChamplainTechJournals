# FW-MGMT Configuration

## Interface Configuration
```
configure
set interfaces ethernet eth0 description LAN
set interfaces ethernet eth1 description MGMT
set interfaces ethernet eth0 address 172.16.150.3/24
set interfaces ethernet eth1 address 172.16.200.2/28
commit
save
```

## Gateway & DNS Configuration
```
configure
set protocols static route 0.0.0.0/0 next-hop 172.16.150.2
set system name-server 172.16.150.2
commit
save
```

## DNS Forwarding
```
configure
set service dns forwarding listen-address 172.16.200.2
set service dns forwarding allow-from 172.16.200.0/28
set service dns forwarding system
commit
save
```

## Zone Configuration
```
configure
set zone-policy zone LAN interface eth0
set zone-policy zone MGMT interface eth1
commit
save
```

## Firewall Configuration

### Default Firewalls
```
configure
set firewall name LAN-to-MGMT default-action drop
set firewall name MGMT-to-LAN default-action drop
set firewall name LAN-to-MGMT enable-default-log 
set firewall name MGMT-to-LAN enable-default-log

# Assign firewalls to zones
set zone-policy zone MGMT from LAN firewall name LAN-to-MGMT
set zone-policy zone LAN from MGMT firewall name MGMT-to-LAN
commit
save
```

### LAN-to-MGMT Firewall Rules
```
configure
# Allow established traffic
set firewall name LAN-to-MGMT rule 1 action accept
set firewall name LAN-to-MGMT rule 1 state established enable

# Allow SSH MGMT-01->wazuh
set firewall name LAN-to-MGMT rule 10 description "wazuh SSH access from MGMT-01"
set firewall name LAN-to-MGMT rule 10 action accept
set firewall name LAN-to-MGMT rule 10 source address 172.16.150.10
set firewall name LAN-to-MGMT rule 10 destination address 172.16.200.10
set firewall name LAN-to-MGMT rule 10 destination port 22
set firewall name LAN-to-MGMT rule 10 protocol tcp

# Allow HTTPS MGMT-01->wazuh
set firewall name LAN-to-MGMT rule 20 description "wazuh HTTPS access from MGMT-01"
set firewall name LAN-to-MGMT rule 20 action accept
set firewall name LAN-to-MGMT rule 20 source address 172.16.150.10
set firewall name LAN-to-MGMT rule 20 destination address 172.16.200.10
set firewall name LAN-to-MGMT rule 20 destination port 443
set firewall name LAN-to-MGMT rule 20 protocol tcp

# Allow wazuh agent communication
set firewall name LAN-to-MGMT rule 30 description "wazuh agent communication with server"
set firewall name LAN-to-MGMT rule 30 action accept
set firewall name LAN-to-MGMT rule 30 destination address 172.16.200.10
set firewall name LAN-to-MGMT rule 30 destination port 1514,1515
set firewall name LAN-to-MGMT rule 30 protocol tcp
commit
save
```

### MGMT-to-LAN Firewall Rules
```
configure
# Allow established traffic back 
set firewall name MGMT-to-LAN rule 1 action accept
set firewall name MGMT-to-LAN rule 1 state established enable

# Allow MGMT to initiate any connection to LAN
set firewall name MGMT-to-LAN rule 10 description "allows MGMT to LAN"
set firewall name MGMT-to-LAN rule 10 action accept
set firewall name MGMT-to-LAN rule 10 destination address 172.16.150.0/24

# Allow MGMT to initiate any connection to DMZ
set firewall name MGMT-to-LAN rule 20 description "allows MGMT to DMZ"
set firewall name MGMT-to-LAN rule 20 action accept
set firewall name MGMT-to-LAN rule 20 destination address 172.16.50.0/29
commit
save
```

## RIP Configuration
```
configure
set protocols rip interface eth0
set protocols rip network '172.16.200.0/28'
commit
save
```
