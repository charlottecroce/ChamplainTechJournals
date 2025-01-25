# lab01- Network Management

## nmon1-charlotte
- setup with hostname, username, networking (10.0.5.11, remember: add `charlotte.local` to search domain)
- add record to DNS manager \
![image](https://github.com/user-attachments/assets/40d632c5-18c8-42b0-a938-19f6aabce1d0)

```
I had trouble reaching the internet on nmon1, then realized fw01 couldn't reach the internet as well.
idk what happened but I rebooted fw01 and it worked again
```

## enable SNMP services on pfSense
- web dashboard (10.0.5.2)
- services -> SNMP \
![image](https://github.com/user-attachments/assets/27e9470d-e84b-4e8b-8076-cfcbc9b54dea) \
![image](https://github.com/user-attachments/assets/bcdeb3dd-1245-4fc0-aff3-0a84cb383c8f)
- restart SNMP service \
![image](https://github.com/user-attachments/assets/727824d9-510f-4235-8e62-7360a41ebae2)


## Install and Test SNMP Client on nmon01
- `sudo yum install net-snmp-utils` \
![image](https://github.com/user-attachments/assets/c2924ebd-c975-4cbf-9b0e-b26e36954fdb)

## Install SNMPD (a SNMP Server) on web01
- set up web01 (10.0.5.12, you know the drill by now)
- `sudo yum install net-snmp-utils net-snmp`
- The default snmp configuration does not suit our purpose. Make a backup copy of /etc/snmp/snmpd.conf and create a new/blank version.
  - `sudo cp /etc/snmp/snmpd.conf /etc/snmp/snmpd.conf.backup` \
![image](https://github.com/user-attachments/assets/38e9d23f-a37a-4e61-948c-b949cbb19acc)
- allow 161/udp through firewall
```
sudo firewall-cmd --add-port=161/udp --permanent`
sudo firewall-cmd --reload`
```
- enable/start snmpd
```
sudo systemctl enable snmpd
sudo systemctl start snmpd
```

## install the SNMP Service Feature on AD01 using Server Manager on MGMT
## install the SNMP-Tools Remote Administration Feature on MGM01
![image](https://github.com/user-attachments/assets/545f45bb-c125-4f69-9447-b605773f26be) \
![image](https://github.com/user-attachments/assets/f62408cf-24bd-4947-9277-df5637f800e5)


## Enable Remote Management on AD01
Remote Computer Management does not work immediately for our remote AD01 Server due to firewall restrictions as seen in the error message. \
![image](https://github.com/user-attachments/assets/f6c94f07-746a-4cc1-8f09-db5eb76f08a5) \
You will need to fix this by invoking a remote PowerShell session with AD01 from mgmt01. \
![image](https://github.com/user-attachments/assets/b60a950e-bc09-424d-93cc-38c55deb0105)

## SNMP Service Security Properties on AD01
- Adjust the SNMP service properties on AD01 to add the SYS265 community string and limit queries to those from nmon01. \
![image](https://github.com/user-attachments/assets/2629d201-965b-4a1e-8afe-7b88ebcbddd9)
- Restart the SNMP Service on ad01


## Capturing snmp packets nmon01->web01
- on web01: `tcpdump -i ens192 port 161 -c10 -AAA`
- on nom01: `snmpwalk -Os -c SYS265 -v2c web01-charlotte system`
