# Wazuh Server Configuration

## Network Configuration
- Set hostname: `sudo hostnamectl hostname wazuh-charlotte`
- Configure static IP with netplan by editing `/etc/netplan/00-installer-config.yaml`:
  ```yaml
  network:
    ethernets:
      ens160:
        addresses:
          - 172.16.200.10/28
        nameservers:
          addresses: [172.16.200.2]
        routes:
          - to: default
            via: 172.16.200.2
    version: 2
  ```
- Apply netplan configuration:
  ```
  sudo netplan apply
  ```

## Wazuh Installation
> **IMPORTANT**: Take a snapshot before installation

Run the single-node installation command:
```
curl -sO https://packages.wazuh.com/4.7/wazuh-install.sh && sudo bash ./wazuh-install.sh -a -i
```
> Note: The `-i` flag ignores minimum requirements of 2 CPU and 4 GB RAM

**IMPORTANT**: Save the auto-generated password shown after installation, you will need it later.

## Accessing the Wazuh Dashboard
- Try accessing the dashboard at: http://172.16.200.10/app/login
- Login with the auto-generated credentials

## Wazuh Agent Management
1. Create a new agent group:
   - Wazuh dropdown > Management > Groups > Create a new group called "linux"

2. Deploy a new agent:
   - Wazuh dropdown > Agents > Deploy a new agent
   - Configuration options:
     - OS: Redhat/CentOS
     - Version: CentOS 6 or higher (works on Rocky 8)
     - Architecture: x86_64
     - Server IP: 172.16.200.10
     - Agent Group: Linux

3. The web interface will generate an installation command for your agents

## Firewall Requirements
Ensure these ports are open:
- **1514/TCP** for agent communication
- **1515/TCP** for enrollment via automatic agent request
- **55000/TCP** for enrollment via Wazuh server API

## Agent Directory Structure
Wazuh agent files are stored in `/var/ossec/`. Key directories include:
- `/var/ossec/etc/` - Configuration files
  - `/var/ossec/etc/ossec.conf` - agent IP settings
- `/var/ossec/logs/` - Log files
- `/var/ossec/queue/` - Communication queue
- `/var/ossec/agentless/` - Agentless monitoring

## Viewing Security Events
Dropdown > Modules > Security Events
