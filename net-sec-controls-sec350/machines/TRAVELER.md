# TRAVELER Configuration
Windows machine to replace RW01
## Network Configuration
- System is on WAN network
- IP address: `10.0.17.51/24`
- Default gateway: `10.0.17.2`
- DNS server: `10.0.17.2`

## SSH Key Creation for Jump Server Access
Generate SSH keys using PowerShell:
```bash
# Generate new SSH key
ssh-keygen -t rsa -b 4096 -C "traveler to jump"
# Use filename: jump-charlotte
# Add a passphrase
```
To connect to the jump server:
```powershell
ssh -i C:\Users\username\.ssh\jump-charlotte charlotte-jump@10.0.17.151
```

Web Access
Can access nginx01 via `http://10.0.17.151:80` (port forwarded through edge-01)

