# VyOS 
an open source networking OS based on Debian \
https://docs.vyos.io/en/sagitta/

## Overview
- VyOS has two modes: operational and configuration mode
- The operational mode is used to view the system status and run commands (command prompt displays `$`)
- the configuration mode is used to modify the system configuration (command prompt displays `#`)

## Commands
### Basics
- enter configuration mode from operational mode: `configure`
- exit configuration mode: `exit`
- commit current set of changes `commit`
- save current changes: `save`
  - `commit`, followed by `save` will save configuration changes

### Change Password
```
set system login user charlotte authentication plaintext-password [password]
```

### Set Hostname
```
set system host-name fw01-charlotte
```
 
### Interfaces
- set IP: `set interfaces ethernet ethX address 172.16.50.X./24`
- add description: `set interfaces ethernet ethX description SEC350-WAN`

### Gateway and DNS Server
- create default route (gateway): `set protocols static route 0.0.0.0/0 next-hop 10.0.17.2`
- set DNS server: `set system name-server 10.0.17.2`


### NAT
```
set nat source rule 10 description "NAT FROM DMZ to WAN"
set nat source rule 10 outbound-interface eth0
set nat source rule 10 source address 172.16.50.0/29
set nat source rule 10 translation address masquerade
```

### DNS Forwarding
```
set service dns forwarding listen-address 172.16.50.2
set service dns forwarding allow-from 172.16.50.0/29
set service dns forwarding system
```

