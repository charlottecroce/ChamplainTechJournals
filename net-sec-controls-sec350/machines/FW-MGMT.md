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
copy current configuration form `configs` directory

## RIP Configuration
```
configure
set protocols rip interface eth0
set protocols rip network '172.16.200.0/28'
commit
save
```
