# 0\_Network Configuration

### vSphere

https://vcenter02.cyber.local\
Username: nathan.croce@cyber.local\
Password: cyber.local password

### fw01-SYS-255-01-nathan.croce - PfSense firewall

IP Address: 10.0.17.104\
Upstream gateway: 10.0.17.2\
LAN interface: 10.0.5.2\
Network Adapter 1: WAN\
Network Adapter 2: LAN

### wks01-nathan - Windows workstation

IP address: 10.0.5.100\
Default Gateway: 10.0.5.2\
DNS: 10.0.5.6

### ad01-nathan - Windows server

IP Address: 10.0.5.6\
Gateway: 10.0.5.2\
DNS 10.0.5.2

### dhcp01-nathan - DHCP server

IP Address: 10.0.5.4\
Gateway: 10.0.5.2\
DNS 10.0.5.6

### fs01-nathan - file server

IP Address: 10.0.5.8\
Gateway: 10.0.5.2\
DNS 10.0.5.6

### web01-nathan - web server

IP Address: 10.0.5.10\
Gateway: 10.0.5.2\
DNS 10.0.5.6
