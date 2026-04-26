# NET333=0 final - part 2
At the conclusion of Part 1, you have designed and started configuring the Hospital Network in Packet Tracer.  For Part 2 of the assignment, you will:

Configure DHCP for Main, North, and South
Configure Routing through the ISP
Configure Static NAT to map public IP's to internal servers
Configure PAT to all workstations to communicate on the Internet
 

Configure DHCP for Main, North, and South
Main: Add a server to the Central-Data Center-Production server VLAN
Assign the server an IP address on that VLAN
Update the default pool to include addresses from the Backbone VLAN
Add pools for all other Central VLANs
Add helper address to all router configurations
Workstations must be able to get IPs from proper pool
North: Add a server to the North-Clinic VLAN
Assign the server an IP address on that VLAN
Update the default pool for North-Clinic VLAN
Add a pool for the North-Guest VLAN
Workstations must be able to get IPs from proper pool
South: same steps as North
Configure routing through ISP
The Main Campus Border Router should have a connection to the ISP Router
The North and South Border/Distribution Router should have connections to the ISP Router
The Border routers should be able to ping the ISP router on their shared network
Main: 152.16.10.0/24
South: 212.232.16.0/24
North: 89.25.202.0/24
Configure default routes on the border routers to send traffic to ISP router
ip route 0.0.0.0 0.0.0.0 ip-address-of-ISP-router-on-shared-network
If correct, should be able to ping public IPs between border routers
Configure Static NAT to map Public IPs to internal servers
Add another server to Main-Central-Data-Center-Production VLAN and assign appropriate IP address
Configure Static NAT on Main Border Router to map a Main Campus IP to the new server
Configure PAT for Main, North, and South clients
Configure PAT on the 3 border routers to allow internal private address workstations to access external addresses
Hint #1: For access-list, you do not need to include every subnet and can use 172.16.0.0/16 to represent all internal networks
Hint #2: Multilayer switches cannot have physical interfaces set as incoming or outgoing interfaces, but their logical interfaces can! You'll want to set your VLAN interfaces for Clinic/Guest/Building Control as incoming, set the public IP for the switch on VLAN 1 (don't forget "no shutdown"), and make the VLAN 1 interface the outgoing one.
If Static NAT and PAT are successful, a North or South workstation should be able to access the web page on the new server using the assigned Public IP address





# dhcp

production Server gets a static IP: 172.16.12.10 (this is the DHCP server)

|Pool Name	|Default Gateway	|Start IP	|Subnet Mask|
|-|-|-|-|
|serverPool (default/backbone)	|172.16.15.2	|172.16.15.15	|255.255.255.0|
|guest	|172.16.0.2	|172.16.0.15	|255.255.252.0|
|clinic	|172.16.4.2	|172.16.4.15	|255.255.252.0|
|building	|172.16.8.2	|172.16.8.15	|255.255.254.0|
|psych	|172.16.10.3	|172.16.10.15	|255.255.255.0|
|counseling	|172.16.11.1	|172.16.11.15	|255.255.255.0|
|production	|172.16.12.2	|172.16.12.15	|255.255.255.0|
|dev	|172.16.13.2	|172.16.13.15	|255.255.255.0|
|health	|172.16.14.2	|172.16.14.15	|255.255.255.0|

<img width="762" height="435" alt="image" src="https://github.com/user-attachments/assets/930db34b-8ec7-4cc6-9bdd-f59b41c0fc8a" />

open port on dc edge
```
interface f0/24
switchport mode access
switchport access vlan 60
no shutdown
```


add helper addressess on all three mls
```
interface vlan 10
ip helper-address 172.16.12.10
interface vlan 20
ip helper-address 172.16.12.10
interface vlan 30
ip helper-address 172.16.12.10
interface vlan 40
ip helper-address 172.16.12.10
interface vlan 50
ip helper-address 172.16.12.10
interface vlan 60
ip helper-address 172.16.12.10
interface vlan 70
ip helper-address 172.16.12.10
interface vlan 80
ip helper-address 172.16.12.10
interface vlan 90
ip helper-address 172.16.12.10
```


## north and south mls

