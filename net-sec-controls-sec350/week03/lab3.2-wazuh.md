# Lab 3.2 - Wazuh
In this lab, we are going to experiment with a far more modern logging system called Wazuh.  Wazuh is one of several ELK based SIEMs.  We are using this one because of the relatively ease of installation as well as functionality.  Unlike a traditionally syslog client and server, Wazuh allows us to install agents on supported systems.  Agents can refine that information sent to their SIEM for streamlined analysis.

>[!Warning]
>TAKE A SNAPSHOT BEFORE INSTALLATION

## Installation
For a single node installation on wazuh, run the following command.
`curl -sO https://packages.wazuh.com/4.7/wazuh-install.sh && sudo bash ./wazuh-install.sh -a -i`
(added -i to ignore minimum requirements of 2CPU and 4 GB RAM)

>[!Note]
>Save the auto-generated password, you will need it later

## Wazuh/OSSEC Agent on web01
- Wazuh dropdown > management > groups > create a new group called linux
- Wazuh dropdown > agents > Deploy a new agent with the following configuration.
  - Redhat/CentoS
  - CentOS 6 or higher (Note, it will work on rocky 8)
  - x86_64
  - 172.16.200.10
  - Linux
- run the generated command on web01 to install the agent:
```
curl -o wazuh-agent-4.7.5-1.x86_64.rpm https://packages.wazuh.com/4.x/yum/wazuh-agent-4.7.5-1.x86_64.rpm && sudo WAZUH_MANAGER='172.16.200.10' WAZUH_AGENT_GROUP='linux' WAZUH_AGENT_NAME='web01-charlotte' rpm -ihv wazuh-agent-4.7.5-1.x86_64.rpm
```
![image](https://github.com/user-attachments/assets/c6c6ae88-635e-4db1-a1d3-e1473bf63653)
![image](https://github.com/user-attachments/assets/1609a92a-ffe2-4d93-8477-f6669a95c2f5)

- start the agent
```
sudo systemctl daemon-reload
sudo systemctl enable wazuh-agent
sudo systemctl start wazuh-agent
```

## to view security events
dropdown > modules > security events
