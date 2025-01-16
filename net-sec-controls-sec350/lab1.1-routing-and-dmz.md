# Lab 1.1, Routing and DMZ

## Configuring rw01
- Secure your champuser default account by changing the password: `password123!`
- Add a new sudo user `charlotte:password123!` - `sudo usermod -aG sudo charlotte`
- Set your hostname: `sudo hostnamectl set-hostname rw01-charlotte`
- Make sure you have a static ip that matches the one in the IP assignments spreadsheet: use nmtui, set IP to `10.0.17.51/24` and gateway/DNS to `10.0.17.2` \
![image](https://github.com/user-attachments/assets/46252357-1387-45bd-a4ae-ede9e12417c9)


## fw01
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

### Configuring NAT and DNS Forwarding
```
configure
set nat source rule 10 description "NAT FROM DMZ to WAN"
set nat source rule 10 outbound-interface eth0
set nat source rule 10 source address 172.16.50.0/29
set nat source rule 10 translation address masquerade
set service dns forwarding listen-address 172.16.50.2
set service dns forwarding allow-from 172.16.50.0/29
set service dns forwarding system
commit
save
```
![image](https://github.com/user-attachments/assets/2fe9dd01-e8e0-48c6-86a0-6f41fba39886)


## web01
Set adapter to DMZ: \
![image](https://github.com/user-attachments/assets/a2abea31-7eb8-486a-b563-3962d086ab44) \
default creds: `root:Ch@mpl@1n!22`
```
adduser charlotte
passwd charlotte (password123!)
usermod -aG wheel charlotte
```

nmtui \
![image](https://github.com/user-attachments/assets/c69680f9-be75-4b5e-976b-cf6b508f6553) \
![image](https://github.com/user-attachments/assets/06fa4ee7-ce28-40d2-8193-3f84b03b41d1) \

install httpd ([use this doc](https://github.com/charlottecroce/ChamplainTechJournals/blob/main/sysadmin-i-sys255/lab08-apache.md#install-httpd))

## log01
![image](https://github.com/user-attachments/assets/b7112a43-e0e0-4d8c-af36-a7a925ccc1d8) \
```
adduser charlotte
passwd charlotte (password123!)
usermod -aG wheel charlotte
```

![image](https://github.com/user-attachments/assets/4b9ac768-72f6-4ef4-92ed-5be231e63c7b) \
![image](https://github.com/user-attachments/assets/cd26c18f-74b8-481c-bc37-8c602f7f46c7) \
log01 will be initially in the DMZ, later we will change this to a segmented network area


## on rw01, testing web service
- any address in your DMZ should route via fw01’s WAN interface. We do this with a static route on rw01
- anything addressed to the 172.16.50.0/29 network will go through the 10.0.17.151 router \
```
sudo ip route add 172.16.50.0/29 via 10.0.17.151
sudo systemctl restart NetworkManager
traceroute 172.16.50.3
```
