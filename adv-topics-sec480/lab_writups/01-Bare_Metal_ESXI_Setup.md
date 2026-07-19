# Bare Metal ESXI Setup

in this lab we set up the ESXI server, created virtual networks, and set up a vyos firewall/router and a managment workstation as VMs on the ESXI server

## installing ESXI on supermicro server
- download ISO from `CYBER-SHARE(X:)`
- install to USB via rufus
<img width="465" height="590" alt="{752F5C39-E359-436B-A26B-84EFC876E145}" src="https://github.com/user-attachments/assets/ce224558-fe6d-4216-8f79-bfabb116c659" />

- put USB in physical server
- go to IPMI interface (192.168.3.155)
- remote control > iKVM
- powercontrol > set power reset
- open virtual keyboard - spam F11
- select UEFI: <USB>
<img width="296" height="281" alt="{9F2BF516-1566-40AD-8C8A-881CEDCBB079}" src="https://github.com/user-attachments/assets/b29106c5-ac59-49d6-9314-72117b70a8e5" />

- install on smaller drive
<img width="669" height="297" alt="{352C96E1-2EF9-4546-ACF4-4B2B5F2D89CD}" src="https://github.com/user-attachments/assets/8724be06-2573-4ffd-8885-cb554df402b1" />

- REMEMBER ROOT PASSWORD
- after installation, remove USB from server and reboot from IKVM
- once the grey/yellow screen appears: F2 > configure networking

<img width="630" height="328" alt="{6E7D9E98-88D0-4025-9D2E-C9FD207AFEFD}" src="https://github.com/user-attachments/assets/c03adea5-997d-46df-b448-b8eacd29be42" />
<img width="617" height="303" alt="{DAD9450B-2071-43A6-8570-1868207B531E}" src="https://github.com/user-attachments/assets/f064e30c-692b-4b9b-9b64-be4e12c16c2c" />
<img width="612" height="263" alt="{2B09B8DC-8510-442B-946F-EF4457A41DCF}" src="https://github.com/user-attachments/assets/41c54f10-8187-4bd3-92ef-6c8233ed1836" />
<img width="559" height="202" alt="{B9550A70-52EE-4E21-95F8-451FF16DF786}" src="https://github.com/user-attachments/assets/154861f8-4538-4ce1-8020-c0eafc94f8ce" />

- ESXI console: https://192.168.3.205/ui/#/login
- create new VMFS datastore (datastore2), using the other hard drive

## Create a virtual 480-WAN

- Management Network: assigned to ESXi host, dont touch
- VM Network: Freeman Network

- add new vSwith

<img width="544" height="253" alt="{B6CF1EE5-A8A2-4D76-9CE1-42296099F6F7}" src="https://github.com/user-attachments/assets/64ec66df-a71a-4160-8a77-ec6582df272e" />

- add port group
<img width="478" height="238" alt="{16EDD717-7CA2-448F-830A-ABF75E64F6B6}" src="https://github.com/user-attachments/assets/00c139d3-6860-43b4-9d0a-152be841ada9" />

## upload ISOs
- datastore2 > datastore browser > create ISO dir, upload xubuntu, windows, vyos from shared drive

## Deploy your cyber.local gateway system called 480-fw-charlotte
- 1CPU, 2GB RAM, 10GB disk, thin provisioned
- add new network adapter, apply to VM Network
- apply vyos ISO to CD/DVD Drive
- login is `vyos:vyos`
```
install image
```

[vyos commands](https://github.com/charlottecroce/ChamplainTechJournals/blob/main/net-sec-controls-sec350/machines/FW01.md)

set hostname
```
configure
set system host-name 480-fw-charlotte
commit
save
```

allow ssh
```
set service ssh port 22
```

set interface ip
```
configure
set interfaces ethernet eth0 description 480-internal
set interfaces ethernet eth0 address 10.0.17.2/24
set interfaces ethernet eth1 description freeman
set interfaces ethernet eth1 address 192.168.3.15/24
commit
save
```

set gateway and DNS
```
configure
set protocols static route 0.0.0.0/0 next-hop 192.168.3.250
set system name-server 192.168.4.4
set system name-server 192.168.4.5
commit
save
```
set up DNS forwarding
```
set service dns forwarding listen-address 10.0.17.2
set service dns forwarding allow-from 10.0.17.0/24
set service dns forwarding system
```
set up NAT
```
set nat source rule 10 outbound-interface eth1
set nat source rule 10 source address 10.0.17.0/24
set nat source rule 10 translation address masquerade
```

*eth0 and eth1 are mixed up in ip assignments from what the sheet/video says. not an issue just be aware that freeman-WAN is eth1 and 480-internal is eth0*

export commands to save for backup
```
show configuration commands | grep -v "syslog global\|ntp\|login\|console\|config\|hw-id\|loopback\|conntrack"
```

## Deploy a 480-WAN based virtual machine (480-mgmt-charlotte)
- 1CPU, 2GB RAM, 20GB disk, thin provisioned
- apply xubuntu ISO to CD/DVD Drive
- install normally

<img width="547" height="341" alt="image" src="https://github.com/user-attachments/assets/9784dc9a-c50b-4433-b9be-7afaacf289ce" />
<img width="475" height="131" alt="image" src="https://github.com/user-attachments/assets/7aafd1e0-11d0-4b9a-8d02-9e4fd8738242" />

to reset dns
```
sudo systemctl restart systemd-resolved
```

once networking is working, set up CRD for convenience!

