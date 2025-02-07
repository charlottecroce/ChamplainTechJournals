# Wazuh

## Installing Server
- run the following command: `curl -sO https://packages.wazuh.com/4.7/wazuh-install.sh && sudo bash ./wazuh-install.sh -a -i`
- remember to save the auto-generated password

### Ports to open on firewall
- **1514/TCP** for agent communication.
- **1515/TCP** for enrollment via automatic agent request.
- **55000/TCP** for enrollment via Wazuh server API.

## Installing Agents
- Wazuh dropdown > Agents > enter agent configurations
- run the generated command on the remote system to install the agent:
- start agent service:
```
sudo systemctl daemon-reload
sudo systemctl enable wazuh-agent
sudo systemctl start wazuh-agent
```

## Agent directory structure
Wazuh agent files are stored in /var/ossec/. Key directories include:
- `/var/ossec/etc/` - Configuration files
  - `/var/ossec/etc/ossec.conf` - agent IP settings
- `/var/ossec/logs/` - Log files
- `/var/ossec/queue/` - Communication queue
- `/var/ossec/agentless/` - Agentless monitoring
