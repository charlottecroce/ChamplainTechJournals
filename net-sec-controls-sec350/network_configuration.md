# network configuration

### Rw01: This is the “road warrior” linux laptop.  A computer that sits outside your organization's network
WAN IP: 10.0.17.51/24

### Fw01: This is a vyos router/firewall that connects the SEC-350 (ISP), DMZ, and LAN networks
WAN IP: 10.0.17.151/24 \
DMZ IP: 172.16.50.2/29 \
LAN IP: 172.16.150.2/24

### Web01: This is the organization's CENTOS web server in the DMZ
DMZ IP: 172.16.50.3/29

### Log01: This is the organization’s CentOS log server (in DMZ for now)
DMZ IP: 172.16.50.5/29
