# Lab 1.1, Routing and DMZ

## Configuring rw01
- Secure your champuser default account by changing the password: `password123!`
- Add a new sudo user `charlotte:password123!` - `sudo usermod -aG sudo charlotte`
- Set your hostname: `sudo hostnamectl set-hostname rw01-charlotte`
- Make sure you have a static ip that matches the one in the IP assignments spreadsheet: use nmtui, set IP to `10.0.17.51/24` and gateway/DNS to `10.0.17.2` \
![image](https://github.com/user-attachments/assets/46252357-1387-45bd-a4ae-ede9e12417c9)


## Configuring fw01
![image](https://github.com/user-attachments/assets/723c16dc-f130-4f61-9508-b0fe70adbca5) \
default creds: `vyoz:Ch@mpla1n!22`

### set hostname
```
configure
set system host-name fw01-charlotte
commit
save 
```
Repeat exit until you get to a login prompt. Then you should see your new hostname, so go ahead and log in back to configure.

### configure interfaces
```
configure
set interfaces ethernet eth0 description SEC350-WAN
set interfaces ethernet eth1 description CHARLOTTE-DMZ
set interfaces ethernet eth2 description CHARLOTTE-LAN
set interfaces ethernet eth0 address 10.0.17.151/24
set interfaces ethernet eth1 address 172.16.50.2/29
set interfaces ethernet eth2 address 172.16.150.2/24
commit
save
```
![image](https://github.com/user-attachments/assets/2a546cc0-a012-48b3-bfc8-3884334decfa)

### configure gateway & DNS
```
configure
set protocols static route 0.0.0.0/0 next-hop 10.0.17.2
set system name-server 10.0.17.2
commit
save
```

