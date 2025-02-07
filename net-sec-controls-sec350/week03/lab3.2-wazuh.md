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
- groups screen in Wazuh > create a new group called linux
- Find the agents screen in Wazuh, Deploy a new agent with the following configuration.
  - Redhat/CentoS
  - CentOS 6 or higher (Note, it will work on rocky 8)
  - x86_64
  - 172.16.200.10
  - Linux
- run the generated command on web01 to install the agent
