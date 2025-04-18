# SEC350 Project 2: Remote Access to MGMT02 via WireGuard VPN
Andrei Gorlitsky, Benjamin Tyler, Charlotte Croce\
4/17/25

---

## Objective
Allow remote administrator **Tanisha** to securely access **MGMT02** (`172.16.200.11`) using RDP through a WireGuard VPN hosted on the **jump** server (`172.16.200.10`). Traveler (`10.0.17.55`) will serve as the VPN client.

---

## System Overview

| VM         | Role                 | IP Address    | Network |
| ---------- | -------------------- | ------------- |---------|
| `jump`     | WireGuard VPN Server | 172.16.200.10 | DMZ     |
| `traveler` | WireGuard VPN Client | 10.0.17.55    | WAN     |
| `mgmt02`   | RDP Target           | 172.16.200.11 | MGMT    |

---

## Configuration

### Install WireGuard on Jump (Ubuntu)
```bash
sudo apt update
sudo apt install wireguard -y
```

### Generate VPN Keys on Jump
```bash
umask 077
wg genkey | tee server_private.key | wg pubkey > server_public.key
```
Example output:
```
PrivateKey = PRIVATEKEYJUMP
PublicKey  = PUBLICKEYJUMP
```

### Step 3: Configure WireGuard Server
Create and edit `/etc/wireguard/wg0.conf`:
```ini
[Interface]
Address = 10.10.10.1/24
PrivateKey = PRIVATEKEYJUMP
ListenPort = 51820

[Peer]
PublicKey = PUBLICKEYWINDOWS
AllowedIPs = 10.10.10.2/32
```
Start the service:
```bash
sudo systemctl enable wg-quick@wg0
sudo systemctl start wg-quick@wg0
```

###Configure WireGuard on Traveler (Windows)
1. Install from [https://www.wireguard.com/install/](https://www.wireguard.com/install/)
2. Open the WireGuard GUI and click "Add Tunnel > Add Empty Tunnel"
3. Keys auto-generate:
```
PrivateKey = PRIVATEKEYWINDOWS
PublicKey  = PUBLICKEYWINDOWS
```
4. Use the following configuration:
```ini
[Interface]
PrivateKey = PRIVATEKEYWINDOWS
Address = 10.10.10.2/24

[Peer]
PublicKey = PUBLICKEYJUMP
Endpoint = 172.16.200.10:51820
AllowedIPs = 172.16.200.11/32
PersistentKeepalive = 25
```
5. Click "Activate"

### Enable IP Forwarding and NAT on Jump
```bash
sudo sysctl -w net.ipv4.ip_forward=1
```
Make it permanent:
```bash
sudo nano /etc/sysctl.conf
# Add or uncomment:
net.ipv4.ip_forward=1
sudo sysctl -p
```
Configure NAT:
```bash
sudo iptables -t nat -A POSTROUTING -s 10.10.10.0/24 -o <interface> -j MASQUERADE
```
Replace `<interface>` with the name of the jump box’s MGMT interface (e.g., `ens160`).

### Configure Firewall Rules on VyOS
```vyos
set firewall name DMZ-to-MGMT rule 100 action accept
set firewall name DMZ-to-MGMT rule 100 source address 10.10.10.2
set firewall name DMZ-to-MGMT rule 100 destination address 172.16.200.11
set firewall name DMZ-to-MGMT rule 100 destination port 3389
set firewall name DMZ-to-MGMT rule 100 protocol tcp
commit
save
```

### Enable RDP on MGMT02
1. Go to `Settings > System > Remote Desktop` and enable RDP.
2. Create a user:
```powershell
net user tanisha SuperSecurePass123 /add
net localgroup "Remote Desktop Users" tanisha /add
```

---

## Testing
- Activate WireGuard tunnel on traveler
- `ping 172.16.200.11` from traveler
- Open Remote Desktop (`mstsc`) and connect to:
  - IP: `172.16.200.11`
  - Username: `mgmt02-andrei\tanisha`
  - Password: `SuperSecurePass123`

---

## Suggested Screenshots
- `/etc/wireguard/wg0.conf` file on jump
- Keys (with private blurred)
- WireGuard tunnel status in traveler GUI
- Successful ping to MGMT02
- RDP session connected
- VyOS firewall rule
- `wg show` output on jump

---


## Final Result
Tanisha can now securely access MGMT02 over an encrypted WireGuard tunnel. The VPN is restricted to only the required IP and port.

## Sources
- https://www.wireguard.com/
