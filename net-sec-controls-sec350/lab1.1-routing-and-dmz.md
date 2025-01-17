# Lab 1.1, Routing and DMZ

## Configuring rw01
- changing the champuser password: `password123!`
- set hostname to `rw01-charlotte`([reference](https://github.com/charlottecroce/ChamplainTechJournals/blob/main/sysadmin-i-sys255/lab03-linux.md#set-hostname))
- add sudo user `charlotte:password123!` ([reference](https://github.com/charlottecroce/ChamplainTechJournals/blob/main/sysadmin-i-sys255/lab03-linux.md#creating-privileged-user))
- Make sure you have a static ip that matches the one in the IP assignments spreadsheet: use **nmtui**, set IP to `10.0.17.51/24` and gateway/DNS to `10.0.17.2` \
![image](https://github.com/user-attachments/assets/46252357-1387-45bd-a4ae-ede9e12417c9)


## fw01, gateway/router/firewall ([VyOS doc](https://github.com/charlottecroce/ChamplainTechJournals/blob/main/net-sec-controls-sec350/vyos.md))
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

### Configuring NAT and DNS Forwarding for DMZ
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


## web01, web server
### basics
- Set adapter to DMZ: \
![image](https://github.com/user-attachments/assets/a2abea31-7eb8-486a-b563-3962d086ab44) \
default creds: `root:Ch@mpl@1n!22`

- set hostname to `web01-charlotte`([reference](https://github.com/charlottecroce/ChamplainTechJournals/blob/main/sysadmin-i-sys255/lab03-linux.md#set-hostname))
- add sudo user `charlotte:password123!` ([reference](https://github.com/charlottecroce/ChamplainTechJournals/blob/main/sysadmin-i-sys255/lab03-linux.md#creating-privileged-user))
- `nmtui` \
![image](https://github.com/user-attachments/assets/c69680f9-be75-4b5e-976b-cf6b508f6553) \
![image](https://github.com/user-attachments/assets/06fa4ee7-ce28-40d2-8193-3f84b03b41d1) 

### configure httpd
- install httpd ([reference](https://github.com/charlottecroce/ChamplainTechJournals/blob/main/sysadmin-i-sys255/lab08-apache.md#install-httpd))


### on rw01, testing web service
- any address in your DMZ should route via fw01’s WAN interface. We do this with a static route on rw01
- anything addressed to the 172.16.50.0/29 network will go through the 10.0.17.151 router 
```
sudo ip route add 172.16.50.0/29 via 10.0.17.151
sudo systemctl restart NetworkManager
traceroute 172.16.50.3
```


## log01, rsyslog server
log01 will be initially in the DMZ, later we will change this to a segmented network area 
### basics
![image](https://github.com/user-attachments/assets/b7112a43-e0e0-4d8c-af36-a7a925ccc1d8) 
- set hostname to `log01-charlotte`([reference](https://github.com/charlottecroce/ChamplainTechJournals/blob/main/sysadmin-i-sys255/lab03-linux.md#set-hostname))
- add sudo user `charlotte:password123!` ([reference](https://github.com/charlottecroce/ChamplainTechJournals/blob/main/sysadmin-i-sys255/lab03-linux.md#creating-privileged-user))


### rsyslog setup
![image](https://github.com/user-attachments/assets/4b9ac768-72f6-4ef4-92ed-5be231e63c7b) \
![image](https://github.com/user-attachments/assets/cd26c18f-74b8-481c-bc37-8c602f7f46c7) 


allow UDP and TCP 514 for syslog traffic
```
sudo firewall-cmd --add-port=514/tcp --permament
sudo firewall-cmd --add-port=514/udp --permament
sudo firewall-cmd --reload
```
![image](https://github.com/user-attachments/assets/62b95926-6b2a-42e2-a12f-610b1a3336b8) 

On log01, the `/etc/rsyslog.conf` file needs to be modified to receive syslog messages over ports 514 tcp and udp.  Uncomment the appropriate lines (see below) and restart the rsyslog service.
![image](https://github.com/user-attachments/assets/48994d9b-0f17-4626-ab9d-985d37c5e506) \
![image](https://github.com/user-attachments/assets/b7c9efbf-0819-4381-99f7-14826220bb8a) 

### on web01, configure log forwarding to log01
- `sudo yum install rsyslog`
- Create the following file: `/etc/rsyslog.d/sec350.conf` and restart rsyslog on web01
![image](https://github.com/user-attachments/assets/143d58a5-5713-4425-b1d5-d8f9dcf63cf0)

- monitor incoming logs on log01: `tail -f /var/log/messages`
- create test log on web01: `logger -t test TESTFROMWEB01TOLOG01`

