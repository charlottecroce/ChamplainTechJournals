# SYS265 - Network Configuration

## pfsense router/gateway/firewall
upstream gateway: 10.0.17.2 \
my unique WAN IP: 10.0.17.104 \
net adapter 1: WAN \
net adapter 2: LAN

### wks01-charlotte - Windows workstation
IP address: 10.0.5.100/24 \
Default Gateway: 10.0.5.2\
DNS: 10.0.5.5

### ad01-charlotte - Windows server core
IP Address: 10.0.5.5/24 \
Gateway: 10.0.5.2\
DNS: 10.0.5.2

### mgmt01-charlotte - Windows server
IP address: 10.0.5.10/24 \
Gateway: 10.0.5.2\
DNS: 10.0.5.5


### nmon1-charlotte - 
IP address: 10.0.5.11/24 \
Gateway: 10.0.5.2 \
DNS: 10.0.5.5
