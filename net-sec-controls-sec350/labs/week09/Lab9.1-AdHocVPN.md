# Lab 9.1 - Ad Hoc VPN with SSH
SSH allows you to create a remote port forwarding tunnel such that connections to a local port on traveler will traverse an ssh tunnel from traveler to jump and then be forwarded to a system of your choice, say mgmt02.

- Enable RDP on mgmt02
- Create a named local administrator account (charlotte) if not done so already
- Create the DMZ-to-LAN and LAN-to-MGMT rules necessary for RDP to connect to mgmt02
```
# on edge-02
set firewall name DMZ-to-LAN rule 40 action 'accept'
set firewall name DMZ-to-LAN rule 40 description 'jump to RDP'
set firewall name DMZ-to-LAN rule 40 destination address '172.16.200.11'
set firewall name DMZ-to-LAN rule 40 destination port '3389'
set firewall name DMZ-to-LAN rule 40 protocol 'tcp'

# on fw-mgmt
set firewall name LAN-to-MGMT rule 40 action 'accept'
set firewall name LAN-to-MGMT rule 40 description 'jump to RDP'
set firewall name LAN-to-MGMT rule 40 destination address '172.16.200.11'
set firewall name LAN-to-MGMT rule 40 destination port '3389'
set firewall name LAN-to-MGMT rule 40 protocol 'tcp'
```

source: https://www.cloudthat.com/resources/blog/a-guide-to-access-rdp-through-ssh-tunneling-using-putty
## Invoke an SSH connection from traveler to jump such that RDP connections in that tunnel are redirected to mgmt02.
### Step 1: Configure PuTTY for SSH Tunneling
- Launch PuTTY on your source Windows machine
- In the "Session" category:
  - Enter the IP of jump box[actually the firewall interface -PF] (10.0.17.151)
  - Keep port 22 / SSH
  - Optionally save your session configuration

### Step 2: Set Up the SSH Tunnel for RDP
- In the PuTTY Configuration window, navigate to Connection > SSH > Tunnels
- Configure the tunnel with:
  - Source port: 3390 (or any unused local port)
  - Destination: 172.16.200.11:3389 (mgmt02)
  - Select "Local" and "Auto" options
  - Click "Add" to create the tunnel

### Step 3: Connect to the Jump Box
- Return to the "Session" category
- save your configuration
- Click "Open" to connect to the Linux jump box/ enter jump box creds

### Step 4: Connect via RDP Through the Tunnel
- With the SSH connection active, open Remote Desktop Connection on your source Windows machine
- In the "Computer" field, enter: localhost:3390
- Click "Connect" and enter credentials for the destination Windows machine





___
### Scrapped Idea Using command (doesn't work)

```
ssh -J charlotte@10.0.17.151 -L 3389:172.16.200.11:3389 charlotte@172.16.200.11
```

`-J  charlotte@10.0.17.151`: Specifies the jump host. This is the firewall address but firewall port forwards ssh to jump
`-L 22:172.16.200.11:3389`: Creates a local port forwarding. This tells SSH to listen on 3389 on your local machine and forward any connections to 172.16.200.11 on3389.
`charlotte@172.16.200.11`: Specifies the target RDP server

