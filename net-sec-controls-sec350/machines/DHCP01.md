# DHCP01 Configuration
## Basic Setup
- Set hostname to `dhcp01-charlotte`
- Add sudo user `charlotte`

Set network via netplan:
- IP Address: `172.16.150.???/24`
- Gateway & DNS: `172.16.150.2`
- Network adapter: LAN


## Install and Configure DHCP Server

Install DHCP server
```bash
sudo apt update
sudo apt install isc-dhcp-server -y
```
Configure DHCP server
```bash
> sudo nano /etc/dhcp/dhcpd.conf

default-lease-time 600;
max-lease-time 7200;
option subnet-mask 255.255.255.0;
option broadcast-address 172.16.150.255;
option routers 172.16.150.2;
option domain-name-servers 172.16.150.2;

subnet 172.16.150.0 netmask 255.255.255.0 {
  range 172.16.150.100 172.16.150.150;
}
```
Configure the interface for DHCP server:
```bash
> sudo nano /etc/default/isc-dhcp-server
...
INTERFACESv4="ens160"
INTERFACESv6=""
...
```
Start and enable DHCP server
```bash
sudo systemctl enable isc-dhcp-server
sudo systemctl restart isc-dhcp-server
```

## Install Wazuh Agent
```bash
# Download and install Wazuh agent
curl -o wazuh-agent-4.7.5-1.amd64.deb https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-agent/wazuh-agent-4.7.5-1.amd64.deb && sudo WAZUH_MANAGER='172.16.200.10' WAZUH_AGENT_GROUP='linux' WAZUH_AGENT_NAME='dhcp01-charlotte' dpkg -i wazuh-agent-4.7.5-1.amd64.deb

# Start the agent
sudo systemctl daemon-reload
sudo systemctl enable wazuh-agent
sudo systemctl start wazuh-agent
```
