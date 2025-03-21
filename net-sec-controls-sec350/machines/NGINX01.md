# NGINX01 Configuration
## Basic Setup
- Set hostname to `nginx01-charlotte`
- Add sudo user `charlotte`

- Set network via nmtui:
  - IP Address: `172.16.50.???/29`
  - Gateway & DNS: `172.16.50.2`
  - Network adapter: DMZ

## Install and Configure NGINX
```bash
# Install NGINX
sudo apt update
sudo apt install nginx -y
sudo systemctl enable nginx
sudo systemctl start nginx

# Create custom index page
echo "<h1>NGINX01 - Charlotte Croce</h1>" | sudo tee /var/www/html/index.html
```

* Remember to add firewall and port forwarding rule for this new IP!
* Also, add firewall-cmd rules if applicable

## Install Wazuh Agent
```bash
# Download and install Wazuh agent
curl -o wazuh-agent-4.7.5-1.amd64.deb https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-agent/wazuh-agent-4.7.5-1.amd64.deb && sudo WAZUH_MANAGER='172.16.200.10' WAZUH_AGENT_GROUP='linux' WAZUH_AGENT_NAME='nginx01-charlotte' dpkg -i wazuh-agent-4.7.5-1.amd64.deb

# Start the agent
sudo systemctl daemon-reload
sudo systemctl enable wazuh-agent
sudo systemctl start wazuh-agent
```
