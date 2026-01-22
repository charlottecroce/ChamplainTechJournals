# Lab 2-1: Subnet Design  

| VLAN | VLAN\_NAME | Hosts Needed | Network | Netmask | Router Address |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | Management | 250 | 10.16.0.0 | 255.255.255.0 | 10.16.0.1 |
| 100 | FacStaff | 200 | 10.16.1.0 | 255.255.255.0 | 10.16.1.1 |
| 110 | Student | 450 | 10.16.2.0 | 255.255.254.0 | 10.16.2.1 |
| 130 | StuLab1 | 35 | 10.16.12.0 | 255.255.255.192 | 10.16.12.1 |
| 140 | StuLab2 | 35 | 10.16.12.64 | 255.255.255.192 | 10.16.12.65 |
| 200 | StuWireless | 900 | 10.16.4.0 | /22 | 10.16.4.1 |
| 210 | FSWireless | 650 | 10.15.8.0 | /22 | 10.16.8.1 |

## Configure Edge Switches

* Add vlans to the vlan database

100 and 110 to all
```
(config)#vlan 100
(config-vlan)# name FacStaff
(config)#vlan 110
(config-vlan)# name Student
```

130 (Lab1) in East-02 switch only
```
(config)#vlan 130
(config-vlan)# name StuLab1
```

140 (Lab2) in West-02 switch only
```
(config)#vlan 140
(config-vlan)# name StuLab2
```

All edge switches assigned VLAN 100 (FacStaff) on ports 4-12
```
(config)# interface range fa0/4 - 12
(config-if-range)# switchport mode access
(config-if-range)# switchport access vlan 100
```

All edge switches assigned VLAN 110 (Student) on ports 13-20
```
(config)# interface range fa0/13 - 20
(config-if-range)# switchport mode access
(config-if-range)# switchport access vlan 110
```

East-Edge-02 assigned VLAN 130 (Lab1) on ports 21-24
```
(config)# interface range fa0/21 - 24
(config-if-range)# switchport mode access
(config-if-range)# switchport access vlan 130
```

West-Edge-02 assigned VLAN 140 (Lab2) on ports 21-24
```
(config)# interface range fa0/21 - 24
(config-if-range)# switchport mode access
(config-if-range)# switchport access vlan 140
```

## Configure End User Devices

* Assign FacStaff PC's IP's from VLAN 100 (make sure netmask and gateway are correct)
  * IPs: 10.16.1.x  
  * Gateway 10.16.1.1  
  * Connect to interface fa0/4 \- 12

* Assign Student PC's IP's from VLAN 110
   * IPs: 10.16.2.x  
   * Gateway 10.16.2.1  
   * Connect to interface fa0/13 \- 20

* Assign Lab PC's appropriate IP's
   * Remember 2 different VLANs/subnets

## Configure Trunking

### Configure trunk ports for Core switches

* Add vlans 100, 110, 130, and 140 to the vlan database on Core Switches

Configure FastEthernet 0/1 and 0/2 as trunk ports for the appropriate vlans
```
(config)# interface range f0/1 - 2
(config-if-range)# switchport trunk encapsulation dot1q
(config-if-range)# switchport mode trunk
(config-if-range)# switchport trunk allowed vlan 100,110,130,140
```

### Configure trunk ports for edge switches
Configure FastEthernet 0/1 as trunk port for the appropriate vlans
```
(config)# interface f0/1
(config-if)# switchport mode trunk
(config-if)# switchport trunk allowed vlan 100,110,130,140
```

- Create Cross-over cable connection between edge switch and core switch trunk ports

## Enable Routing

* We will use the EAST-Core Switch as the Router
  * Assign the router addresses from the table to:
  * VLANs 100,110,130, 140 to East-Core
```
ip routing
interface vlan 100
ip address 10.16.1.1 255.255.255.0
no shutdown

interface vlan 110
ip address 10.16.2.1 255.255.254.0
no shutdown

interface vlan 130
ip address 10.16.12.1 255.255.255.192
no shutdown

interface vlan 140
ip address 10.16.12.65 255.255.255.192
no shutdown
```

**NOTE: This only needs to be set on the router-switch acting as the gateway for the vlan**

You should now be able to ping between two systems on different VLANs in EAST 

## Configure East-West Trunk

Configure Gigabit Ethernet 0/1 on both East and West core switches as trunk ports for defined vlans
```
(config)# interface g0/1
(config-if)# switchport trunk encapsulation dot1q
(config-if)# switchport mode trunk
(config-if)# switchport trunk allowed vlan 100,110,130,140
```

- Copper "cross-over" connector to connect those trunk ports

You should be able to ping between all devices!

## Useful commands:

Commands to navigate different modes on a Cisco Switch/Router (enable, config t...) and how you know what mode you are in

```
> = exec mode

enable / en
# = privileged exec mode

configure terminal / conf t
(config)# = configuration mode
```

Commands to create VLANS on switch

```
(config)# vlan 10
(config-vlan)# name management
```

Setting access and trunk ports on switch

```
access:
switchport mode access
sw m a

trunk:
switchport trunk encapsulation dot1q (if not already set)
switchport mode trunk
sw m tr
```

Configure interfaces in "ranges"

```
interface range f0/1 - 9
int range f0/1 - 9
```
