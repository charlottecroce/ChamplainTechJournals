# Lab 3.1 Segmentation 1
In this lab, we are going to segment our network by adding a new firewall and a new network (MGMT). We will retire our log01 server and replace it with a new server on the MGMT network.

## wks01 (LAN)
- IP Address:  172.16.150.50
- Netmask:  255.255.255.0
- Gateway:  172.16.150.2
- DNS:  172.16.150.2


## fw01 - create a source rule 30 for NAT FROM MGMT to WAN
```
set nat source rule 30 description "NAT FROM MGMT to WAN"
set nat source rule 30 outbound-interface eth0
set nat source rule 30 source address 172.16.200.0/28
set nat source rule 30 translation address masquerade
```


## fw-mgmt

![image](https://github.com/user-attachments/assets/e9fe5785-ef2b-4efa-9cc2-f10c25cc9476)
Configure your fw-mgmt firewall's hostname with interface descriptions and interface addresses:
- eth0:  LAN-172.16.150.3/24
- eth1:  MGMT-172.16.200.2/28 (NOTE: MGMT is using a /28!)

```
set interfaces ethernet eth0 description LAN
set interfaces ethernet eth1 description MGMT
set interfaces ethernet eth0 address 172.16.150.3/24
set interfaces ethernet eth1 address 172.16.200.2/28
```
![image](https://github.com/user-attachments/assets/68f108b9-2a62-4575-9614-c2ec286093ad)

Set the following:
- gateway next-hop: `set protocols static route 0.0.0.0/0 next-hop 172.16.150.2`
name server to your fw01’s LAN interface address: `set system name-server 172.16.150.2`
set dns forwarding such that requests are allowed from your management subnet and management interface.
```
set nat source rule 40 description "NAT from MGMT to WAN"
set nat source rule 40 outbound-interface eth0
set nat source rule 40 source address 172.16.200.0/28
set nat source rule 40 translation address masquerade
```


## mgmt02 (MGMT)
- IP Address:  172.16.200.11
- Netmask:  255.255.255.240 (yes this is a /28)
- Gateway:  172.16.200.2
- DNS:  172.16.200.2



## RIP on FW1 and FW-MGMT
fw01
```
set protocols rip interface eth2
set protocols rip network '172.16.50.0/29'
```
fw-mgmt
```
set protocols rip interface eth0
set protocols rip network '172.16.200.0/28'
```




## wazuh (MGMT)
- IP: 172.16.200.10/28
- Gateway:  172.16.200.2
- DNS: 172.16.200.2

