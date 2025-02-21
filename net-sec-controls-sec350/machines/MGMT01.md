# MGMT01 Configuration

## Network Configuration
- Configure static IP via network manager:
  - IP Address: `172.16.150.10/24`
  - Gateway & DNS: `172.16.150.2`
  - Network: LAN

## Chrome Remote Desktop Setup
1. Open Chrome and sign in with charlotte.croce@mymail.champlain.edu
2. Enable sync if prompted
3. Go to remotedesktop.google.com and install the app
4. On your main host (laptop):
   - Go to https://g.co/crd/headless
   - Download and install the Chrome Remote Desktop package
   - For dependency issues:
     ```
     sudo apt install libutempter0 xbase-clients xserver-xorg-video-dummy xvfb
     sudo dpkg -i google-chrome-stable_current_amd64
     ```
5. Follow the setup prompts and create a PIN
6. Log out of the remote computer before attempting to connect

## Notes
- With current firewall configs, this machine should be able to access:
  - SSH to systems in the DMZ (port 22)
  - HTTPS access to wazuh server (port 443)
