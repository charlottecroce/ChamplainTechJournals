# Network Machine Configuration Table

| Machine | IP Address | Default Gateway | DNS Server | Network |
|----------|------------|----------------|------------|-----------------|
| [fw01](machines/FW01.md) | eth0: 10.0.17.151/24<br>eth1: 172.16.50.2/29<br>eth2: 172.16.150.2/24 | 10.0.17.2 | 10.0.17.2 | WAN/DMZ/LAN |
| [edge01](machines/EDGE01.md) | eth0: 10.0.17.151/24<br>eth1: 172.16.50.2/29<br>eth2: 172.16.150.2/24 | 10.0.17.2 | 10.0.17.2 | WAN/DMZ/LAN |
| [fw-mgmt](machines/FW-MGMT.md) | eth0: 172.16.150.3/24<br>eth1: 172.16.200.2/28 | 172.16.150.2 | 172.16.150.2 | LAN/MGMT |
| [web01](machines/WEB01.md) | 172.16.50.3/29 | 172.16.50.2 | 172.16.50.2 | DMZ |
| [nginx01](machines/NGINX01.md) | 172.16.50.???/29 | 172.16.50.2 | 172.16.50.2 | DMZ |
| [log01](machines/LOG01.md) | 172.16.50.5/29 | 172.16.50.2 | 172.16.50.2 | DMZ |
| [jump](machines/LOG01.md#recommissioned-as-jump-server) | 172.16.50.4/29 | 172.16.50.2 | 172.16.50.2 | DMZ |
| [wazuh](machines/WAZUH.md) | 172.16.200.10/28 | 172.16.200.2 | 172.16.200.2 | MGMT |
| [mgmt01](machines/MGMT01.md) | 172.16.150.10/24 | 172.16.150.2 | 172.16.150.2 | LAN |
| [mgmt02](machines/MGMT02.md) | 172.16.200.11/28 | 172.16.200.2 | 172.16.200.2 | MGMT |
| [wks01](machines/WKS01.md) | 172.16.150.50/24 | 172.16.150.2 | 172.16.150.2 | LAN |
| [rw01](machines/RW01.md) | 10.0.17.51/24 | 10.0.17.2 | 10.0.17.2 | WAN |
| [traveler](machines/TRAVELER.md) | 10.0.17.51/24 | 10.0.17.2 | 10.0.17.2 | WAN |
| [dhcp01](machines/DHCP01.md) | 172.16.150.???/24 | 172.16.150.2 | 172.16.150.2 | LAN |

*Note: fw01 was replaced by edge01, web01 was replaced by nginx01, log01 was repurposed as jump-charlotte, and rw01 was replaced by traveler*
